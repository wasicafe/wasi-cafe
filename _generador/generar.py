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


# Textos fijos por idioma. Una ficha con "idioma": "en" sale entera en inglés
# (lang del <html>, og:locale, migas, fechas, CTA y bloque de guías).
TXT = {
    'es': {'locale': 'es_PE', 'lang': 'es-PE', 'inicio': 'Inicio', 'faq': 'Preguntas frecuentes',
           'meta': 'Blog de Wasi Café · San Isidro, Lima', 'actualizado': ' · Actualizado el ',
           'cta_t': 'Te esperamos en Wasi Café',
           'cta_p': 'Cafetería de especialidad en San Isidro. Ven a probar nuestro café, brunch y postres, o escríbenos.',
           'cta_b': 'Escríbenos por WhatsApp', 'cta_w': 'Hola!%20Quiero%20info%20de%20Wasi%20Caf%C3%A9%20%E2%98%95',
           'volver': '← Volver al blog'},
    'en': {'locale': 'en_US', 'lang': 'en', 'inicio': 'Home', 'faq': 'Frequently asked questions',
           'meta': 'Wasi Café blog · San Isidro, Lima', 'actualizado': ' · Updated ',
           'cta_t': 'See you at Wasi Café',
           'cta_p': 'Specialty coffee shop in San Isidro, Lima. Come for coffee, breakfast, brunch and desserts, or message us.',
           'cta_b': 'Message us on WhatsApp', 'cta_w': 'Hi!%20I%27d%20like%20info%20about%20Wasi%20Caf%C3%A9%20%E2%98%95',
           'volver': '← Back to the blog'},
}


def tx(f: dict) -> dict:
    return TXT[f.get('idioma', 'es')]


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
        f'<meta property="og:locale" content="{tx(f)["locale"]}">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{og}">\n'
        f'<meta name="twitter:description" content="{d}">\n'
        f'<meta name="twitter:image" content="{BASE}/og-image.png">\n')


def datos(f: dict) -> str:
    url = f'{BASE}/blog/{f["slug"]}'
    bloques = [
        {"@context": "https://schema.org", "@type": "BlogPosting",
         "headline": f['h1'], "description": f['descripcion'], "inLanguage": tx(f)["lang"],
         "datePublished": f['fecha'], "dateModified": f.get('modificado', f['fecha']),
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "image": portada(f),
         "author": {"@type": "Organization", "name": "Wasi Café", "url": BASE},
         "publisher": {"@type": "Organization", "name": "Wasi Café",
                       "logo": {"@type": "ImageObject", "url": f'{BASE}/LOGOS.png'}},
         "about": f.get('about', ["Café de especialidad", "Perú"])},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": tx(f)["inicio"], "item": BASE + '/'},
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
                                "postalCode": "15046", "addressCountry": "PE"},
                    "geo": {"@type": "GeoCoordinates", "latitude": -12.1015761,
                            "longitude": -77.0289421},
                    "servesCuisine": ["Café de especialidad", "Peruvian", "Brunch"],
                    "priceRange": "S/ 3 - S/ 69"})
    return '\n'.join('<script type="application/ld+json">' +
                     json.dumps(b, ensure_ascii=False) + '</script>' for b in bloques)


def portada(f: dict) -> str:
    """Primera foto real del artículo (si la hay) para los datos estructurados."""
    for s in f.get('secciones', []):
        for x in s.get('fotos', []):
            return BASE + x['src']
    return f'{BASE}/og-image.png'


def galeria(fotos: list) -> str:
    """Fotos reales de la carta, con nombre y precio. Pequeñas (429 px), por eso
    van en rejilla y nunca estiradas a todo el ancho."""
    celdas = ''.join(
        f'<figure style="margin:0"><img src="{esc(x["src"])}" alt="{esc(x["alt"])}" '
        f'width="429" height="333" loading="lazy" decoding="async" '
        f'style="width:100%;height:auto;aspect-ratio:429/333;object-fit:cover;border-radius:14px;display:block">'
        f'<figcaption style="font-size:.86rem;color:var(--ink-soft);margin-top:.45rem;line-height:1.4">'
        f'{esc(x["pie"])}</figcaption></figure>' for x in fotos)
    return ('<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(180px,calc(50% - .5rem)),1fr));'
            f'gap:1rem;margin:1.4rem 0 1.8rem">{celdas}</div>')


GUIAS = [
    ('desayunos-en-san-isidro-carta-precios-horario', 'Desayunos en San Isidro'),
    ('almuerzo-en-san-isidro-combos-y-precios', 'Almuerzo en San Isidro'),
    ('brunch-en-san-isidro-que-pedir-como-elegir', 'Brunch en San Isidro'),
    ('cafe-de-especialidad-san-isidro-guia', 'Café de especialidad'),
    ('sandwiches-peruanos-y-hamburguesas-san-isidro', 'Sándwiches'),
    ('postres-artesanales-cafeteria-san-isidro', 'Postres'),
    ('cafeterias-para-trabajar-laptop-san-isidro', 'Trabajar con laptop'),
    ('cafeteria-en-san-isidro-horario-como-llegar', 'Horario y cómo llegar'),
]


GUIAS_EN = ['Breakfast (in Spanish)', 'Lunch (in Spanish)', 'Brunch (in Spanish)', 'Specialty coffee (in Spanish)',
            'Sandwiches (in Spanish)', 'Desserts (in Spanish)', 'Working with a laptop (in Spanish)', 'Hours and directions (in Spanish)']


