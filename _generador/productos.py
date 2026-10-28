#!/usr/bin/env python3
"""Una página por producto de la carta: /producto/<producto> y el índice /productos.

OJO: NO usar la carpeta carta/: con carta.html y carta/ juntos, /carta deja de abrir la carta.

Por qué existe: quien busca «pie de limón San Isidro» o «pan con chicharrón cerca
de Javier Prado» busca UN producto. Cada página tiene datos reales y propios:
foto, precio y descripción de la carta del POS, en qué combos viene, los demás
de su categoría y dónde pedirlo. Solo se crean páginas de productos con foto
(sin foto la página quedaría vacía de verdad).

Fuente: los bloques {"id":...,"items":[...]} de carta.html, que refresca
`node actualizar-carta.mjs` desde el POS. Tras cambiar precios en el POS:
  node actualizar-carta.mjs && python3 _generador/productos.py && python3 _generador/registrar.py

«Lo más pedido»: si existe el archivo de ventas indicado en VENTAS_JSON
({nombre: unidades en 60 días}), los 3 primeros de cada categoría lo dicen.
Ese archivo NO va al repositorio (el repo es público): vive fuera.

Uso:  VENTAS_JSON=/ruta/ventas60.json python3 productos.py
"""
import html, json, os, pathlib, re, sys, unicodedata
import datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import generar  # partes fijas, guías y ficha del negocio idénticas a las del blog

SITIO = generar.SITIO
DESTINO = SITIO / 'producto'
BASE = generar.BASE
HOY = datetime.date.today().isoformat()
MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
OCULTAS = {'Capacitación', 'Extras'}
COMBOS = {'Desayunos', 'Dulce Pausa', 'Combo Bebida + Postre', 'Promociones'}
# Guía del blog que corresponde a cada categoría (enlace de contexto).
GUIA = {
    'Desayunos': ('desayunos-en-san-isidro-carta-precios-horario', 'desayunos en San Isidro'),
    'Cafés': ('cafe-de-especialidad-san-isidro-guia', 'café de especialidad en San Isidro'),
    'Infusiones': ('infusiones-te-y-chocolate-caliente-san-isidro', 'infusiones, té y chocolate caliente'),
    'Frappés': ('frappes-y-cafe-helado-en-san-isidro', 'frappés y café helado'),
    'Bebidas Frías': ('jugos-y-batidos-en-san-isidro-precios', 'jugos, batidos y bebidas frías'),
    'Frozen': ('jugos-y-batidos-en-san-isidro-precios', 'jugos, batidos y frozen'),
    'Jugos': ('jugos-y-batidos-en-san-isidro-precios', 'jugos y batidos en San Isidro'),
    'Batidos': ('jugos-y-batidos-en-san-isidro-precios', 'jugos y batidos en San Isidro'),
    'Sándwiches': ('sandwiches-peruanos-y-hamburguesas-san-isidro', 'sándwiches y hamburguesas en San Isidro'),
    'Omelettes': ('omelettes-y-huevos-en-san-isidro', 'omelettes y huevos en San Isidro'),
    'Salchipapas': ('almuerzo-en-san-isidro-combos-y-precios', 'almuerzo en San Isidro'),
    'Promociones': ('almuerzo-en-san-isidro-combos-y-precios', 'almuerzo en San Isidro'),
    'Dulce Pausa': ('postres-artesanales-cafeteria-san-isidro', 'postres en San Isidro'),
    'Postres': ('postres-artesanales-cafeteria-san-isidro', 'postres en San Isidro'),
    'Guarniciones': ('sandwiches-peruanos-y-hamburguesas-san-isidro', 'sándwiches y acompañamientos'),
    'Ensaladas': ('almuerzo-en-san-isidro-combos-y-precios', 'almuerzo en San Isidro'),
    'Tamales': ('desayuno-criollo-pan-con-chicharron-y-tamal-san-isidro', 'desayuno criollo en San Isidro'),
    'Helados': ('postres-artesanales-cafeteria-san-isidro', 'postres y helados en San Isidro'),
    'Cócteles': ('pisco-sour-y-after-office-en-san-isidro', 'pisco sour y after office'),
    'Empanadas': ('pisco-sour-y-after-office-en-san-isidro', 'algo para picar en San Isidro'),
    'Combo Bebida + Postre': ('postres-artesanales-cafeteria-san-isidro', 'postres en San Isidro'),
}


def norm(t: str) -> str:
    t = unicodedata.normalize('NFD', t.lower())
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


def slug_de(nombre: str, cat: str) -> str:
    s = re.sub(r'[^a-z0-9]+', '-', norm(nombre)).strip('-')
    if s[:1].isdigit():                       # «1 Bola» → helado-1-bola
        s = re.sub(r'[^a-z0-9]+', '-', norm(cat)).strip('-').rstrip('s') + '-' + s
    return s


