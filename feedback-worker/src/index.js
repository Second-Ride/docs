/**
 * Rückmeldungen aus dem Formular am Seitenende der Doku als GitHub-Issue
 * anlegen (Cloudflare Worker).
 *
 * Das Formular (overrides/partials/feedback.html, docs/javascripts/feedback.js)
 * schickt JSON per POST hierher. Der Worker prüft die Eingabe, baut Titel und
 * Text des Issues selbst zusammen und legt es mit dem Token aus dem Secret
 * GITHUB_TOKEN an. Das Token verlässt den Worker nie. Besucher brauchen kein
 * GitHub-Konto.
 *
 * Einrichtung und Betrieb: README.md in diesem Ordner.
 */

const MAX_BODY_BYTES = 8 * 1024;
const MIN_MESSAGE = 10;
const MAX_MESSAGE = 2000;
const MAX_NAME = 60;
const MAX_TITLE = 120;
const MAX_LINKS = 2;
// Wer schneller als das nach dem ersten Klick ins Feld abschickt, ist kein Mensch
const MIN_FILL_MS = 1500;

export default {
  async fetch(request, env) {
    const cors = corsHeaders(request, env);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: cors ? 204 : 403, headers: cors ?? {} });
    }
    if (request.method !== "POST") {
      return json({ error: "method_not_allowed" }, 405, cors);
    }
    // Ohne erlaubte Herkunft (fremde Seite, Skript ohne Origin) wird nichts angelegt
    if (!cors) {
      return json({ error: "origin_not_allowed" }, 403);
    }

    const ip = request.headers.get("CF-Connecting-IP") ?? "unknown";
    if (!(await withinLimits(env, ip))) {
      return json({ error: "rate_limited" }, 429, cors);
    }

    let input;
    try {
      input = JSON.parse(await readLimited(request, MAX_BODY_BYTES));
    } catch {
      return json({ error: "invalid_body" }, 400, cors);
    }

    const checked = validate(input, env);
    if (checked.error) {
      return json({ error: checked.error }, checked.status ?? 400, cors);
    }
    if (checked.silent) {
      // Honigtopf-Feld ausgefüllt: Bot. Erfolg vortäuschen, nichts anlegen.
      return json({ ok: true }, 200, cors);
    }

    if (!env.GITHUB_TOKEN) {
      log("error", "GITHUB_TOKEN fehlt");
      return json({ error: "not_configured" }, 500, cors);
    }

    try {
      const issue = await createIssue(env, buildIssue(checked.value, env));
      return json({ ok: true, issue_url: issue.html_url, number: issue.number }, 200, cors);
    } catch (err) {
      log("error", "Issue konnte nicht angelegt werden", { reason: String(err.message ?? err) });
      return json({ error: "github_failed" }, 502, cors);
    }
  },
};

/** Erlaubte Herkunft prüfen und CORS-Header liefern, sonst null. */
export function corsHeaders(request, env) {
  const origin = request.headers.get("Origin");
  if (!origin) return null;
  const allowed = (env.ALLOWED_ORIGINS ?? "")
    .split(",")
    .map((o) => o.trim())
    .filter(Boolean);
  if (!allowed.includes(origin)) return null;
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };
}

async function withinLimits(env, ip) {
  // Beide Zähler sind optional, damit der Worker auch ohne sie läuft (z.B. lokal)
  if (env.IP_LIMITER && !(await env.IP_LIMITER.limit({ key: ip })).success) return false;
  if (env.GLOBAL_LIMITER && !(await env.GLOBAL_LIMITER.limit({ key: "all" })).success) return false;
  return true;
}

