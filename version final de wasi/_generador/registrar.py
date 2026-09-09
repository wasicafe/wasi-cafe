#!/usr/bin/env python3
"""Reconstruye el índice del blog y el sitemap leyendo la carpeta blog/.

Un post que existe pero no está enlazado desde /blog ni en el sitemap es
prácticamente invisible: nadie llega a él. Y mantener tres sitios a mano
(el post, la tarjeta del índice y la línea del sitemap) es garantía de que
antes o después uno se quede atrás.

Aquí la carpeta blog/ es la única fuente de verdad: se lee lo que hay y se
regeneran las tarjetas, el listado de datos estructurados y el sitemap.
Idempotente: correrlo dos veces da el mismo resultado.

Uso:  python3 registrar.py
"""
import re, json, pathlib, html

AQUI = pathlib.Path(__file__).resolve().parent
SITIO = AQUI.parent
BLOG = SITIO / 'blog'
BASE = 'https://wasicafe.com'

# Páginas fijas del sitio, con su prioridad. El resto sale del blog.
FIJAS = [('/', '1.0', 'weekly'), ('/carta', '0.9', 'weekly'), ('/curso', '0.8', 'monthly'),
         ('/blog', '0.8', 'weekly'), ('/sellos', '0.5', 'monthly')]


def leer(p):
    h = p.read_text(encoding='utf-8')
    def uno(pat):
        m = re.search(pat, h, re.S)
        return html.unescape(m.group(1)).strip() if m else ''
    d = {'slug': p.stem,
         'h1': uno(r'<h1>(.*?)</h1>'),
         'desc': uno(r'<meta name="description" content="(.*?)">'),
         'eyebrow': uno(r'<p class="eyebrow">(.*?)</p>'),
         'fecha': uno(r'"datePublished"\s*:\s*"(.*?)"')}
    return d if d['slug'] and d['h1'] else None


def main() -> None:
    posts = sorted(filter(None, (leer(p) for p in BLOG.glob('*.html'))),
                   key=lambda d: (d['fecha'], d['slug']), reverse=True)
    print(f'  {len(posts)} posts encontrados en blog/')

    # ── índice: tarjetas ──
    idx = (SITIO / 'blog.html').read_text(encoding='utf-8')
    tarjetas = ''.join(
        f'<a class="post" href="/blog/{d["slug"]}"><span class="k">{html.escape(d["eyebrow"])}</span>'
        f'<h2>{html.escape(d["h1"])}</h2><p>{html.escape(d["desc"])}</p>'
        f'<span class="more">Leer →</span></a>' for d in posts)
    nuevo, n = re.subn(r'(<a class="post" href="/blog/).*(<span class="more">Leer →</span></a>)',
                       lambda m: tarjetas, idx, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('no encontré el bloque de tarjetas en blog.html')

    # ── índice: listado de datos estructurados ──
    lista = ', '.join(json.dumps(
        {"@type": "BlogPosting", "headline": d['h1'], "url": f'{BASE}/blog/{d["slug"]}',
         "datePublished": d['fecha']}, ensure_ascii=False) for d in posts)
    nuevo, n2 = re.subn(r'(\{"@type": "BlogPosting", "headline".*"datePublished": "[\d-]+"\})',
                        lambda m: lista, nuevo, count=1, flags=re.S)
    (SITIO / 'blog.html').write_text(nuevo, encoding='utf-8')
    print(f'  blog.html: {len(posts)} tarjetas' + (f' + listado JSON-LD' if n2 else ' (JSON-LD sin tocar)'))

    # ── sitemap ──
    urls = [f'  <url><loc>{BASE}{r}</loc><changefreq>{c}</changefreq><priority>{p}</priority></url>'
            for r, p, c in FIJAS]
    urls += [f'  <url><loc>{BASE}/blog/{d["slug"]}</loc><lastmod>{d["fecha"]}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.6</priority></url>' for d in posts]
    (SITIO / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(urls) + '\n</urlset>\n', encoding='utf-8')
    print(f'  sitemap.xml: {len(urls)} URLs')


if __name__ == '__main__':
    main()
