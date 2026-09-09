#!/usr/bin/env python3
"""Genera un post del blog de Wasi Café a partir de una ficha JSON.

Por qué existe: cada post del blog es un HTML autocontenido de ~26 KB, y el 38 %
son partes fijas (fuentes, todo el CSS, cabecera, pie, scripts). Escribirlas a
mano en cada post garantiza que tarde o temprano uno salga distinto. Aquí esas
partes se leen de los .part extraídos del post de cold brew, así que son
IDÉNTICAS BYTE A BYTE en todos los posts. Lo único que cambia es lo que debe
cambiar: meta, datos estructurados y el artículo.

Uso:  python3 generar.py ficha.json [ficha2.json ...]
"""
import json, sys, pathlib, html, re

AQUI = pathlib.Path(__file__).resolve().parent
SITIO = AQUI.parent / 'version final de wasi'
BLOG = SITIO / 'blog'
BASE = 'https://wasicafe.com'

PARTES = {n: (AQUI / f'{n}.part').read_text(encoding='utf-8')
          for n in ('A_cabecera', 'B_recursos', 'C_chrome', 'D_pie')}


def esc(t: str) -> str:
    """Escapa para un atributo HTML. Las comillas rompen los meta."""
    return html.escape(t, quote=True)


def meta(f: dict) -> str:
    url = f'{BASE}/blog/{f["slug"]}'
    d, og = esc(f['descripcion']), esc(f.get('ogTitulo', f['h1']))
    return (
        f'<title>{esc(f["tituloSeo"])}</title>\n'
        f'<meta name="theme-color" content="#F7F1E8">\n'
        f'<meta name="description" content="{d}">\n'
        f'<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<link rel="icon" href="/favicon-32x32.png" sizes="32x32">\n'
        f'<meta property="og:type" content="article">\n'
        f'<meta property="og:title" content="{og}">\n'
        f'<meta property="og:description" content="{d}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:image" content="{BASE}/og-image.png">\n'
        f'<meta property="og:site_name" content="Wasi Café">\n'
        f'<meta property="og:locale" content="es_PE">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{og}">\n'
        f'<meta name="twitter:description" content="{d}">\n'
        f'<meta name="twitter:image" content="{BASE}/og-image.png">\n')


def datos(f: dict) -> str:
    url = f'{BASE}/blog/{f["slug"]}'
    bloques = [
        {"@context": "https://schema.org", "@type": "BlogPosting",
         "headline": f['h1'], "description": f['descripcion'], "inLanguage": "es-PE",
         "datePublished": f['fecha'], "dateModified": f['fecha'],
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "image": f'{BASE}/og-image.png',
         "author": {"@type": "Organization", "name": "Wasi Café", "url": BASE},
         "publisher": {"@type": "Organization", "name": "Wasi Café",
                       "logo": {"@type": "ImageObject", "url": f'{BASE}/LOGOS.png'}},
         "about": f.get('about', ["Café de especialidad", "Perú"])},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + '/'},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + '/blog'},
            {"@type": "ListItem", "position": 3, "name": f['tituloCorto'], "item": url}]},
    ]
    if f.get('faq'):
        bloques.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q['p'],
             "acceptedAnswer": {"@type": "Answer", "text": q['r']}} for q in f['faq']]})
    # La ficha del negocio va en TODOS los posts: es lo que une el artículo con
    # la cafetería para un buscador o un asistente de IA.
    bloques.append({"@context": "https://schema.org", "@type": "CafeOrCoffeeShop",
                    "name": "Wasi Café", "url": BASE,
                    "image": f'{BASE}/LOGOS.png', "telephone": "+51908724496",
                    "address": {"@type": "PostalAddress",
                                "streetAddress": "Luis Felipe Villarán 904",
                                "addressLocality": "San Isidro", "addressRegion": "Lima",
                                "postalCode": "15073", "addressCountry": "PE"},
                    "geo": {"@type": "GeoCoordinates", "latitude": -12.1015761,
                            "longitude": -77.0289421},
                    "servesCuisine": ["Café de especialidad", "Peruvian", "Brunch"],
                    "priceRange": "S/ 3 - S/ 69"})
    return '\n'.join('<script type="application/ld+json">' +
                     json.dumps(b, ensure_ascii=False) + '</script>' for b in bloques)


