# docs.second-ride.de: MkDocs-Seite hinter nginx, gebaut von Coolify bei
# jedem Push auf main.
#
# Deploy-Gate: `mkdocs build --strict` macht jede Warnung zum Fehler (kaputte
# interne Links, fehlende Seiten in der Navigation, fehlende Plugins). Dann
# entsteht kein Image, und die laufende Version bleibt.

FROM python:3.12-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdocs build --strict -d /site \
    && cp /site/llms-full.txt /site/all-docs


FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /site /usr/share/nginx/html
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --start-interval=2s --retries=3 \
    CMD ["wget", "-q", "--spider", "http://127.0.0.1/"]