def precio(p: float) -> str:
    return f'S/ {p:.2f}'


def leer_carta() -> list:
    cats = []
    for linea in (SITIO / 'carta.html').read_text(encoding='utf-8').split('\n'):
        s = linea.strip()
        if s.startswith('{"id":"') and '"items":[' in s:
            cats.append(json.loads(s.rstrip(',')))
    prods = []
    for c in cats:
        cat = c['es']['n']
        if cat in OCULTAS:
            continue
        for it in c['items']:
            prods.append({'cat': cat, 'n': it['es']['n'], 'd': (it['es'].get('d') or '').strip(),
                          'p': float(it['p']), 'img': it.get('img', ''),
                          'en': it.get('en', {}).get('n', ''), 'en_d': it.get('en', {}).get('d', '')})
    for x in prods:
        x['slug'] = slug_de(x['n'], x['cat'])
    return prods


def frase_desc(d: str) -> str:
    d = d.strip().rstrip('.')
    return d[0].upper() + d[1:] + '.' if d else ''


def pagina(x: dict, prods: list, con_pagina: set, top: set) -> str:
    cat, nombre = x['cat'], x['n']
    url = f'{BASE}/producto/{x["slug"]}'
    img = '/' + x['img'].split('wasicafe.com/')[1]
    pv = precio(x['p'])
    titulo = f'{nombre}: {pv} en San Isidro | Wasi Café'
    if len(titulo) > 65:
        titulo = f'{nombre} | Wasi Café, San Isidro'
    if len(titulo) > 65:
        titulo = f'{nombre[:50].rstrip()} | Wasi Café'
    desc = (f'{nombre} en Wasi Café, San Isidro: {pv}. ' + (frase_desc(x["d"]) + ' ' if x['d'] else '')
            + 'En la mesa por QR o para llevar, a pasos de Javier Prado.')
    if len(desc) > 165:
        desc = f'{nombre} en Wasi Café, San Isidro: {pv}. En la mesa por QR o para llevar, a pasos de Javier Prado.'
    e = generar.esc
    T = generar.TXT['es']

    # combos donde aparece (por nombre o descripción del combo)
    n_norm = norm(nombre)
    combos = [c for c in prods if c['cat'] in COMBOS and c['n'] != nombre and len(n_norm) >= 4
              and (re.search(r'\b' + re.escape(n_norm) + r'\b', norm(c['n'])) or re.search(r'\b' + re.escape(n_norm) + r'\b', norm(c['d'])))]
    hermanos = [h for h in prods if h['cat'] == cat and h['n'] != nombre]

    def enlace(h):
        t = f'{e(h["n"])} ({precio(h["p"])})'
        return f'<a href="/producto/{h["slug"]}">{t}</a>' if h['slug'] in con_pagina else t

    cuerpo = [f'<figure style="margin:0 auto 1.4rem;max-width:429px"><img src="{e(img)}" alt="{e(nombre)} en Wasi Café, San Isidro" '
              f'width="429" height="333" decoding="async" style="width:100%;height:auto;aspect-ratio:429/333;object-fit:cover;border-radius:14px;display:block"></figure>',
              f'<p style="font-family:var(--display);font-size:2rem;color:var(--ink);margin:0 0 .6rem">{pv}</p>']
    p1 = (frase_desc(x['d']) + ' ' if x['d'] else '') + f'Es parte de la carta de <strong>{e(cat)}</strong> de Wasi Café, en San Isidro.'
    if nombre in top:
        p1 += f' Es uno de los más pedidos de {e(cat.lower())} por nuestros clientes.'
    cuerpo.append(f'<p>{p1}</p>')
    if combos:
        cuerpo.append('<h2>También viene en estos combos</h2><ul>' + ''.join(
            f'<li>{enlace(c)}' + (f': {e(c["d"][0].lower() + c["d"][1:])}' if c['d'] else '') + '</li>' for c in combos[:8]) + '</ul>')
    if hermanos:
        cuerpo.append(f'<h2>Más {e(cat.lower())} en la carta</h2><ul>' + ''.join(
            f'<li>{enlace(h)}</li>' for h in hermanos[:10]) + '</ul>')
    g = GUIA.get(cat)
    cuerpo.append('<h2>Dónde pedirlo</h2>'
                  '<p>En <strong>Wasi Café</strong>, Luis Felipe Villarán 904, San Isidro, a pasos de la avenida Javier Prado. '
                  'Atendemos de lunes a viernes de 8:00 a. m. a 9:00 p. m. y los sábados de 9:00 a. m. a 9:00 p. m.; los domingos está cerrado. '
                  'En el local se pide desde la mesa escaneando el código QR, y todo se puede pedir para llevar. '
                  'Aceptamos efectivo, tarjeta, Yape y Plin.</p>'
                  f'<p><a href="{MAPA}" target="_blank" rel="noopener">Ver en Google Maps</a> · <a href="/carta">Carta completa con precios</a>'
                  + (f' · Guía: <a href="/blog/{g[0]}">{e(g[1])}</a>' if g else '') + '</p>'
                  '<p style="font-size:.86rem;color:var(--ink-soft)">Precio de la carta al ' + generar.fecha_legible(HOY) + '. '
                  'La carta en línea se actualiza sola desde la caja.</p>')

    faq = [(f'¿Cuánto cuesta {nombre} en Wasi Café?', f'{pv} en la carta de Wasi Café, en San Isidro.'),
           (f'¿Se puede pedir {nombre} para llevar?', 'Sí, todo lo de la carta se puede pedir para llevar.'),
           ('¿Dónde queda Wasi Café?', 'En Luis Felipe Villarán 904, San Isidro, Lima, a pasos de la avenida Javier Prado.')]

    ld_item = {"@context": "https://schema.org", "@type": "MenuItem", "name": nombre, "description": x['d'] or f'{nombre} de la carta de Wasi Café',
               "image": BASE + img, "url": url, "menuAddOn": [],
               "offers": {"@type": "Offer", "price": f'{x["p"]:.2f}', "priceCurrency": "PEN", "availability": "https://schema.org/InStock"}}
    ld_item.pop('menuAddOn')
    ld_migas = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + '/'},
        {"@type": "ListItem", "position": 2, "name": "Productos", "item": BASE + '/productos'},
        {"@type": "ListItem", "position": 3, "name": nombre, "item": url}]}
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in faq]}
    negocio = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                         generar.datos({'slug': x['slug'], 'descripcion': desc, 'h1': nombre, 'tituloCorto': nombre, 'fecha': HOY,
                                        'secciones': [], 'intro': ''}), re.S)[-1]
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>\n' for b in (ld_item, ld_migas, ld_faq))
    ld += f'<script type="application/ld+json">{negocio}</script>\n'

    meta = (f'<title>{e(titulo)}</title>\n<meta name="theme-color" content="#F7F1E8">\n'
            f'<meta name="description" content="{e(desc)}">\n'
            f'<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">\n'
            f'<link rel="canonical" href="{url}">\n<link rel="icon" href="/favicon-32x32.png" sizes="32x32">\n'
            f'<meta property="og:type" content="product">\n<meta property="og:title" content="{e(nombre)} · {pv} · Wasi Café">\n'
            f'<meta property="og:description" content="{e(desc)}">\n<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{BASE}{e(img)}">\n<meta property="og:site_name" content="Wasi Café">\n'
            f'<meta property="og:locale" content="es_PE">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{e(nombre)} · {pv} · Wasi Café">\n<meta name="twitter:description" content="{e(desc)}">\n'
            f'<meta name="twitter:image" content="{BASE}{e(img)}">\n')

    art = [f'<div class="crumbs"><a href="/">Inicio</a><span>›</span><a href="/productos">Productos</a><span>›</span>{e(nombre)}</div></div>',
           '', '<article>',
           f'<div class="read ahero"><p class="eyebrow">{e(cat)}</p><h1>{e(nombre)}</h1>'
           f'<p class="ameta">Carta de Wasi Café · San Isidro, Lima</p></div>',
           '<div class="read prose">', '\n'.join(cuerpo), '</div>',
           f'<section class="faq read"><h2>{T["faq"]}</h2>' + ''.join(
               f'<details><summary>{e(q)}</summary><p>{e(r)}</p></details>' for q, r in faq) + '</section>',
           generar.guias('__producto__'),
           f'  <div class="read"><div class="cta"><h3>{T["cta_t"]}</h3><p>{T["cta_p"]}</p>'
           f'<a class="btn" href="https://wa.me/51908724496?text={T["cta_w"]}" target="_blank" rel="noopener">{T["cta_b"]}</a></div>',
           '  <a class="back" href="/productos">← Todos los productos</a></div>', '</article>']
    return (generar.PARTES['A_cabecera'] + meta + generar.PARTES['B_recursos'] + ld +
            generar.PARTES['C_chrome'] + '\n'.join(art) + generar.PARTES['D_pie'])