def resolver_relacionados(f: dict) -> list:
    """Los títulos de los enlaces relacionados salen del H1 REAL del post enlazado.
    Escribirlos en la ficha invita a inventarlos (pasó en el primer post: los tres
    estaban mal). Si el slug no existe, es un error, no un enlace roto silencioso."""
    out = []
    for r in f.get('relacionados', []):
        slug = r['slug'] if isinstance(r, dict) else r
        ruta = BLOG / f'{slug}.html'
        if not ruta.exists():
            raise ValueError(f'relacionado inexistente: {slug}')
        m = re.search(r'<h1>(.*?)</h1>', ruta.read_text(encoding='utf-8'), re.S)
        out.append({'slug': slug, 'titulo': html.unescape(m.group(1)).strip()})
    return out


def articulo(f: dict) -> str:
    p = [f'<div class="crumbs"><a href="/">Inicio</a><span>›</span>'
         f'<a href="/blog">Blog</a><span>›</span>{esc(f["tituloCorto"])}</div></div>',
         '', '<article>',
         f'<div class="read ahero"><p class="eyebrow">{esc(f["eyebrow"])}</p>'
         f'<h1>{esc(f["h1"])}</h1>',
         '<p class="ameta">Blog de Wasi Café · San Isidro, Lima</p></div>',
         '<div class="read prose">', f['intro']]
    for s in f['secciones']:
        p.append(f'<h2>{esc(s["h2"])}</h2>')
        p.append(s['html'])
    p.append('</div>')
    if f.get('faq'):
        p.append('<section class="faq read"><h2>Preguntas frecuentes</h2>' + ''.join(
            f'<details><summary>{esc(q["p"])}</summary><p>{q["r"]}</p></details>'
            for q in f['faq']) + '</section>')
    p.append('  <div class="read"><div class="cta"><h3>Te esperamos en Wasi Café</h3>'
             '<p>Cafetería de especialidad en San Isidro. Ven a probar nuestro café, '
             'brunch y postres — o escríbenos.</p>'
             '<a class="btn" href="https://wa.me/51908724496?text=Hola!%20Quiero%20info%20'
             'de%20Wasi%20Caf%C3%A9%20%E2%98%95" target="_blank" rel="noopener">'
             'Escríbenos por WhatsApp</a></div>')
    p.append('  <a class="back" href="/blog">← Volver al blog</a>')
    rel = resolver_relacionados(f)
    if rel:
        p.append('  <div style="margin-top:1.4rem">' + ''.join(
            f'<a class="back" href="/blog/{r["slug"]}" style="display:block">'
            f'› {r["titulo"]}</a>' for r in rel) + '</div></div>')
    else:
        p.append('</div>')
    p.append('</article>')
    return '\n'.join(p)


def generar(ficha: dict) -> str:
    return (PARTES['A_cabecera'] + meta(ficha) + PARTES['B_recursos'] +
            datos(ficha) + PARTES['C_chrome'] + articulo(ficha) + PARTES['D_pie'])


def revisar(h: str, f: dict) -> list:
    """Comprobaciones que deben pasar ANTES de escribir el archivo."""
    fallos = []
    for etq in ('html', 'head', 'body', 'article', 'div'):
        a, c = len(re.findall(rf'<{etq}[\s>]', h)), h.count(f'</{etq}>')
        if a != c:
            fallos.append(f'{etq}: {a} abiertas vs {c} cerradas')
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            json.loads(b)
        except Exception as e:
            fallos.append(f'JSON-LD inválido: {e}')
    texto = re.sub(r'<[^>]+>', ' ', h[h.find('<div class="read prose">'):h.find('</article>')])
    if len(texto.split()) < 700:
        fallos.append(f'solo {len(texto.split())} palabras (mínimo 700)')
    if not (100 <= len(f['descripcion']) <= 165):
        fallos.append(f'meta description de {len(f["descripcion"])} caracteres (100-165)')
    if len(f['tituloSeo']) > 65:
        fallos.append(f'title de {len(f["tituloSeo"])} caracteres (máx 65)')
    return fallos


def main() -> None:
    total, malos = 0, 0
    for ruta in sys.argv[1:]:
        for f in json.loads(pathlib.Path(ruta).read_text(encoding='utf-8')):
            try:
                h = generar(f)
            except ValueError as e:
                malos += 1
                print(f'  ✗ {f["slug"]}\n      {e}')
                continue
            fallos = revisar(h, f)
            if fallos:
                malos += 1
                print(f'  ✗ {f["slug"]}')
                for x in fallos:
                    print(f'      {x}')
                continue
            (BLOG / f'{f["slug"]}.html').write_text(h, encoding='utf-8')
            total += 1
            print(f'  ✓ {f["slug"]}  ({len(h)} bytes)')
    print(f'\n{total} posts escritos' + (f', {malos} rechazados' if malos else ''))


if __name__ == '__main__':
    main()