/** Körper lesen, aber bei mehr als `max` Bytes abbrechen. */
async function readLimited(request, max) {
  const declared = Number(request.headers.get("Content-Length"));
  if (declared > max) throw new Error("too_large");
  const reader = request.body?.getReader();
  if (!reader) throw new Error("empty");
  const chunks = [];
  let size = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    size += value.byteLength;
    if (size > max) {
      await reader.cancel();
      throw new Error("too_large");
    }
    chunks.push(value);
  }
  const all = new Uint8Array(size);
  let offset = 0;
  for (const chunk of chunks) {
    all.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return new TextDecoder().decode(all);
}

/** Eingabe prüfen. Liefert { value } oder { error, status } oder { silent }. */
export function validate(input, env) {
  if (!input || typeof input !== "object") return { error: "invalid_body" };

  if (typeof input.website === "string" && input.website.trim() !== "") {
    return { silent: true };
  }

  const message = typeof input.message === "string" ? input.message.trim() : "";
  if (message.length < MIN_MESSAGE) return { error: "message_too_short" };
  if (message.length > MAX_MESSAGE) return { error: "message_too_long" };
  if ((message.match(/https?:\/\//gi) ?? []).length > MAX_LINKS) return { error: "too_many_links" };

  if (!(Number(input.elapsed) >= MIN_FILL_MS)) return { error: "too_fast", status: 429 };

  const name = oneLine(input.name).slice(0, MAX_NAME);

  const siteUrl = env.SITE_URL ?? "";
  let page;
  try {
    page = new URL(String(input.page ?? ""));
  } catch {
    return { error: "invalid_page" };
  }
  if (!siteUrl || !page.href.startsWith(siteUrl)) return { error: "invalid_page" };
  // Ohne Suchparameter, damit keine Tracking-Reste im öffentlichen Issue stehen
  const pageUrl = `${page.origin}${page.pathname}${page.hash}`;

  const title = oneLine(input.title).slice(0, MAX_TITLE) || page.pathname;
  const src = typeof input.src === "string" && /^[\p{L}\p{N}_\-./ ]{1,200}\.md$/u.test(input.src) && !input.src.includes("..")
    ? input.src
    : "";

  return { value: { message, name, pageUrl, title, src } };
}

/** Titel und Text des Issues. Alles, was Besucher schreiben, wird entschärft. */
export function buildIssue({ message, name, pageUrl, title, src }, env) {
  const repo = env.GITHUB_REPO;
  const quoted = neutralize(message)
    .split(/\r?\n/)
    .map((line) => `> ${line}`)
    .join("\n");

  const lines = [`**Seite:** ${pageUrl}`];
  if (src) lines.push(`**Datei:** [\`${src}\`](https://github.com/${repo}/blob/main/docs/${encodeURI(src)})`);
  lines.push(`**Von:** ${name ? neutralize(name) : "anonym"}`, "", quoted, "", "---", "_Über das Rückmeldeformular der Doku gesendet._");

  return {
    title: `Rückmeldung: ${neutralize(title)}`.slice(0, 200),
    body: lines.join("\n"),
    labels: env.LABEL ? [env.LABEL] : [],
  };
}

async function createIssue(env, issue) {
  const response = await fetch(`https://api.github.com/repos/${env.GITHUB_REPO}/issues`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "Content-Type": "application/json",
      "User-Agent": "second-ride-docs-feedback",
      "X-GitHub-Api-Version": "2022-11-28",
    },
    body: JSON.stringify(issue),
  });
  if (response.status !== 201) {
    throw new Error(`GitHub antwortete mit ${response.status}: ${(await response.text()).slice(0, 300)}`);
  }
  return response.json();
}

function oneLine(value) {
  return typeof value === "string" ? value.replace(/\s+/g, " ").trim() : "";
}

/** Keine @-Erwähnungen (würden Personen benachrichtigen), kein rohes HTML. */
function neutralize(text) {
  return text.replace(/@(?=[\w-])/g, "@​").replace(/</g, "&lt;");
}

function json(data, status, cors) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", ...(cors ?? {}) },
  });
}

function log(level, message, extra = {}) {
  console[level](JSON.stringify({ message, ...extra }));
}