def indice(prods: list, con_pagina: set) -> str:
    e = generar.esc
    url = f'{BASE}/productos'
    desc = 'Todos los productos de la carta de Wasi Café en San Isidro, con foto y precio: cafés, desayunos, sándwiches, postres, jugos y más.'
    por_cat = {}
    for x in prods:
        por_cat.setdefault(x['cat'], []).append(x)
    bloques = []
    for cat, xs in por_cat.items():
        items = ''.join(
            (f'<li><a href="/producto/{x["slug"]}">{e(x["n"])}</a> · {precio(x["p"])}</li>' if x['slug'] in con_pagina
             else f'<li>{e(x["n"])} · {precio(x["p"])}</li>') for x in xs)
        bloques.append(f'<h2>{e(cat)}</h2><ul>{items}</ul>')
    ld_lista = {"@context": "https://schema.org", "@type": "ItemList", "name": "Productos de Wasi Café",
                "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{BASE}/producto/{x["slug"]}', "name": x['n']}
                                    for i, x in enumerate([p for p in prods if p['slug'] in con_pagina])]}
    meta = (f'<title>Productos y precios de Wasi Café | San Isidro, Lima</title>\n<meta name="theme-color" content="#F7F1E8">\n'
            f'<meta name="description" content="{e(desc)}">\n<meta name="robots" content="index, follow">\n'
            f'<link rel="canonical" href="{url}">\n<link rel="icon" href="/favicon-32x32.png" sizes="32x32">\n'
            f'<meta property="og:title" content="Productos y precios de Wasi Café">\n<meta property="og:description" content="{e(desc)}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{BASE}/og-image.png">\n<meta property="og:locale" content="es_PE">\n')
    art = ['<div class="crumbs"><a href="/">Inicio</a><span>›</span>Productos</div></div>', '', '<article>',
           '<div class="read ahero"><p class="eyebrow">carta de Wasi Café</p><h1>Todos los productos, con foto y precio</h1>'
           '<p class="ameta">Wasi Café · San Isidro, Lima</p></div>',
           '<div class="read prose"><p>Cada producto con foto tiene su página: precio, descripción, en qué combos viene y dónde pedirlo. '
           'La <a href="/carta">carta en línea</a> se actualiza sola desde la caja.</p>' + ''.join(bloques) + '</div>',
           generar.guias('__producto__'), '</article>']
    return (generar.PARTES['A_cabecera'] + meta + generar.PARTES['B_recursos'] +
            f'<script type="application/ld+json">{json.dumps(ld_lista, ensure_ascii=False)}</script>\n' +
            generar.PARTES['C_chrome'] + '\n'.join(art) + generar.PARTES['D_pie'])