def guias(slug: str, idioma: str = 'es') -> str:
    """Bloque fijo con las guías principales: cada post empuja a las páginas que
    deben ganar las búsquedas locales. Se omite el enlace a sí mismo."""
    chip = ('display:inline-block;padding:.45rem .9rem;border:1px solid var(--line);border-radius:999px;'
            'font-size:.88rem;color:var(--ink);text-decoration:none;background:var(--paper)')
    if idioma == 'en':
        items = [(f'/blog/{s}', e) for (s, _), e in zip(GUIAS, GUIAS_EN)] + [('/carta', 'Menu with prices'), ('/productos', 'All products (in Spanish)')]
        titulo = 'More Wasi Café guides'
    else:
        items = [(f'/blog/{s}', t) for s, t in GUIAS if s != slug] + [('/carta', 'Carta con precios'), ('/productos', 'Todos los productos')]
        titulo = 'Guías de Wasi Café en San Isidro'
    return ('  <nav class="read guias" aria-label="Guías de Wasi Café en San Isidro" style="display:block;margin-top:2.6rem">'
            '<p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:0 0 .8rem">'
            f'{titulo}</p><ul style="list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.5rem">'
            + ''.join(f'<li><a href="{h}" style="{chip}">{t}</a></li>' for h, t in items) + '</ul></nav>')


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


MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
         'septiembre', 'octubre', 'noviembre', 'diciembre']


def fecha_legible(iso: str) -> str:
    a, m, d = iso.split('-')
    return f'{int(d)} de {MESES[int(m) - 1]} de {a}'


MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']


def fecha_idioma(f: dict) -> str:
    if f.get('idioma') == 'en':
        a, m, d = f['modificado'].split('-')
        return f'{MONTHS[int(m) - 1]} {int(d)}, {a}'
    return fecha_legible(f['modificado'])


def articulo(f: dict) -> str:
    T = tx(f)
    p = [f'<div class="crumbs"><a href="/">{T["inicio"]}</a><span>›</span>'
         f'<a href="/blog">Blog</a><span>›</span>{esc(f["tituloCorto"])}</div></div>',
         '', '<article>',
         f'<div class="read ahero"><p class="eyebrow">{esc(f["eyebrow"])}</p>'
         f'<h1>{esc(f["h1"])}</h1>',
         f'<p class="ameta">{T["meta"]}' + (f'{T["actualizado"]}{fecha_idioma(f)}' if f.get('modificado') else '') + '</p></div>',
         '<div class="read prose">', f['intro']]
    for s in f['secciones']:
        p.append(f'<h2>{esc(s["h2"])}</h2>')
        p.append(s['html'])
        if s.get('fotos'):
            p.append(galeria(s['fotos']))
    p.append('</div>')
    if f.get('faq'):
        p.append(f'<section class="faq read"><h2>{T["faq"]}</h2>' + ''.join(
            f'<details><summary>{esc(q["p"])}</summary><p>{q["r"]}</p></details>'
            for q in f['faq']) + '</section>')
    p.append(guias(f['slug'], f.get('idioma', 'es')))
    p.append(f'  <div class="read"><div class="cta"><h3>{T["cta_t"]}</h3>'
             f'<p>{T["cta_p"]}</p>'
             f'<a class="btn" href="https://wa.me/51908724496?text={T["cta_w"]}" target="_blank" rel="noopener">'
             f'{T["cta_b"]}</a></div>')
    p.append(f'  <a class="back" href="/blog">{T["volver"]}</a>')
    rel = resolver_relacionados(f)
    if rel:
        p.append('  <div style="margin-top:1.4rem">' + ''.join(
            f'<a class="back" href="/blog/{r["slug"]}" style="display:block">'
            f'› {r["titulo"]}</a>' for r in rel) + '</div></div>')
    else:
        p.append('</div>')
    p.append('</article>')
    return '\n'.join(p)


_MAPA_PROD = {}


def mapa_productos(idioma: str) -> list:
    """(nombre, url) de cada producto con página propia, el nombre más largo primero
    para que «Pie de limón + Café Americano» gane a «Pie de limón»."""
    if idioma not in _MAPA_PROD:
        import productos  # import tardío: productos importa este módulo
        lista = []
        for x in productos.leer_carta():
            if not x['img']:
                continue
            if idioma == 'en':
                lista.append((x['en'], f'/en/product/{x["slug_en"]}'))
            else:
                lista.append((x['n'], f'/producto/{x["slug"]}'))
        _MAPA_PROD[idioma] = sorted(lista, key=lambda z: -len(z[0]))
    return _MAPA_PROD[idioma]


def enlazar_productos(h: str, idioma: str = 'es') -> str:
    """Convierte «<strong>Pie de Limón (S/ 15.90)</strong>» del artículo en enlace a la
    página del producto. Solo dentro del artículo, solo con el precio al lado (así no se
    enlaza una palabra suelta) y sin tocar lo que ya es enlace: se puede correr dos veces."""
    i, j = h.find('<div class="read prose">'), h.find('</article>')
    if i < 0 or j < 0:
        return h
    cuerpo = h[i:j]
    for nombre, url in mapa_productos(idioma):
        pat = re.compile(r'<strong>(' + re.escape(esc(nombre)) + r')( \(S/ [\d.]+\))', re.I)
        cuerpo = pat.sub(lambda m: f'<strong><a href="{url}">{m.group(1)}</a>{m.group(2)}', cuerpo)
    return h[:i] + cuerpo + h[j:]


def generar(ficha: dict) -> str:
    cab = PARTES['A_cabecera']
    if ficha.get('idioma') == 'en':
        cab = cab.replace('<html lang="es"', '<html lang="en"', 1)
    return (cab + meta(ficha) + PARTES['B_recursos'] +
            datos(ficha) + PARTES['C_chrome'] + enlazar_productos(articulo(ficha), ficha.get('idioma', 'es')) + PARTES['D_pie'])


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
