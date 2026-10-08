// Ausführen: node --test feedback-worker/test/
import test from "node:test";
import assert from "node:assert/strict";
import worker from "../src/index.js";

const ORIGIN = "https://docs.second-ride.de";

const baseEnv = () => ({
  GITHUB_REPO: "Second-Ride/docs",
  LABEL: "doku-feedback",
  SITE_URL: "https://docs.second-ride.de/",
  ALLOWED_ORIGINS: ORIGIN,
  GITHUB_TOKEN: "test-token",
});

const payload = (over = {}) => ({
  message: "In Schritt 3 fehlt die Angabe zum Drehmoment der Mutter.",
  name: "Hans",
  website: "",
  elapsed: 8000,
  page: `${ORIGIN}/conversion-manual/MID50/01-schwalbe/?utm=x#schritt-3`,
  title: "Schwalbe",
  src: "conversion-manual/MID50/01-schwalbe/index.md",
  ...over,
});

const post = (body, { origin = ORIGIN, raw } = {}) =>
  new Request(`${ORIGIN}/api/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...(origin ? { Origin: origin } : {}) },
    body: raw ?? JSON.stringify(body),
  });

// GitHub-Aufrufe abfangen
function mockGitHub(t, status = 201) {
  const calls = [];
  t.mock.method(globalThis, "fetch", async (url, init) => {
    calls.push({ url, init, body: JSON.parse(init.body) });
    return new Response(JSON.stringify({ html_url: "https://github.com/Second-Ride/docs/issues/42", number: 42 }), { status });
  });
  return calls;
}

test("legt ein Issue an und liefert dessen Adresse", async (t) => {
  const calls = mockGitHub(t);
  const res = await worker.fetch(post(payload()), baseEnv());
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { ok: true, issue_url: "https://github.com/Second-Ride/docs/issues/42", number: 42 });
  assert.equal(res.headers.get("Access-Control-Allow-Origin"), ORIGIN);

  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, "https://api.github.com/repos/Second-Ride/docs/issues");
  assert.equal(calls[0].init.headers.Authorization, "Bearer test-token");
  const { title, body, labels } = calls[0].body;
  assert.equal(title, "Rückmeldung: Schwalbe");
  assert.deepEqual(labels, ["doku-feedback"]);
  assert.match(body, /\*\*Seite:\*\* https:\/\/docs\.second-ride\.de\/conversion-manual\/MID50\/01-schwalbe\/#schritt-3/);
  assert.ok(!body.includes("utm="), "Suchparameter gehören nicht ins Issue");
  assert.match(body, /\*\*Von:\*\* Hans/);
  assert.match(body, /> In Schritt 3 fehlt die Angabe/);
  assert.match(body, /blob\/main\/docs\/conversion-manual\/MID50\/01-schwalbe\/index\.md/);
});

test("ohne Namen steht anonym im Issue", async (t) => {
  const calls = mockGitHub(t);
  await worker.fetch(post(payload({ name: "  " })), baseEnv());
  assert.match(calls[0].body.body, /\*\*Von:\*\* anonym/);
});

test("entschärft @-Erwähnungen und HTML", async (t) => {
  const calls = mockGitHub(t);
  await worker.fetch(post(payload({ message: "Hallo @Carlo-SR <script>alert(1)</script> siehe oben" })), baseEnv());
  const body = calls[0].body.body;
  assert.ok(!body.includes("@Carlo-SR"));
  assert.ok(!body.includes("<script>"));
});

test("fremde Herkunft wird abgewiesen, ohne GitHub anzufragen", async (t) => {
  const calls = mockGitHub(t);
  const res = await worker.fetch(post(payload(), { origin: "https://evil.example" }), baseEnv());
  assert.equal(res.status, 403);
  const noOrigin = await worker.fetch(post(payload(), { origin: null }), baseEnv());
  assert.equal(noOrigin.status, 403);
  assert.equal(calls.length, 0);
});

test("Preflight wird beantwortet", async () => {
  const res = await worker.fetch(
    new Request(`${ORIGIN}/api/feedback`, { method: "OPTIONS", headers: { Origin: ORIGIN } }),
    baseEnv(),
  );
  assert.equal(res.status, 204);
  assert.match(res.headers.get("Access-Control-Allow-Methods"), /POST/);
});

test("GET ist nicht erlaubt", async () => {
  const res = await worker.fetch(new Request(`${ORIGIN}/api/feedback`, { headers: { Origin: ORIGIN } }), baseEnv());
  assert.equal(res.status, 405);
});

test("Honigtopf: Bot bekommt Erfolg, es entsteht kein Issue", async (t) => {
  const calls = mockGitHub(t);
  const res = await worker.fetch(post(payload({ website: "http://spam.example" })), baseEnv());
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { ok: true });
  assert.equal(calls.length, 0);
});

test("zu schnell abgeschickt wird abgelehnt", async (t) => {
  const calls = mockGitHub(t);
  const res = await worker.fetch(post(payload({ elapsed: 200 })), baseEnv());
  assert.equal(res.status, 429);
  assert.equal((await res.json()).error, "too_fast");
  assert.equal(calls.length, 0);
});

for (const [name, over, error] of [
  ["zu kurze Nachricht", { message: "kaputt" }, "message_too_short"],
  ["zu lange Nachricht", { message: "x".repeat(2001) }, "message_too_long"],
  ["zu viele Links", { message: "http://a.example http://b.example http://c.example" }, "too_many_links"],
  ["Seite von woanders", { page: "https://example.com/seite/" }, "invalid_page"],
  ["Seite kaputt", { page: "keine url" }, "invalid_page"],
]) {
  test(`lehnt ab: ${name}`, async (t) => {
    const calls = mockGitHub(t);
    const res = await worker.fetch(post(payload(over)), baseEnv());
    assert.equal(res.status, 400);
    assert.equal((await res.json()).error, error);
    assert.equal(calls.length, 0);
  });
}

test("ungültiger Dateipfad wird weggelassen statt übernommen", async (t) => {
  const calls = mockGitHub(t);
  await worker.fetch(post(payload({ src: "../../etc/passwd" })), baseEnv());
  assert.ok(!calls[0].body.body.includes("**Datei:**"));
});

test("zu großer Körper wird abgewiesen", async (t) => {
  const calls = mockGitHub(t);
  const res = await worker.fetch(post(null, { raw: JSON.stringify({ message: "x".repeat(20000) }) }), baseEnv());
  assert.equal(res.status, 400);
  assert.equal(calls.length, 0);
});

test("kein JSON", async (t) => {
  mockGitHub(t);
  const res = await worker.fetch(post(null, { raw: "das ist kein json" }), baseEnv());
  assert.equal(res.status, 400);
});

test("Rate Limit schlägt zu", async (t) => {
  const calls = mockGitHub(t);
  const env = { ...baseEnv(), IP_LIMITER: { limit: async () => ({ success: false }) } };
  const res = await worker.fetch(post(payload()), env);
  assert.equal(res.status, 429);
  assert.equal((await res.json()).error, "rate_limited");
  assert.equal(calls.length, 0);
});

test("GitHub-Fehler wird als 502 gemeldet, ohne Token preiszugeben", async (t) => {
  mockGitHub(t, 403);
  t.mock.method(console, "error", () => {});
  const res = await worker.fetch(post(payload()), baseEnv());
  assert.equal(res.status, 502);
  assert.ok(!(await res.text()).includes("test-token"));
});

test("fehlendes Token wird gemeldet", async (t) => {
  mockGitHub(t);
  t.mock.method(console, "error", () => {});
  const { GITHUB_TOKEN, ...env } = baseEnv();
  const res = await worker.fetch(post(payload()), env);
  assert.equal(res.status, 500);
  assert.equal((await res.json()).error, "not_configured");
});