def revisar(h: str) -> list:
    fallos = []
    for etq in ('html', 'head', 'body', 'article', 'div', 'ul', 'nav', 'section'):
        a, c = len(re.findall(rf'<{etq}[\s>]', h)), h.count(f'</{etq}>')
        if a != c:
            fallos.append(f'{etq}: {a} vs {c}')
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            json.loads(b)
        except Exception as ex:
            fallos.append(f'JSON-LD: {ex}')
    if '—' in re.sub(r'<script.*?</script>', '', h, flags=re.S):
        fallos.append('guion largo')
    return fallos


def main() -> None:
    prods = leer_carta()
    slugs = [x['slug'] for x in prods]
    dup = {s for s in slugs if slugs.count(s) > 1}
    if dup:
        raise SystemExit(f'slugs repetidos: {dup}')
    con_pagina = {x['slug'] for x in prods if x['img']}
    top = set()
    ruta = os.environ.get('VENTAS_JSON')
    if ruta and pathlib.Path(ruta).exists():
        ventas = json.loads(pathlib.Path(ruta).read_text(encoding='utf-8'))
        for cat in {x['cat'] for x in prods}:
            orden = sorted((x for x in prods if x['cat'] == cat and ventas.get(x['n'], 0) >= 10),
                           key=lambda x: -ventas.get(x['n'], 0))
            top |= {x['n'] for x in orden[:3]}
    DESTINO.mkdir(exist_ok=True)
    vigentes = set()
    malos = 0
    for x in prods:
        if x['slug'] not in con_pagina:
            continue
        h = pagina(x, prods, con_pagina, top)
        f = revisar(h)
        if f:
            malos += 1
            print('  ✗', x['slug'], f)
            continue
        (DESTINO / f'{x["slug"]}.html').write_text(h, encoding='utf-8')
        vigentes.add(f'{x["slug"]}.html')
    # páginas de productos que ya no están en la carta: se borran (el sitemap las suelta)
    for viejo in DESTINO.glob('*.html'):
        if viejo.name not in vigentes:
            viejo.unlink()
            print('  − retirado', viejo.name)
    h = indice(prods, con_pagina)
    if revisar(h):
        raise SystemExit(f'índice con fallos: {revisar(h)}')
    (SITIO / 'productos.html').write_text(h, encoding='utf-8')
    print(f'  {len(vigentes)} páginas de producto en producto/ ({malos} con fallos) + productos.html; «más pedidos»: {len(top)}')


if __name__ == '__main__':
    main()
