"""Cuarta ola (28/10/2026): omelettes y huevos (nueva) y café cerca de Javier Prado
(reescrita con datos reales). Mismas reglas: carta del POS, portada y ventas reales.
Uso: python3 fichas_ola4.py  → escribe ola4.json
"""
import json, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-28'
MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
HORARIO = ('de lunes a viernes de <strong>8:00 a. m. a 9:00 p. m.</strong> y los sábados de '
           '<strong>9:00 a. m. a 9:00 p. m.</strong>; los domingos estamos cerrados')
ORIGEN = 'Cusco, Cajamarca, Junín, Amazonas y San Martín'


def foto(nombre, pie=None):
    x = CARTA[nombre]
    if not x.get('img'):
        raise SystemExit(f'sin foto: {nombre}')
    return {'src': '/' + x['img'].split('wasicafe.com/')[1], 'alt': f"{nombre} en Wasi Café, San Isidro",
            'pie': pie or f"{nombre} · S/ {x['p']:.2f}"}


def s(n):
    return f"S/ {CARTA[n]['p']:.2f}"


def li(n, texto=None):
    d = CARTA[n].get('d', '') if texto is None else texto
    return f"<li><strong>{n} ({s(n)})</strong>{': ' + d[0].lower() + d[1:] + '.' if d else '.'}</li>"


def lista(*nombres):
    return '<ul>' + ''.join(li(n) for n in nombres) + '</ul>'


fichas = []

fichas.append({
    "slug": "omelettes-y-huevos-en-san-isidro",
    "tituloSeo": "Omelettes y huevos en San Isidro: carta y precios | Wasi Café",
    "h1": "Omelettes y huevos para desayunar en San Isidro: la carta de Wasi Café con precios",
    "tituloCorto": "Omelettes en San Isidro",
    "ogTitulo": "Omelettes y huevos en San Isidro, con precios",
    "descripcion": "Omelettes en San Isidro desde S/ 18.50: de queso, jamón, pollo, tocino y completo, más huevos revueltos, con jamón o sancochados en Wasi Café.",
    "eyebrow": "omelettes en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Omelette", "Desayuno", "San Isidro"],
    "intro": (
        "<p>Para muchos, desayunar bien es sinónimo de huevos. En <strong>Wasi Café</strong>, en San Isidro, hay siete omelettes preparados al momento "
        "y varias formas de pedir huevos sueltos, para armar el desayuno a tu medida. Aquí está todo, con precios reales.</p>"
        "<p>Los precios son los de nuestra <a href=\"/carta\">carta en línea</a>, que se actualiza sola desde la caja.</p>"),
    "secciones": [
        {"h2": "Los siete omelettes", "html": (
            lista('Omelette de Queso', 'Omelette de Jamón', 'Omelette de Tocino', 'Omelette de Pollo', 'Omelette Jamón y Queso',
                  'Omelette Tocino y Queso', 'Omelette Completo')
            + "<p>El <strong>Omelette Completo</strong> es el más cargado: jamón, queso, tocino, tomate y pimiento. Si quieres algo simple, "
            "el de queso o el de jamón son los más ligeros.</p>"),
         "fotos": [foto('Omelette Completo'), foto('Omelette Jamón y Queso'), foto('Omelette de Pollo'), foto('Omelette de Queso')]},
        {"h2": "Huevos a tu manera", "html": (
            lista('Huevos Revueltos', 'Huevos con Jamón', 'Huevos con Tocino', 'Huevos Jamón y Queso', 'Huevos Sancochados')
            + f"<p>Y si solo quieres sumar uno a lo que ya pediste, un huevo suelto cuesta {s('Huevo')}.</p>"),
         "fotos": [foto('Huevos Revueltos'), foto('Huevos con Jamón'), foto('Huevos con Tocino'), foto('Huevos Sancochados')]},
        {"h2": "Para acompañar", "html": (
            lista('Tostadas', 'Croissant', 'Pan al Ajo')
            + "<p>Un omelette con tostadas y un jugo natural es un desayuno completo. Si prefieres que todo venga junto a precio cerrado, "
            "mira los combos de abajo.</p>"),
         "fotos": [foto('Tostadas'), foto('Croissant')]},
        {"h2": "Combos de desayuno con huevos", "html": (
            "<p>Tres combos de la carta ya incluyen huevos y café:</p><ul>"
            f"<li><strong>Desayuno Americano ({s('Desayuno Americano')})</strong>: café, jugo de papaya o piña, huevos revueltos o fritos, tostadas, mermelada y mantequilla.</li>"
            f"<li><strong>Light ({s('Light')})</strong>: café, huevos duros, revueltos o fritos, porción de palta y tostadas.</li>"
            f"<li><strong>Trío Completo ({s('Trío Completo')})</strong>: café, jugo y mixto completo de jamón, queso y huevo.</li></ul>"
            "<p>El Light y el Desayuno Americano están entre los desayunos más pedidos por nuestros clientes. Todos los combos están en la guía de "
            "<a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>")},
        {"h2": "Cómo elegir", "html": (
            "<ul><li><strong>Si tienes poco tiempo:</strong> huevos revueltos con tostadas, que salen más rápido que un omelette relleno.</li>"
            "<li><strong>Si quieres proteína sin tanto embutido:</strong> el omelette de pollo o los huevos sancochados.</li>"
            "<li><strong>Si es desayuno largo de sábado:</strong> el Omelette Completo con un jugo natural y un café.</li>"
            "<li><strong>Si cuidas lo que comes:</strong> el combo Light, con huevos, palta y tostadas.</li></ul>")},
        {"h2": "El café del desayuno", "html": (
            f"<p>Con los huevos, lo clásico es un <strong>americano ({s('Americano')})</strong> o un <strong>café con leche ({s('Café con Leche')})</strong>. "
            f"Nuestro café es de especialidad, 100 % peruano, de {ORIGEN}. Si prefieres algo frío, un <strong>jugo de naranja ({s('Jugo de Naranja')})</strong> "
            "exprimido al momento.</p>")},
        {"h2": "Horario y dónde estamos", "html": (
            f"<p>El desayuno no tiene hora de corte: puedes pedir un omelette a cualquier hora mientras estemos abiertos, {HORARIO}. "
            "Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>. Todo se puede pedir para llevar.</p>")},
    ],
    "faq": [
        {"p": "¿Cuánto cuesta un omelette en Wasi Café?", "r": f"Desde {s('Omelette de Queso')} el de queso o jamón; el Omelette Completo cuesta {s('Omelette Completo')}."},
        {"p": "¿Hasta qué hora sirven desayuno?", "r": "El desayuno se sirve todo el día mientras el local está abierto, de 8:00 a. m. a 9:00 p. m. de lunes a viernes y desde las 9:00 a. m. los sábados."},
        {"p": "¿Hay combos con huevos y café?", "r": "Sí: Desayuno Americano, Light y Trío Completo, todos con café incluido."},
    ],
    "relacionados": ["desayunos-en-san-isidro-carta-precios-horario", "desayuno-criollo-pan-con-chicharron-y-tamal-san-isidro", "desayuno-saludable-ideas-cafeteria-san-isidro"],
})

