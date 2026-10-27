"""Fichas de los artículos pilares del blog de Wasi Café (26/10/2026).

Todo dato sale de la carta del POS (precios), de la portada (horario,
dirección, servicios) o de las ventas (domingo cerrado). Nada inventado.
Las fotos son las reales de la carta, buscadas por el NOMBRE del producto:
si un nombre no existe, el script falla en vez de poner una foto equivocada.
"""
import json, sys, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-26'


def foto(nombre, pie=None):
    x = CARTA[nombre]
    if not x.get('img'):
        raise SystemExit(f'sin foto: {nombre}')
    precio = f"S/ {x['p']:.2f}".replace('.00', '')
    return {'src': '/' + x['img'].split('wasicafe.com/')[1], 'alt': f"{nombre} en Wasi Café, San Isidro",
            'pie': pie or f"{nombre} · {precio}"}


def s(n):
    """Precio con formato peruano: S/ 19.90."""
    return f"S/ {CARTA[n]['p']:.2f}"


HORARIO = ('<table style="width:100%;border-collapse:collapse;margin:1rem 0 1.4rem">'
           '<tr><td style="padding:.5rem 0;border-bottom:1px solid var(--line)">Lunes a viernes</td>'
           '<td style="padding:.5rem 0;border-bottom:1px solid var(--line);text-align:right"><strong>8:00 a. m. a 9:00 p. m.</strong></td></tr>'
           '<tr><td style="padding:.5rem 0;border-bottom:1px solid var(--line)">Sábado</td>'
           '<td style="padding:.5rem 0;border-bottom:1px solid var(--line);text-align:right"><strong>9:00 a. m. a 9:00 p. m.</strong></td></tr>'
           '<tr><td style="padding:.5rem 0">Domingo</td><td style="padding:.5rem 0;text-align:right">Cerrado</td></tr></table>')

MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'

fichas = []

