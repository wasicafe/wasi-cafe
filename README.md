# Wasi Cafe

Sitio web de **Wasi Cafe**, una cafetería de café de especialidad ubicada en **San Isidro, Lima, Perú**. El sitio presenta la cafetería, su carta (menú de café, sándwiches y postres) y un curso de café & postres.

- **Dominio en producción:** [wasicafe.com](https://wasicafe.com)

## Stack

Sitio **estático**, sin framework ni build step:

- **HTML / CSS / JS plano.** Todo el CSS y el JS viven embebidos (`<style>` y `<script>` en línea) dentro de cada archivo `.html`.
- No hay `package.json`, bundler, ni dependencias de Node.
- SEO: metadatos, Open Graph y JSON-LD (schema `LocalBusiness` / reseñas) embebidos en el HTML, más `robots.txt` y `sitemap.xml`.

## Estructura

Los archivos publicables están en `version final de wasi/`:

| Archivo | Rol |
|---|---|
| `index.html` | **Home**, servida como `/` (las páginas enlazan a la home con `href="/"`). Es la **fuente de verdad** de la portada. |
| `carta.html` | Página de la carta / menú (`/carta.html`). |
| `curso.html` | Página del curso de café & postres (`/curso.html`). |
| `home.html` | **Plantilla / espejo** de `index.html`. Versión más antigua y reducida (sin la sección de promos ni el schema de reseñas que sí tiene `index.html`). **No** se publica ni aparece en el sitemap. |
| `robots.txt` | Reglas de crawling. Lista solo `/`, `carta.html`, `curso.html`. |
| `sitemap.xml` | Sitemap. Lista solo `/`, `carta.html`, `curso.html` (no `home.html`). |
| `LOGOS.png` | Logotipo / imagen de marca. |

Otros archivos en la raíz del repo (`wasi-cafe-carta-mobile.html`, `wasicafe-branding.html`) son material de trabajo y están en `.gitignore`.

## Cómo correr en local

La configuración de arranque vive en `version final de wasi/.claude/launch.json` y levanta un servidor estático con Ruby/WEBrick en el **puerto 8080**:

```json
{
  "runtimeExecutable": "ruby",
  "runtimeArgs": ["serve.rb"],
  "port": 8080
}
```

> **Nota:** `serve.rb` está referenciado por `launch.json` pero actualmente **no existe en el repositorio**. Hasta que se agregue, sirve la carpeta `version final de wasi/` con cualquier servidor estático en el puerto 8080, por ejemplo:
>
> ```bash
> cd "version final de wasi"
> ruby -run -e httpd . -p 8080      # Ruby (WEBrick), equivalente al launch.json
> # o
> python3 -m http.server 8080       # alternativa con Python
> ```
>
> Luego abre <http://localhost:8080/>.

## Fuente de verdad y comandos `cp` (riesgo de sobrescritura)

El archivo `version final de wasi/.claude/settings.local.json` autoriza, entre otros, estos comandos:

```bash
cp home.html index.html     # sobrescribe index.html con el contenido de home.html
cp index.html carta.html    # sobrescribe carta.html con el contenido de index.html
```

⚠️ **Atención:** estos `cp` **sobrescriben sin aviso** archivos publicables y pueden perder cambios:

- `cp home.html index.html` reemplaza la home real (`index.html`, la fuente de verdad) por la plantilla espejo más antigua `home.html`, perdiendo la sección de promos, el schema de reseñas y los metadatos SEO adicionales que solo tiene `index.html`.
- `cp index.html carta.html` reemplaza la carta por una copia de la home, destruyendo el contenido propio de `carta.html`.

**Fuente de verdad:**

- La **home** es `index.html`. `home.html` es solo una plantilla/espejo histórico; si necesitas regenerar la home, edita `index.html` directamente, no copies desde `home.html`.
- `carta.html` y `curso.html` son páginas independientes con contenido propio; no deben generarse copiando `index.html`.

Antes de ejecutar cualquiera de esos `cp`, confirma la dirección de la copia y ten un commit limpio para poder revertir.

## Pendientes

- **Refactor a CSS/JS compartido.** Hoy cada página repite el CSS y el JS embebidos en línea. Extraer estilos y scripts comunes a archivos compartidos (p. ej. `styles.css` y `main.js`) reduciría la duplicación y evitaría que las páginas se desincronicen.
- **Agregar `serve.rb`** (o actualizar `launch.json`) para que el comando de arranque del `launch.json` funcione tal cual.
- **Consolidar `home.html`.** Decidir si se elimina la plantilla espejo o se documenta formalmente su propósito, para eliminar la ambigüedad sobre la fuente de verdad y el riesgo de los `cp`.
