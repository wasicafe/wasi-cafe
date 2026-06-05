# Wasi Café

Sitio web de **Wasi Café**, una cafetería de café de especialidad en **San Isidro, Lima, Perú**. Presenta la cafetería, su carta (café, sándwiches, hamburguesas y postres) y un curso de café & barismo.

- **Producción:** [wasicafe.com](https://wasicafe.com)
- **Repo:** `wasicafe/wasi-cafe` · rama de producción: `main`
- **Despliegue:** automático vía **Cloudflare Pages** en cada push a `main` (no hay GitHub Pages ni Actions). Para publicar se necesita la cuenta de GitHub `wasicafe` (`gh auth switch --user wasicafe`).

## Stack

Sitio **estático** (HTML/CSS/JS plano, sin framework ni bundler). El CSS y el JS viven embebidos en cada `.html`. SEO con metadatos, Open Graph/Twitter, JSON-LD (`CafeOrCoffeeShop`, `Menu`, `Course`, `FAQPage`, `BreadcrumbList`), `robots.txt` y `sitemap.xml`. Incluye PWA (manifest + íconos), página 404 con marca y cabeceras de seguridad para Cloudflare.

## Estructura (`version final de wasi/` = raíz del sitio publicado)

| Archivo | Rol |
|---|---|
| `index.html` | **Home**, servida como `/`. Fuente de verdad de la portada. |
| `carta.html` | Carta / menú (`/carta.html`). Incluye JSON-LD `Menu` con todas las secciones e ítems. |
| `curso.html` | Curso de café & barismo (`/curso.html`). |
| `404.html` | Página de error con marca (Cloudflare la sirve en 404). |
| `manifest.webmanifest` | Manifiesto PWA. |
| `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | Set de íconos / favicons (derivados de `LOGOS.png`). |
| `og-image.png` | Imagen social 1200×630 para compartir en redes. |
| `_headers` | Cabeceras HTTP de seguridad y caché (Cloudflare Pages). |
| `_redirects` | Redirecciones (p. ej. `/home.html → /` 301). |
| `robots.txt`, `sitemap.xml` | SEO. Listan `/`, `carta.html`, `curso.html`. |
| `LOGOS.png` | Logotipo de marca. |
| `serve.rb` | Servidor estático local (Ruby/WEBrick), puerto 8080. |

Material de trabajo fuera del sitio (`wasi-cafe-carta-mobile.html`, `wasicafe-branding.html`) está en `.gitignore`.

## Cómo correr en local

```bash
ruby "version final de wasi/serve.rb"   # o: npm start
# luego abre http://localhost:8080/
```

`version final de wasi/.claude/launch.json` arranca lo mismo (Ruby `serve.rb`, puerto 8080).

## Notas

- **Fuente de verdad:** `index.html` es la home. (El antiguo `home.html`, un duplicado huérfano que no se servía, fue eliminado; cualquier acceso a `/home.html` redirige a `/` con 301.) Los alias `cp home.html index.html` / `cp index.html carta.html` que pudieran existir en `settings.local.json` quedaron **obsoletos** — no los uses: sobrescriben páginas publicables.
- **Para publicar:** `git push` a `main` con la cuenta `wasicafe` → Cloudflare despliega en ~1–2 min.

## Pendientes

- **Refactor a CSS/JS compartido.** Cada página repite el CSS/JS embebido; extraerlo a `styles.css`/`main.js` compartidos reduciría duplicación y evitaría desincronización.
- **IDs duplicados pre-existentes** `darkIcon` / `hdrDarkIcon` en `carta.html` (HTML inválido, inofensivo; tocarlo afecta el toggle de tema).
- **Verificar el handle de TikTok** (`@wasi.caf`): parece truncado frente a Instagram `wasi.cafe`; confirmar el correcto.