# ---------------------------------------------------------------- 1. Desayunos
fichas.append({
    "slug": "desayunos-en-san-isidro-carta-precios-horario",
    "tituloSeo": "Desayunos en San Isidro: carta, precios y horario | Wasi Café",
    "h1": "Desayunos en San Isidro: qué pedir en Wasi Café, con precios y horario",
    "tituloCorto": "Desayunos en San Isidro",
    "ogTitulo": "Desayunar en San Isidro: la carta de Wasi Café con precios",
    "descripcion": "Desayunos en San Isidro con precios reales: combos desde S/ 19.90, omelettes, tamal y café de especialidad. Horario, dirección y qué pedir en Wasi Café.",
    "eyebrow": "desayunos en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Desayuno", "San Isidro", "Café de especialidad"],
    "intro": (
        "<p>Si buscas <strong>dónde desayunar en San Isidro</strong>, lo primero que importa es simple: que abran temprano, "
        "que el café sea bueno y que sepas cuánto vas a pagar antes de sentarte. Esta guía responde las tres cosas con la carta real de "
        "<strong>Wasi Café</strong>, en Luis Felipe Villarán 904, a pasos de la avenida Javier Prado.</p>"
        "<p>Los precios de esta página son los mismos que ves en nuestra <a href=\"/carta\">carta</a>. Si alguno cambia, la carta en línea "
        "se actualiza sola desde la caja, así que ahí siempre está el dato al día.</p>"),
    "secciones": [
        {"h2": "A qué hora se puede desayunar", "html": (
            "<p>Abrimos de lunes a viernes a las <strong>8:00 a. m.</strong>, una buena hora para quien trabaja en la zona financiera "
            "y quiere desayunar antes de entrar a la oficina. Los sábados abrimos a las 9:00 a. m., con más calma. "
            "<strong>Los domingos estamos cerrados</strong>, así que si planeas un desayuno largo de fin de semana, el sábado es tu día.</p>"
            + HORARIO +
            "<p>El desayuno no tiene hora de corte: puedes pedir un combo de desayuno a media mañana o un omelette a la hora que quieras "
            "mientras estemos abiertos.</p>")},
        {"h2": "Los combos de desayuno, con precio", "html": (
            "<p>Los combos son la forma más sencilla de desayunar completo sin pensar mucho. Todos incluyen café americano o café con leche, "
            "y varios suman un jugo de papaya o piña:</p><ul>"
            f"<li><strong>Continental ({s('Continental')}):</strong> café, jugo, tostadas de pan de molde blanco o integral, mermelada y mantequilla.</li>"
            f"<li><strong>Dúo Café ({s('Dúo Café')}):</strong> café y un mixto clásico de jamón y queso. El más rápido.</li>"
            f"<li><strong>Desayuno Tamalero ({s('Desayuno Tamalero')}):</strong> café, tamal, pan francés y salsa criolla.</li>"
            f"<li><strong>Desayuno Americano ({s('Desayuno Americano')}):</strong> café, jugo, huevos revueltos o fritos, tostadas, mermelada y mantequilla.</li>"
            f"<li><strong>Light ({s('Light')}):</strong> café, huevos (duros, revueltos o fritos), porción de palta y tostadas. Para quien cuida lo que come.</li>"
            f"<li><strong>Pollo Wasi ({s('Pollo Wasi')}):</strong> café, jugo y sándwich de pollo.</li>"
            f"<li><strong>Trío Completo ({s('Trío Completo')}):</strong> café, jugo y mixto completo de jamón, queso y huevo.</li>"
            f"<li><strong>Amanecer Criollo ({s('Amanecer Criollo')}):</strong> café americano y sándwich de chicharrón. El desayuno limeño de siempre.</li>"
            f"<li><strong>Tradición Wasi ({s('Tradición Wasi')}):</strong> para compartir entre dos, con dos cafés, dos jugos, 250 g de chicharrón y tamal de pollo.</li>"
            "</ul><p>Los más pedidos por nuestros clientes son el <strong>Light</strong> y el <strong>Desayuno Americano</strong>.</p>")},
        {"h2": "Si prefieres armar tu propio desayuno", "html": (
            "<p>No a todos les va un combo. Los omelettes se preparan al momento con huevos frescos, y se pueden acompañar con lo que quieras de la carta:</p><ul>"
            f"<li><strong>Omelette Completo ({s('Omelette Completo')}):</strong> jamón, queso, tocino, tomate y pimiento.</li>"
            f"<li><strong>Omelette de Queso ({s('Omelette de Queso')})</strong> u <strong>Omelette de Jamón ({s('Omelette de Jamón')})</strong>, para algo más simple.</li>"
            f"<li><strong>Tamal Criollo ({s('Tamal Criollo')}):</strong> con salsa criolla en pan francés.</li>"
            f"<li><strong>Huevos revueltos ({s('Huevos Revueltos')})</strong>, <strong>tostadas ({s('Tostadas')})</strong> o un <strong>croissant ({s('Croissant')})</strong> como acompañamiento.</li>"
            "</ul>"),
         "fotos": [foto('Omelette Completo'), foto('Tamal Criollo'), foto('Huevos Revueltos'), foto('Croissant Huevos y Jamón')]},
        {"h2": "El café y los jugos del desayuno", "html": (
            "<p>Trabajamos con <strong>granos 100 % peruanos de origen</strong>, de regiones como Cusco, Cajamarca, Junín, Amazonas y San Martín, preparados por baristas. "
            f"Lo que más se pide en Wasi es el <strong>Americano ({s('Americano')})</strong> y, después, el <strong>Capuchino ({s('Capuchino')})</strong>; "
            f"el <strong>Café con Leche ({s('Café con Leche')})</strong> también es un clásico del desayuno. Si te gusta el café suave, el <strong>Café Filtrado ({s('Café Filtrado')})</strong> es el más económico de la carta.</p>"
            f"<p>Los jugos se exprimen al momento: papaya o piña desde {s('Jugo de Papaya')}, naranja, mango o fresa a {s('Jugo de Naranja')}, "
            f"y el <strong>Jugo Especial ({s('Jugo Especial')})</strong> si quieres algo más completo.</p>"),
         "fotos": [foto('Americano'), foto('Capuchino'), foto('Jugo de Naranja'), foto('Jugo de Papaya')]},
        {"h2": "Un desayuno rápido antes de la oficina", "html": (
            "<p>Si tienes diez minutos, los combos de la sección <em>Dulce Pausa</em> juntan algo dulce con café a precio de combo: "
            f"<strong>Croissant + Café Americano ({s('Croissant + Café Americano')})</strong> o <strong>Empanada + Café Americano ({s('Empanada + Café Americano')})</strong>. "
            "Las empanadas se hornean al momento.</p>"
            "<p>Para pedir sin esperar, en las mesas hay un código QR: lo escaneas con el celular, eliges y tu pedido llega a la barra.</p>"),
         "fotos": [foto('Croissant + Café Americano'), foto('Empanada + Café Americano')]},
        {"h2": "Cómo llegar y qué saber antes de ir", "html": (
            f"<p>Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>.</p><ul>"
            "<li><strong>WiFi gratis</strong> y espacio para trabajar con laptop.</li>"
            "<li><strong>Ambiente pet friendly:</strong> puedes venir con tu perro.</li>"
            "<li><strong>Reservas:</strong> se piden desde la <a href=\"/#reservar\">web</a> y te confirmamos por WhatsApp.</li>"
            "<li><strong>Pagos:</strong> efectivo, tarjeta, Yape y Plin. Emitimos boleta o factura electrónica.</li>"
            "<li><strong>Tarjeta de sellos:</strong> acumulas sellos con tu celular y canjeas premios.</li></ul>")},
    ],
    "faq": [
        {"p": "¿A qué hora abre Wasi Café para desayunar?", "r": "De lunes a viernes a las 8:00 a. m. y los sábados a las 9:00 a. m. Cerramos a las 9:00 p. m. Los domingos no abrimos."},
        {"p": "¿Cuánto cuesta un desayuno en Wasi Café?", "r": f"Los combos de desayuno van de {s('Continental')} (Continental o Dúo Café) a {s('Amanecer Criollo')} (Amanecer Criollo). La Tradición Wasi, para dos personas, cuesta {s('Tradición Wasi')}."},
        {"p": "¿Hay desayunos ligeros?", "r": f"Sí. El combo Light ({s('Light')}) trae huevos, palta y tostadas, y hay omelettes desde {s('Omelette de Queso')}."},
        {"p": "¿Abren los domingos?", "r": "No. Atendemos de lunes a sábado; el sábado abrimos de 9:00 a. m. a 9:00 p. m."},
        {"p": "¿Se puede reservar mesa para desayunar?", "r": "Sí. Pides la reserva desde wasicafe.com y te la confirmamos por WhatsApp."},
    ],
    "relacionados": ["donde-desayunar-cerca-de-el-olivar-san-isidro", "desayuno-saludable-ideas-cafeteria-san-isidro", "brunch-en-san-isidro-que-pedir-como-elegir"],
})