fichas.append({
    "slug": "cafe-cerca-de-javier-prado-san-isidro",
    "tituloSeo": "Café cerca de Javier Prado, San Isidro | Wasi Café",
    "h1": "Café cerca de la avenida Javier Prado: Wasi Café, para llevar o para quedarse",
    "tituloCorto": "Café cerca de Javier Prado",
    "ogTitulo": "Café de especialidad a pasos de Javier Prado",
    "descripcion": "Café de especialidad a pasos de Javier Prado, en San Isidro: abierto de corrido de 8 a. m. a 9 p. m., para llevar desde S/ 8, desayunos y combos de almuerzo.",
    "eyebrow": "café cerca de Javier Prado",
    "fecha": "2026-06-15", "modificado": HOY,
    "about": ["Café de especialidad", "Javier Prado", "San Isidro"],
    "intro": (
        "<p>Si trabajas o haces trámites por la <strong>avenida Javier Prado</strong>, en San Isidro, y necesitas un buen café sin desviarte mucho, "
        "<strong>Wasi Café</strong> está en Luis Felipe Villarán 904, a pasos de la avenida. Abrimos de corrido, sin cerrar al mediodía, "
        "y todo se puede pedir para llevar. Esto es lo que encontrarás, con precios reales.</p>"),
    "secciones": [
        {"h2": "Café para llevar, con precio", "html": (
            f"<p>Todo nuestro café es de especialidad, 100 % peruano, de {ORIGEN}. Los más rápidos para llevar:</p>"
            + lista('Café Filtrado', 'Americano', 'Espresso', 'Cortado', 'Café con Leche', 'Capuchino')
            + "<p>El <strong>americano</strong> es el café que más servimos. Para los días de calor, hay "
            f"<strong>café helado ({s('Café Helado')})</strong> y frappés: mira la guía de <a href=\"/blog/frappes-y-cafe-helado-en-san-isidro\">frappés y café helado</a>.</p>"),
         "fotos": [foto('Americano'), foto('Capuchino'), foto('Café Filtrado'), foto('Café con Leche')]},
        {"h2": "Desayuno antes de la oficina", "html": (
            f"<p>Abrimos a las <strong>8:00 a. m.</strong> de lunes a viernes. Los combos más rápidos son el <strong>Dúo Café ({s('Dúo Café')})</strong>, "
            f"con café y un mixto, y el <strong>Continental ({s('Continental')})</strong>, con café, jugo y tostadas. Si hay más tiempo, el "
            f"<strong>Amanecer Criollo ({s('Amanecer Criollo')})</strong> trae americano y pan con chicharrón.</p>"
            "<p>Todas las opciones están en la guía de <a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>"),
         "fotos": [foto('Chicharrón'), foto('Croissant Mixto'), foto('Mixto Clásico')]},
        {"h2": "Almuerzo de 12 a 4", "html": (
            "<p>De lunes a sábado, de 12:00 p. m. a 4:00 p. m., hay combos con plato principal, papas andinas y bebida a elección: "
            f"el <strong>Combo Filete ({s('Combo Filete')})</strong>, el más pedido, y los de bistec, chuleta, milanesa, suprema y hamburguesa ({s('Combo Bistec')}). "
            "Detalle en la guía de <a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">almuerzo en San Isidro</a>.</p>"),
         "fotos": [foto('Filete de Pollo'), foto('Papas Andinas', 'Papas andinas, acompañamiento de los combos')]},
        {"h2": "Para una reunión corta", "html": (
            "<p>A pasos de las oficinas de la zona, Wasi funciona bien para una reunión de media hora: WiFi gratis, pedido desde la mesa con el código QR "
            "y factura electrónica si la necesitas. Aceptamos efectivo, tarjeta, Yape y Plin.</p>"
            "<p>Según nuestras ventas, las horas de más movimiento son de 1:00 a 2:00 p. m. y de 5:00 a 8:00 p. m.; para conversar tranquilo, "
            "mejor la mañana. Más ideas en <a href=\"/blog/reuniones-de-trabajo-en-cafeteria-san-isidro\">reuniones de trabajo en San Isidro</a>.</p>")},
        {"h2": "Algo dulce para la tarde", "html": (
            f"<p>Para el bajón de media tarde: un <strong>alfajor ({s('Alfajor')})</strong>, lo que más sale de la vitrina, o un combo de postre y café, como el "
            f"<strong>Pie de limón + Café Americano ({s('Pie de limón + Café Americano')})</strong>. La carta dulce está en "
            "<a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres en San Isidro</a>.</p>"),
         "fotos": [foto('Alfajor'), foto('Pie de limón + Café Americano')]},
        {"h2": "Cómo llegar", "html": (
            f"<p>Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado. Atendemos {HORARIO}. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Abre la ubicación en Google Maps</a> para ver la ruta desde donde estés. "
            "Más detalles en la guía de <a href=\"/blog/cafeteria-en-san-isidro-horario-como-llegar\">horario y cómo llegar</a>.</p>")},
    ],
    "faq": [
        {"p": "¿Hay una cafetería cerca de la avenida Javier Prado en San Isidro?", "r": "Sí, Wasi Café está en Luis Felipe Villarán 904, a pasos de la avenida Javier Prado."},
        {"p": "¿Cuánto cuesta un café para llevar?", "r": f"Desde {s('Café Filtrado')} el café filtrado; el americano cuesta {s('Americano')} y el capuchino {s('Capuchino')}."},
        {"p": "¿A qué hora abre?", "r": "A las 8:00 a. m. de lunes a viernes y a las 9:00 a. m. los sábados; cierra a las 9:00 p. m. Los domingos está cerrado."},
    ],
    "relacionados": ["cafe-cerca-del-centro-empresarial-san-isidro", "reuniones-de-trabajo-en-cafeteria-san-isidro", "cafeterias-para-trabajar-laptop-san-isidro"],
})

json.dump(fichas, open(AQUI / 'ola4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(fichas), 'fichas | guiones largos:', json.dumps(fichas, ensure_ascii=False).count('—'))