# ------------------------------------------------------ 2. Café de especialidad
fichas.append({
    "slug": "cafe-de-especialidad-san-isidro-guia",
    "tituloSeo": "Café de especialidad en San Isidro: guía y carta | Wasi Café",
    "h1": "Café de especialidad en San Isidro: qué es, cómo reconocerlo y qué pedir",
    "tituloCorto": "Café de especialidad en San Isidro",
    "ogTitulo": "Café de especialidad en San Isidro: guía con la carta de Wasi",
    "descripcion": "Qué es el café de especialidad, cómo reconocer uno bueno y qué pedir en San Isidro: espresso, filtrado, capuchino y fríos con precios de Wasi Café.",
    "eyebrow": "café de especialidad",
    "fecha": "2026-06-13", "modificado": HOY,
    "about": ["Café de especialidad", "San Isidro", "Café peruano"],
    "intro": (
        "<p><strong>Café de especialidad</strong> es una etiqueta que se usa mucho y se explica poco. En esta guía te contamos qué significa de verdad, "
        "cómo distinguir una buena taza en cualquier cafetería y qué pedir según tu gusto, con la carta real de <strong>Wasi Café</strong> en San Isidro.</p>")
    ,
    "secciones": [
        {"h2": "Qué hace que un café sea de especialidad", "html": (
            "<p>El término nace de una idea sencilla: no todo el café es igual. Un café de especialidad es el que se cultiva, se cosecha y se procesa con tanto cuidado "
            "que conserva sabores propios de su origen, en vez de saber solo a «café tostado». En la práctica se reconoce por tres cosas:</p><ul>"
            "<li><strong>Origen claro:</strong> se sabe de qué región viene el grano.</li>"
            "<li><strong>Tueste medio:</strong> lo bastante para desarrollar dulzor, sin quemar los aromas.</li>"
            "<li><strong>Preparación cuidada:</strong> molienda al momento, dosis medida y agua a la temperatura correcta.</li></ul>"
            "<p>El Perú es uno de los grandes productores de café de altura del mundo. En Wasi trabajamos con <strong>granos 100 % peruanos de origen</strong>, "
            "de regiones como Cusco, Cajamarca, Junín, Amazonas y San Martín.</p>")},
        {"h2": "Cómo reconocer una buena taza", "html": (
            "<p>No hace falta ser barista para darse cuenta. Fíjate en esto la próxima vez que pidas un espresso:</p><ul>"
            "<li><strong>La crema:</strong> una capa color avellana, fina y persistente. Si es blanquecina o desaparece en segundos, algo falló.</li>"
            "<li><strong>El sabor:</strong> intenso pero equilibrado, con algo de dulzor. Un café muy amargo suele estar sobreextraído o quemado.</li>"
            "<li><strong>El final:</strong> el sabor que queda en la boca debe ser agradable, no áspero.</li>"
            "<li><strong>La leche:</strong> en un capuchino, la espuma debe ser sedosa, sin burbujas grandes, y no debe tapar el café.</li></ul>")},
        {"h2": "La carta de café de Wasi, con precios", "html": (
            "<p>Si quieres probar el café en estado puro, empieza por lo corto:</p><ul>"
            f"<li><strong>Espresso ({s('Espresso')}):</strong> shot intenso de café peruano. <strong>Ristretto ({s('Ristretto')})</strong> si lo quieres aún más concentrado, y <strong>Espresso Doble ({s('Espresso Doble')})</strong> para los que necesitan más.</li>"
            f"<li><strong>Café Filtrado ({s('Café Filtrado')}):</strong> suave y equilibrado, ideal para notar los sabores del grano.</li>"
            f"<li><strong>Americano ({s('Americano')}):</strong> espresso con agua caliente, suave y aromático.</li></ul>"
            "<p>Con leche:</p><ul>"
            f"<li><strong>Cortado ({s('Cortado')}):</strong> espresso con un toque de leche vaporizada.</li>"
            f"<li><strong>Café con Leche ({s('Café con Leche')})</strong> y <strong>Capuchino ({s('Capuchino')})</strong>, con espuma cremosa.</li>"
            f"<li><strong>Mocachino ({s('Mocachino')}):</strong> espresso con chocolate y leche.</li>"
            f"<li><strong>Tepuchino ({s('Tepuchino')}):</strong> nuestra creación de té con espuma, para quien no toma café.</li></ul>"),
         "fotos": [foto('Espresso'), foto('Cortado'), foto('Capuchino'), foto('Café Filtrado')]},
        {"h2": "Para los días de calor y para el postre", "html": (
            f"<p>En verano el café también se toma frío: <strong>Café Helado ({s('Café Helado')})</strong>, espresso con agua fría y hielo, "
            f"o <strong>Café con Leche Helado ({s('Café con Leche Helado')})</strong>, cremoso. Y si quieres terminar con algo dulce, el "
            f"<strong>Affogato Clásico ({s('Affogato Clásico')})</strong> es helado de vainilla ahogado en espresso. Nuestra versión con medio "
            f"onza de pisco, el <strong>Affogato Wasi + Pisco ({s('Affogato Wasi + Pisco')})</strong>, es nuestra receta de la casa.</p>"),
         "fotos": [foto('Café Helado'), foto('Café con Leche Helado'), foto('Affogato Clásico'), foto('Affogato Wasi + Pisco')]},
        {"h2": "Qué pedir según tu gusto", "html": (
            "<ul><li><strong>Te gusta el café fuerte:</strong> espresso o ristretto.</li>"
            "<li><strong>Prefieres algo suave:</strong> café filtrado o americano.</li>"
            "<li><strong>Quieres algo cremoso:</strong> capuchino o café con leche.</li>"
            "<li><strong>Buscas algo dulce:</strong> mocachino o affogato.</li>"
            "<li><strong>No tomas café:</strong> tepuchino o un chocolate caliente artesanal peruano.</li></ul>"
            "<p>Y si quieres aprender a prepararlo en casa, tenemos un <a href=\"/curso\">curso de café y barismo</a>.</p>")},
    ],
    "faq": [
        {"p": "¿Qué café usa Wasi Café?", "r": "Granos 100 % peruanos de origen, de regiones como Cusco, Cajamarca, Junín, Amazonas y San Martín, preparados por baristas."},
        {"p": "¿Cuánto cuesta un café en Wasi Café?", "r": f"El café filtrado cuesta {s('Café Filtrado')}, el espresso y el americano {s('Espresso')}, y el capuchino {s('Capuchino')}."},
        {"p": "¿Dónde está Wasi Café?", "r": "En Luis Felipe Villarán 904, San Isidro, Lima, a pasos de la avenida Javier Prado."},
        {"p": "¿Tienen opciones sin café?", "r": f"Sí: tepuchino ({s('Tepuchino')}), chocolate caliente artesanal ({s('Chocolate Caliente')}), infusiones, jugos y batidos."},
    ],
    "relacionados": ["como-reconocer-un-buen-espresso", "flat-white-cortado-y-capuccino-diferencias", "cafe-peruano-de-origen-cajamarca-cusco-amazonas-san-martin"],
})

# ------------------------------------------------------------------- 3. Brunch
fichas.append({
    "slug": "brunch-en-san-isidro-que-pedir-como-elegir",
    "tituloSeo": "Brunch en San Isidro: qué pedir y precios | Wasi Café",
    "h1": "Brunch en San Isidro: qué pedir en Wasi Café, plato por plato y con precios",
    "tituloCorto": "Brunch en San Isidro",
    "ogTitulo": "Brunch en San Isidro: la carta de Wasi Café con precios",
    "descripcion": "Brunch en San Isidro con precios reales: sándwiches, omelettes, ensaladas, postres y pisco sour en Wasi Café. Horario de sábado y qué pedir para compartir.",
    "eyebrow": "brunch en San Isidro",
    "fecha": "2026-06-13", "modificado": HOY,
    "about": ["Brunch", "San Isidro", "Sándwiches peruanos"],
    "intro": (
        "<p>El <strong>brunch</strong> es la comida que no obliga a elegir entre desayuno y almuerzo. En San Isidro funciona sobre todo los sábados, "
        "cuando hay tiempo para sentarse sin mirar el reloj. Esta es la guía de qué pedir en <strong>Wasi Café</strong>, con los precios de la carta.</p>")
    ,
    "secciones": [
        {"h2": "Cuándo ir", "html": (
            "<p>El sábado abrimos de <strong>9:00 a. m. a 9:00 p. m.</strong>, así que el brunch puede empezar temprano o a mediodía. "
            "De lunes a viernes abrimos a las 8:00 a. m. Los domingos estamos cerrados.</p>"
            "<p>Si vienes en grupo el sábado, pide la reserva desde la <a href=\"/#reservar\">web</a>: te la confirmamos por WhatsApp.</p>")},
        {"h2": "Lo salado: sándwiches que valen el viaje", "html": (
            "<p>La carta de sándwiches mezcla recetas peruanas y clásicos reinventados:</p><ul>"
            f"<li><strong>Chicharrón ({s('Chicharrón')}):</strong> pan con chicharrón, camote frito y salsa criolla.</li>"
            f"<li><strong>Butifarra ({s('Butifarra')}):</strong> jamón del país con salsa criolla, el clásico peruano.</li>"
            f"<li><strong>Club Wasi ({s('Club Wasi')}):</strong> pollo, chorizo, tocino, queso, lechuga y tomate. Para compartir o para mucha hambre.</li>"
            f"<li><strong>Hamburguesa Wasi ({s('Hamburguesa Wasi')}):</strong> carne de res, huevo frito, tocino, jamón inglés y queso Edam, con papas.</li>"
            f"<li><strong>Tropical Croissant ({s('Tropical Croissant')}):</strong> pollo, mayonesa, durazno y queso Edam.</li></ul>"
            f"<p>Los sándwiches que más salen son el <strong>Filete de Pollo ({s('Filete de Pollo')})</strong>, a la plancha en pan artesanal, y el "
            f"<strong>Club Sandwich ({s('Club Sandwich')})</strong>, con papas.</p>"),
         "fotos": [foto('Chicharrón'), foto('Filete de Pollo'), foto('Club Sandwich'), foto('Hamburguesa Wasi')]},
        {"h2": "Algo más ligero", "html": (
            f"<p>Si prefieres algo fresco, la <strong>Ensalada César ({s('Ensalada César')})</strong> lleva pollo a la plancha, lechuga romana y crutones, "
            f"y la <strong>Ensalada de Pollo ({s('Ensalada de Pollo')})</strong> suma palta y lechuga orgánica. "
            f"Los omelettes se preparan al momento, desde {s('Omelette de Queso')}.</p>"),
         "fotos": [foto('Ensalada César'), foto('Ensalada de Pollo'), foto('Omelette Completo')]},
        {"h2": "Lo dulce y el brindis", "html": (
            "<p>Los postres son artesanales y se hacen en casa. Los dos más pedidos son el cheesecake y la crema volteada:</p><ul>"
            f"<li><strong>Cheesecake de Frutos del Bosque ({s('Cheesecake de Frutos del Bosque')})</strong></li>"
            f"<li><strong>Carrot Cake ({s('Carrot Cake')})</strong></li>"
            f"<li><strong>Tres Leches ({s('Tres Leches')})</strong> y <strong>Crema Volteada ({s('Crema Volteada')})</strong></li></ul>"
            f"<p>Para brindar, un <strong>Pisco Sour ({s('Pisco Sour')})</strong> o un <strong>Vino Tinto de Verano ({s('Vino Tinto de Verano')})</strong>. "
            "Y si quieres postre con café a precio de combo, mira la sección Dulce Pausa de la <a href=\"/carta\">carta</a>.</p>"),
         "fotos": [foto('Cheesecake de Frutos del Bosque'), foto('Carrot Cake'), foto('Pisco Sour'), foto('Tres Leches')]},
        {"h2": "Para beber: jugos, batidos y frozen", "html": (
            "<p>Un brunch sin una buena bebida queda corto. Además del café, la carta tiene:</p><ul>"
            f"<li><strong>Jugos exprimidos al momento:</strong> papaya o piña a {s('Jugo de Papaya')}, naranja, mango o fresa a {s('Jugo de Naranja')}.</li>"
            f"<li><strong>Batidos con leche:</strong> el más pedido es el de <strong>fresa ({s('Fresa con Leche')})</strong>; también hay lúcuma, mango, palta, papaya, piña y plátano.</li>"
            f"<li><strong>Frozen de frutas:</strong> granizados de lúcuma, mango, maracuyá, chicha morada y más, desde {s('Frozen Jamaica')}.</li>"
            f"<li><strong>Clásicos peruanos fríos:</strong> chicha morada ({s('Chicha Morada')}) y limonada natural ({s('Limonada')}).</li></ul>"),
         "fotos": [foto('Fresa con Leche'), foto('Frozen Lúcuma'), foto('Chicha Morada'), foto('Limonada')]},
        {"h2": "Si vas con niños o en grupo", "html": (
            f"<p>Para los más chicos funcionan el <strong>Milk Shake ({s('Milk Shake')})</strong>, un helado artesanal (una bola a {s('1 Bola')}, "
            f"el postre que más sale) o la <strong>Salchipapa Especial ({s('Salchipapa Especial')})</strong> para compartir. "
            f"Si hay alguien vegetariano en la mesa, el sándwich <strong>Caprese ({s('Caprese')})</strong> lleva mozzarella, tomate, albahaca y aceite de oliva.</p>"
            "<p>En grupos grandes, conviene pedir la reserva desde la web y avisar en la nota cuántos son y si hay alguna celebración.</p>"),
         "fotos": [foto('Milk Shake'), foto('1 Bola', 'Helado artesanal · desde S/ 9.90'), foto('Caprese')]},
        {"h2": "Cómo armar un brunch para dos", "html": (
            "<p>Una combinación que funciona: un sándwich salado para compartir, una ensalada, dos bebidas (un capuchino y un jugo exprimido al momento) "
            f"y un postre al centro. Con el Club Wasi ({s('Club Wasi')}), una Ensalada César ({s('Ensalada César')}), un Capuchino ({s('Capuchino')}), "
            f"un Jugo de Naranja ({s('Jugo de Naranja')}) y un Carrot Cake ({s('Carrot Cake')}), dos personas comen bien y prueban de todo.</p>")},
        {"h2": "Antes de ir", "html": (
            f"<p>Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong> (<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">ver mapa</a>). "
            "Hay WiFi gratis, el ambiente es pet friendly y aceptamos efectivo, tarjeta, Yape y Plin.</p>")},
    ],
    "faq": [
        {"p": "¿Wasi Café abre los domingos para el brunch?", "r": "No. El mejor día para el brunch es el sábado, de 9:00 a. m. a 9:00 p. m."},
        {"p": "¿Cuánto cuesta un brunch en Wasi Café?", "r": f"Un sándwich va de {s('Mixto Clásico')} a {s('Club Wasi')}, las ensaladas de {s('Ensalada de Pollo')} a {s('Ensalada César')} y los postres desde {s('Pie de Limón')}."},
        {"p": "¿Tienen cócteles?", "r": f"Sí: Pisco Sour, Piña Colada y Vino Tinto de Verano, a {s('Pisco Sour')} cada uno."},
        {"p": "¿Puedo reservar para un grupo?", "r": "Sí, desde la web. Te confirmamos la reserva por WhatsApp."},
    ],
    "relacionados": ["que-es-el-brunch-origen-historia", "opciones-veganas-sin-gluten-brunch-san-isidro", "desayunos-en-san-isidro-carta-precios-horario"],
})

# ------------------------------------------------- 4. Cafetería abierta / cómo llegar
fichas.append({
    "slug": "cafeteria-en-san-isidro-horario-como-llegar",
    "tituloSeo": "Cafetería en San Isidro abierta hoy: horario y cómo llegar",
    "h1": "Cafetería en San Isidro: horario de Wasi Café, cómo llegar y qué pedir",
    "tituloCorto": "Horario y cómo llegar",
    "ogTitulo": "¿Wasi Café está abierto hoy? Horario, dirección y servicios",
    "descripcion": "Horario de Wasi Café en San Isidro (lunes a sábado), dirección en Luis Felipe Villarán 904, cómo llegar, servicios, pagos y qué pedir si es tu primera visita.",
    "eyebrow": "horario y ubicación",
    "fecha": HOY, "modificado": HOY,
    "about": ["Cafetería", "San Isidro", "Horario"],
    "intro": (
        "<p>Si estás buscando una <strong>cafetería en San Isidro abierta ahora</strong>, aquí tienes todo lo práctico de Wasi Café en un solo lugar: "
        "horario, dirección, cómo pagar y qué pedir si es tu primera vez.</p>"),
    "secciones": [
        {"h2": "Horario", "html": (HORARIO +
            "<p>Atendemos de lunes a sábado sin cerrar a mediodía. Los domingos descansamos. "
            f"Los combos de almuerzo se sirven de 12:00 p. m. a 4:00 p. m., y el más pedido es el Combo Filete ({s('Combo Filete')}).</p>")},
        {"h2": "Dirección y cómo llegar", "html": (
            "<p>Estamos en <strong>Luis Felipe Villarán 904, San Isidro, Lima</strong>, a pasos de la avenida Javier Prado. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Abrir en Google Maps</a> para ver la ruta desde donde estés.</p>"
            "<p>Si nos escribes por WhatsApp al <strong>+51 908 724 496</strong>, te ayudamos con la referencia exacta.</p>")},
        {"h2": "Qué vas a encontrar", "html": (
            "<ul><li><strong>Café de especialidad</strong> con granos 100 % peruanos de origen (Cusco, Cajamarca, Junín, Amazonas y San Martín).</li>"
            "<li><strong>Desayunos</strong> desde las 8:00 a. m., <strong>sándwiches peruanos</strong>, ensaladas y <strong>postres artesanales</strong> hechos en casa.</li>"
            "<li><strong>WiFi gratis</strong> y espacio para trabajar o estudiar.</li>"
            "<li><strong>Pet friendly:</strong> tu perro es bienvenido.</li>"
            "<li><strong>Pedido desde la mesa</strong> con código QR.</li>"
            "<li><strong>Tarjeta de sellos</strong> en tu celular para acumular premios.</li>"
            "<li>Reconocidos como <strong>«Recomendado» por Restaurant Guru</strong> en 2026, por los comentarios de nuestros clientes.</li></ul>")},
        {"h2": "Cómo pedir desde la mesa", "html": (
            "<p>En cada mesa hay un código QR. Lo escaneas con la cámara del celular y se abre la carta con fotos y precios; eliges lo que quieres "
            "y el pedido llega directo a la barra, sin esperar a que pase alguien a tomarlo. Desde la misma página puedes <strong>llamar al mozo</strong> "
            "o <strong>pedir la cuenta</strong> cuando terminas. Si prefieres pedir en persona, también se puede, como siempre.</p>")},
        {"h2": "Formas de pago y comprobantes", "html": (
            "<p>Aceptamos <strong>efectivo, tarjeta, Yape y Plin</strong>. Emitimos <strong>boleta o factura electrónica</strong>; si necesitas factura, "
            "tenla lista con tu RUC al momento de pagar. Si nos dejas tu celular, también te enviamos el comprobante por WhatsApp.</p>")},
        {"h2": "Qué pedir en tu primera visita", "html": (
            f"<p>Para conocernos: un <strong>Capuchino ({s('Capuchino')})</strong> o un <strong>Café Filtrado ({s('Café Filtrado')})</strong>, "
            f"un <strong>sándwich de Chicharrón ({s('Chicharrón')})</strong> si tienes hambre, y para cerrar, el "
            f"<strong>Affogato Wasi + Pisco ({s('Affogato Wasi + Pisco')})</strong>. Toda la carta, con precios al día, está en <a href=\"/carta\">wasicafe.com/carta</a>.</p>"),
         "fotos": [foto('Capuchino'), foto('Chicharrón'), foto('Affogato Wasi + Pisco')]},
        {"h2": "Almuerzo de lunes a sábado", "html": (
            "<p>De lunes a sábado, de 12:00 p. m. a 4:00 p. m., hay combos de almuerzo a precio cerrado, con plato principal, papas andinas y bebida a elección:</p><ul>"
            f"<li><strong>Combo Filete ({s('Combo Filete')})</strong>, el más pedido.</li>"
            f"<li><strong>Combo Bistec</strong>, <strong>Combo Chuleta</strong>, <strong>Combo Milanesa</strong>, <strong>Combo Suprema</strong> y <strong>Combo Hamburguesa</strong>, a {s('Combo Bistec')} cada uno.</li></ul>"
            "<p>Es una opción práctica si trabajas en la zona y quieres comer bien sin salir de San Isidro. El detalle está en la guía de <a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">almuerzo en San Isidro</a>.</p>")},
        {"h2": "Para llevar y para trabajar", "html": (
            "<p>Todo lo de la carta se puede pedir <strong>para llevar</strong>. Y si vienes a trabajar o a estudiar, hay WiFi gratis y estamos abiertos "
            "de corrido todo el día, así que puedes llegar a media mañana y quedarte hasta el almuerzo.</p>"
            "<p>Si te interesa el café más allá de la taza, tenemos un <a href=\"/curso\">curso de café y barismo</a> para empezar desde cero.</p>")},
        {"h2": "Reservas y grupos", "html": (
            "<p>Las reservas se piden desde la <a href=\"/#reservar\">web</a>: eliges día, hora y número de personas, y te confirmamos por WhatsApp. "
            "Para reuniones de trabajo, cumpleaños pequeños o grupos, escríbenos con anticipación.</p>")},
    ],
    "faq": [
        {"p": "¿Wasi Café abre hoy?", "r": "Abrimos de lunes a viernes de 8:00 a. m. a 9:00 p. m. y los sábados de 9:00 a. m. a 9:00 p. m. Los domingos está cerrado."},
        {"p": "¿Dónde queda Wasi Café?", "r": "En Luis Felipe Villarán 904, San Isidro, Lima, a pasos de la avenida Javier Prado."},
        {"p": "¿Aceptan Yape o tarjeta?", "r": "Sí: efectivo, tarjeta, Yape y Plin. Emitimos boleta o factura electrónica."},
        {"p": "¿Puedo ir con mi perro?", "r": "Sí, Wasi Café es pet friendly."},
        {"p": "¿Hay WiFi?", "r": "Sí, WiFi gratis para clientes."},
    ],
    "relacionados": ["desayunos-en-san-isidro-carta-precios-horario", "cafeterias-para-trabajar-laptop-san-isidro", "cafeterias-pet-friendly-san-isidro"],
})

json.dump(fichas, open(AQUI / 'fichas_pilares.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
txt = json.dumps(fichas, ensure_ascii=False)
print(len(fichas), 'fichas', '| guiones largos:', txt.count('—'))
