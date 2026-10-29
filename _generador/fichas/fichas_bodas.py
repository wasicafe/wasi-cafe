"""Bodas pequeñas y cumpleaños con local exclusivo (29/10/2026).

Datos del dueño (29/10/2026): paquetes para BODAS y CUMPLEAÑOS de 20 a 30 personas
con decoración, comida, torta y el local exclusivo; cualquier día; el precio se
cotiza por WhatsApp (no se publica). Del cumpleaños, la portada ya decía:
decoración temática, torta personalizada, bocaditos y bebidas.
Lo demás (carta, horario, dirección, pagos) sale de la carta del POS y la portada.
No se promete lo que no consta (música, fotógrafo, menú cerrado, sabores de torta).
Uso: python3 fichas_bodas.py [--rel]  → escribe bodas.json
"""
import json, pathlib, sys

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-29'
MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
WA_BODA = 'https://wa.me/51908724496?text=Hola!%20Quiero%20cotizar%20una%20boda%20en%20Wasi%20Caf%C3%A9'
WA_CUMPLE = 'https://wa.me/51908724496?text=Hola!%20Quiero%20cotizar%20un%20cumplea%C3%B1os%20en%20Wasi%20Caf%C3%A9'
WA_EN = 'https://wa.me/51908724496?text=Hi!%20I%27d%20like%20a%20quote%20for%20a%20wedding%20at%20Wasi%20Caf%C3%A9'
SLUG_BODA = 'bodas-pequenas-en-san-isidro-local-para-20-a-30-personas'
SLUG_CUMPLE = 'local-para-cumpleanos-en-san-isidro-20-a-30-personas'
SLUG_EN = 'small-wedding-venue-san-isidro-lima'


def foto(nombre, pie):
    x = CARTA[nombre]
    if not x.get('img'):
        raise SystemExit(f'sin foto: {nombre}')
    return {'src': '/' + x['img'].split('wasicafe.com/')[1], 'alt': f"{nombre} de Wasi Café, San Isidro", 'pie': pie}


def rel(*slugs):
    return list(slugs) if '--rel' in sys.argv else [s for s in slugs if s not in (SLUG_BODA, SLUG_CUMPLE, SLUG_EN)]


fichas = []

# ------------------------------------------------------------ Bodas pequeñas
fichas.append({
    "slug": SLUG_BODA,
    "tituloSeo": "Bodas pequeñas en San Isidro: local para 20 a 30 personas",
    "h1": "Bodas pequeñas en San Isidro: un local solo para ustedes, para 20 a 30 invitados",
    "tituloCorto": "Bodas pequeñas en San Isidro",
    "ogTitulo": "Tu boda pequeña en San Isidro, con el local solo para ustedes",
    "descripcion": "Boda pequeña o civil en San Isidro, Lima: Wasi Café queda solo para ustedes, con 20 a 30 invitados, decoración, comida y torta. Cotiza por WhatsApp.",
    "eyebrow": "bodas pequeñas en Lima",
    "fecha": HOY, "modificado": HOY,
    "about": ["Boda pequeña", "Boda civil", "San Isidro"],
    "intro": (
        "<p>No todas las bodas necesitan un salón para doscientas personas. Cada vez más parejas en Lima eligen una "
        "<strong>boda pequeña</strong>: la familia cercana, los amigos de siempre y un lugar donde se pueda conversar. "
        "En <strong>Wasi Café</strong>, en San Isidro, tenemos un paquete pensado justo para eso: el local "
        "<strong>solo para ustedes</strong>, para <strong>20 a 30 invitados</strong>, con <strong>decoración, comida y torta</strong>.</p>"
        f"<p>El precio depende de la fecha, del número de invitados y de lo que quieran servir, así que lo cotizamos contigo por "
        f"<a href=\"{WA_BODA}\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>. Aquí te contamos cómo funciona.</p>"),
    "secciones": [
        {"h2": "Qué incluye el paquete de boda", "html": (
            "<ul><li><strong>El local exclusivo:</strong> durante la celebración, Wasi Café es solo para su boda. Sin mesas de otros clientes.</li>"
            "<li><strong>De 20 a 30 invitados:</strong> el tamaño de una boda íntima, donde todos se conocen.</li>"
            "<li><strong>Decoración</strong> del local para la ocasión.</li>"
            "<li><strong>Comida</strong> para los invitados, que se arma con ustedes al cotizar.</li>"
            "<li><strong>Torta</strong> para el momento del corte.</li></ul>"
            "<p>Se puede hacer <strong>cualquier día</strong>: la fecha se coordina con nosotros según la disponibilidad.</p>")},
        {"h2": "Para qué tipo de boda funciona", "html": (
            "<ul><li><strong>La celebración después de la boda civil.</strong> Muchas parejas se casan por civil en la mañana y quieren un almuerzo "
            "o un brindis con su gente sin trasladarse lejos. Wasi está en San Isidro, a pasos de la avenida Javier Prado, fácil de llegar desde todo Lima.</li>"
            "<li><strong>Una boda íntima</strong> de 20 a 30 personas, sin protocolo de salón grande.</li>"
            "<li><strong>Parejas que viven fuera</strong> y vienen a casarse a Lima con la familia más cercana. "
            f"Si alguno de los invitados no habla español, tenemos una guía en inglés: <a href=\"/blog/{SLUG_EN}\">small wedding venue in Lima</a>.</li></ul>")},
        {"h2": "La comida: de nuestra cocina", "html": (
            "<p>Lo que se sirve en la boda sale de la misma cocina y la misma barra de todos los días. El menú lo definimos juntos al cotizar; "
            "para que te hagas una idea de lo que preparamos:</p><ul>"
            "<li><strong>Sándwiches peruanos y clásicos:</strong> pan con chicharrón, butifarra, club sándwich, croissants rellenos.</li>"
            "<li><strong>Café de especialidad</strong> 100 % peruano, de Cusco, Cajamarca, Junín, Amazonas y San Martín.</li>"
            "<li><strong>Jugos naturales, frozen de fruta y chicha morada.</strong></li>"
            "<li><strong>Para el brindis:</strong> en la carta hay pisco sour y vino tinto de verano.</li></ul>"
            "<p>Puedes ver todo lo que hacemos, con fotos, en <a href=\"/productos\">todos los productos</a>.</p>"),
         "fotos": [foto('Club Sandwich', 'De nuestra cocina: club sándwich'), foto('Croissant Mixto', 'Croissants rellenos'),
                   foto('Pisco Sour', 'Pisco sour para el brindis'), foto('Capuchino', 'Café de especialidad peruano')]},
        {"h2": "La torta", "html": (
            "<p>El paquete incluye torta. Somos cafetería con pastelería propia: en la vitrina de todos los días hay torta de chocolate, "
            "tres leches, carrot cake, cheesecake de frutos del bosque y crema volteada. Al cotizar te contamos las opciones para tu boda.</p>"),
         "fotos": [foto('Torta de Chocolate', 'De la pastelería: torta de chocolate'), foto('Tres Leches', 'Tres leches'),
                   foto('Cheesecake de Frutos del Bosque', 'Cheesecake de frutos del bosque'), foto('Carrot Cake', 'Carrot cake')]},
        {"h2": "Cómo cotizar tu boda", "html": (
            f"<p>Escríbenos por <a href=\"{WA_BODA}\" target=\"_blank\" rel=\"noopener\">WhatsApp al +51 908 724 496</a> con estos datos y te enviamos la propuesta:</p><ol>"
            "<li><strong>La fecha y la hora</strong> que tienen en mente (y una alternativa, por si acaso).</li>"
            "<li><strong>Cuántos invitados</strong> serán, entre 20 y 30.</li>"
            "<li><strong>Qué momento es:</strong> almuerzo después del civil, brindis de tarde, cena.</li>"
            "<li><strong>Ideas de decoración</strong> o colores, si ya los tienen.</li>"
            "<li><strong>Si alguien tiene una dieta especial</strong> o alguna alergia.</li></ol>"
            "<p>Con eso armamos el menú, la decoración y la torta, y les pasamos el precio.</p>")},
        {"h2": "Consejos para una boda pequeña que salga bien", "html": (
            "<ul><li><strong>Cierra la lista de invitados primero.</strong> En una boda de 30 personas, cada nombre cuenta: decide la lista antes de reservar.</li>"
            "<li><strong>Reserva con anticipación</strong> si la fecha es importante (un aniversario, un fin de semana largo).</li>"
            "<li><strong>Piensa en los traslados.</strong> Si hay boda civil antes, calcula el tiempo entre el registro y la celebración.</li>"
            "<li><strong>Un solo momento central.</strong> En una boda íntima funciona mejor un brindis y unas palabras que un programa largo.</li>"
            "<li><strong>Fotos y música:</strong> si los tienen, coordínalos con nosotros al cotizar para planear el espacio.</li></ul>")},
        {"h2": "También celebramos cumpleaños", "html": (
            "<p>El mismo formato de local exclusivo para 20 a 30 personas funciona para cumpleaños, con decoración temática y torta. "
            f"Lo contamos en <a href=\"/blog/{SLUG_CUMPLE}\">local para cumpleaños en San Isidro</a>. Y para reuniones de empresa, baby showers "
            "y otros paquetes, mira <a href=\"/blog/eventos-y-cumpleanos-en-cafeteria-san-isidro\">eventos en San Isidro</a>.</p>")},
        {"h2": "Dónde estamos", "html": (
            "<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro, Lima</strong>, a pasos de la avenida Javier Prado. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>. Aceptamos efectivo, tarjeta, Yape y Plin, "
            "y emitimos boleta o factura electrónica.</p>")},
    ],
    "faq": [
        {"p": "¿Wasi Café hace bodas?", "r": "Sí, bodas pequeñas de 20 a 30 invitados, con el local exclusivo, decoración, comida y torta."},
        {"p": "¿Para cuántas personas es el paquete de boda?", "r": "De 20 a 30 invitados."},
        {"p": "¿El local es solo para la boda?", "r": "Sí, durante la celebración Wasi Café queda exclusivo para su boda."},
        {"p": "¿Cuánto cuesta una boda en Wasi Café?", "r": "Depende de la fecha, el número de invitados y el menú. Se cotiza por WhatsApp al +51 908 724 496."},
        {"p": "¿Qué días se puede hacer la boda?", "r": "Cualquier día, coordinando la fecha según la disponibilidad."},
        {"p": "¿Sirve para la celebración después de la boda civil?", "r": "Sí. Wasi está en San Isidro, a pasos de Javier Prado, y es una opción cómoda para el almuerzo o el brindis después del civil."},
    ],
    "relacionados": rel(SLUG_CUMPLE, 'eventos-y-cumpleanos-en-cafeteria-san-isidro', 'postres-artesanales-cafeteria-san-isidro'),
})

# ------------------------------------------------------------ Cumpleaños con local exclusivo
fichas.append({
    "slug": SLUG_CUMPLE,
    "tituloSeo": "Local para cumpleaños en San Isidro: 20 a 30 personas",
    "h1": "Local para cumpleaños en San Isidro: Wasi Café solo para tu celebración, de 20 a 30 personas",
    "tituloCorto": "Local para cumpleaños en San Isidro",
    "ogTitulo": "Celebra tu cumpleaños en Wasi Café, con el local solo para ti",
    "descripcion": "Local para cumpleaños en San Isidro, Lima, para 20 a 30 personas: Wasi Café exclusivo, decoración temática, torta, comida y bebidas. Cotiza por WhatsApp.",
    "eyebrow": "cumpleaños en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Cumpleaños", "Local para eventos", "San Isidro"],
    "intro": (
        "<p>Buscar un <strong>local para un cumpleaños</strong> en Lima suele terminar en dos extremos: un salón enorme o una mesa apretada en un restaurante lleno. "
        "En <strong>Wasi Café</strong>, en San Isidro, hay un punto medio: el local <strong>solo para tu celebración</strong>, para "
        "<strong>20 a 30 invitados</strong>, con <strong>decoración temática, torta y comida</strong>.</p>"
        f"<p>El precio se arma según la fecha y lo que quieras servir, y lo cotizamos contigo por "
        f"<a href=\"{WA_CUMPLE}\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>.</p>"),
    "secciones": [
        {"h2": "Qué incluye", "html": (
            "<ul><li><strong>Local exclusivo</strong> durante el cumpleaños: sin otros clientes alrededor.</li>"
            "<li><strong>De 20 a 30 invitados.</strong></li>"
            "<li><strong>Decoración temática</strong>, según el gusto del cumpleañero.</li>"
            "<li><strong>Torta personalizada.</strong></li>"
            "<li><strong>Comida, bocaditos y bebidas</strong> para el festejado y sus invitados.</li></ul>"
            "<p>Se puede hacer <strong>cualquier día</strong>, coordinando la fecha.</p>")},
        {"h2": "Para qué cumpleaños funciona", "html": (
            "<ul><li><strong>Cumpleaños de adultos</strong> con amigos y familia, para conversar sin gritar por encima de la música de otro local.</li>"
            "<li><strong>Cumpleaños de los papás o los abuelos</strong>, con toda la familia en una sola mesa.</li>"
            "<li><strong>Cumpleaños de la oficina</strong>, a pasos de la avenida Javier Prado. Emitimos factura si la paga la empresa.</li>"
            "<li><strong>Cumpleaños infantiles pequeños.</strong> Si vienen niños, mira también la guía de "
            "<a href=\"/blog/ir-a-la-cafeteria-con-ninos-san-isidro\">ir a la cafetería con niños</a>.</li></ul>")},
        {"h2": "La comida y la torta", "html": (
            "<p>Todo sale de nuestra cocina y nuestra pastelería. El menú lo definimos juntos al cotizar; algunas ideas de lo que preparamos a diario:</p><ul>"
            "<li><strong>Bocaditos salados:</strong> empanadas, croissants rellenos, mixtos y sándwiches peruanos.</li>"
            "<li><strong>Dulces:</strong> alfajores, brownies, pies y tortas de la casa.</li>"
            "<li><strong>Bebidas:</strong> jugos naturales, frozen de fruta, chicha morada, limonada y café de especialidad.</li></ul>"
            "<p>Todo, con foto, en <a href=\"/productos\">todos los productos</a>.</p>"),
         "fotos": [foto('Empanada de Pollo', 'Empanadas recién horneadas'), foto('Alfajor', 'Alfajores'),
                   foto('Torta de Chocolate', 'De la pastelería: torta de chocolate'), foto('Frozen Fresa', 'Frozen de fruta')]},
        {"h2": "Cómo cotizar", "html": (
            f"<p>Escríbenos por <a href=\"{WA_CUMPLE}\" target=\"_blank\" rel=\"noopener\">WhatsApp al +51 908 724 496</a> con:</p><ol>"
            "<li>La <strong>fecha y la hora</strong> del cumpleaños.</li>"
            "<li>El <strong>número de invitados</strong>, entre 20 y 30.</li>"
            "<li>El <strong>tema o los colores</strong> para la decoración.</li>"
            "<li>Qué te gustaría para la <strong>torta</strong>.</li>"
            "<li>Si hay <strong>niños, alergias o dietas especiales</strong>.</li></ol>"
            "<p>Con eso te enviamos la propuesta con el precio.</p>")},
        {"h2": "Ideas para la decoración temática", "html": (
            "<ul><li><strong>Un tema que diga algo del cumpleañero:</strong> su color favorito, un viaje, una película, su equipo.</li>"
            "<li><strong>Dos o tres colores, no más:</strong> en un local íntimo, una paleta corta se ve más elegante que muchos colores juntos.</li>"
            "<li><strong>Fotos de distintas épocas:</strong> funcionan muy bien en cumpleaños de 40, 50 o 60, y sacan conversación.</li>"
            "<li><strong>El nombre y la edad,</strong> si quieren que se vea en las fotos.</li></ul>"
            "<p>Cuéntanos la idea al cotizar y la llevamos a la decoración del local.</p>")},
        {"h2": "Si son menos de 20 personas", "html": (
            "<p>Para grupos más chicos no hace falta el local exclusivo: puedes reservar mesa desde la <a href=\"/#reservar\">web</a> "
            "(eliges día, hora y número de personas, y te confirmamos por WhatsApp) o pedir el <strong>Paquete Café</strong> o el "
            "<strong>Paquete Brunch</strong>. Los explicamos en <a href=\"/blog/eventos-y-cumpleanos-en-cafeteria-san-isidro\">eventos en San Isidro</a>.</p>")},
        {"h2": "También hacemos bodas pequeñas", "html": (
            f"<p>El mismo formato, con decoración, comida, torta y el local solo para ustedes, sirve para bodas de 20 a 30 invitados: "
            f"lo contamos en <a href=\"/blog/{SLUG_BODA}\">bodas pequeñas en San Isidro</a>.</p>")},
        {"h2": "Dónde estamos", "html": (
            "<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro, Lima</strong>, a pasos de la avenida Javier Prado. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>. Aceptamos efectivo, tarjeta, Yape y Plin.</p>")},
    ],
    "faq": [
        {"p": "¿Wasi Café se puede alquilar para un cumpleaños?", "r": "Sí, para cumpleaños de 20 a 30 personas con el local exclusivo, decoración temática, torta y comida."},
        {"p": "¿Cuánto cuesta un cumpleaños en Wasi Café?", "r": "Depende de la fecha, el número de invitados y el menú. Se cotiza por WhatsApp al +51 908 724 496."},
        {"p": "¿Qué días se puede celebrar?", "r": "Cualquier día, coordinando la fecha según la disponibilidad."},
        {"p": "¿Y si somos menos de 20?", "r": "Puedes reservar mesa desde la web o pedir el Paquete Café o el Paquete Brunch."},
    ],
    "relacionados": rel(SLUG_BODA, 'eventos-y-cumpleanos-en-cafeteria-san-isidro', 'postres-artesanales-cafeteria-san-isidro'),
})

# ------------------------------------------------------------ Inglés: small wedding venue
fichas.append({
    "idioma": "en",
    "slug": SLUG_EN,
    "tituloSeo": "Small wedding venue in San Isidro, Lima | Wasi Café",
    "h1": "Small wedding venue in San Isidro, Lima: Wasi Café, exclusively yours for 20 to 30 guests",
    "tituloCorto": "Small wedding venue in Lima",
    "ogTitulo": "A small wedding in Lima, with the venue all to yourselves",
    "descripcion": "Small wedding venue in San Isidro, Lima, for 20 to 30 guests: Wasi Café exclusively for you, with decoration, food and wedding cake. Quotes on WhatsApp.",
    "eyebrow": "small weddings in Lima",
    "fecha": HOY, "modificado": HOY,
    "about": ["Small wedding", "Wedding venue", "Lima"],
    "intro": (
        "<p>Getting married in Lima with just your closest people? <strong>Wasi Café</strong>, a specialty coffee shop in San Isidro, Lima's business district, "
        "offers a <strong>small wedding package</strong>: the whole venue <strong>exclusively for you</strong>, for <strong>20 to 30 guests</strong>, "
        "with <strong>decoration, food and a wedding cake</strong>.</p>"
        f"<p>The price depends on the date, the number of guests and the menu, so we quote it on "
        f"<a href=\"{WA_EN}\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>.</p>"),
    "secciones": [
        {"h2": "What the package includes", "html": (
            "<ul><li><strong>The venue, exclusively yours</strong> during the celebration: no other customers.</li>"
            "<li><strong>20 to 30 guests.</strong></li>"
            "<li><strong>Decoration</strong> for the occasion.</li>"
            "<li><strong>Food</strong> for your guests, planned with you when we quote.</li>"
            "<li><strong>A wedding cake.</strong></li></ul>"
            "<p>Any day of the week, depending on availability.</p>")},
        {"h2": "Who it is for", "html": (
            "<ul><li><strong>Couples having a civil ceremony in Lima</strong> who want a lunch or a toast afterwards nearby.</li>"
            "<li><strong>Couples living abroad</strong> who come to Lima to marry with their closest family.</li>"
            "<li><strong>Intimate weddings</strong> where everyone knows each other.</li></ul>"
            "<p>San Isidro is central and easy to reach, and many international hotels are in the district.</p>")},
        {"h2": "The food and the cake", "html": (
            "<p>Everything comes from our own kitchen and pastry counter. We plan the menu with you; as an idea of what we make every day: "
            "Peruvian sandwiches like pan con chicharrón and butifarra, club sandwiches and filled croissants, fresh juices, chicha morada, "
            "Peruvian specialty coffee from Cusco, Cajamarca, Junín, Amazonas and San Martín, and pisco sour for the toast.</p>"
            "<p>For the cake, our pastry counter makes chocolate cake, tres leches, carrot cake and berry cheesecake; we will tell you the options when we quote. "
            "See everything with photos in <a href=\"/en/products\">all products</a>.</p>"),
         "fotos": [foto('Torta de Chocolate', 'Chocolate cake from our pastry counter'), foto('Pisco Sour', 'Pisco sour for the toast'),
                   foto('Club Sandwich', 'Club sandwich'), foto('Capuchino', 'Peruvian specialty coffee')]},
        {"h2": "Why a café for a small wedding", "html": (
            "<p>A large banquet hall can feel empty with 25 guests. A café is the opposite: warm, close, made for conversation. "
            "With the venue closed to the public, your guests can move around, talk to everyone and enjoy the food without a stiff programme. "
            "It also keeps things simple: one place for the toast, the meal and the cake, in a central district that is easy to reach from anywhere in Lima.</p>")},
        {"h2": "Tips for a small wedding in Lima", "html": (
            "<ul><li><strong>Close the guest list first.</strong> At 30 guests, every name matters.</li>"
            "<li><strong>Book early</strong> if your date matters, especially around long weekends and holidays.</li>"
            "<li><strong>Plan the timing</strong> between the civil ceremony and the celebration, and allow for Lima traffic.</li>"
            "<li><strong>Keep one central moment:</strong> a toast and a few words work better than a long programme at an intimate wedding.</li>"
            "<li><strong>Photographer or music?</strong> Tell us when you ask for a quote so we can plan the space.</li></ul>")},
        {"h2": "How to get a quote", "html": (
            f"<p>Message us on <a href=\"{WA_EN}\" target=\"_blank\" rel=\"noopener\">WhatsApp at +51 908 724 496</a> with your date and time, "
            "the number of guests (20 to 30), the moment (lunch, afternoon toast or dinner), any decoration ideas, and dietary needs. "
            "We will send you a proposal with the price.</p>")},
        {"h2": "Practical information", "html": (
            "<ul><li><strong>Address:</strong> Luis Felipe Villarán 904, San Isidro, Lima, a short walk from Javier Prado Avenue.</li>"
            "<li><strong>Payments:</strong> cash, cards, Yape and Plin; we issue receipts and invoices.</li>"
            "<li><strong>Language:</strong> our online menu has an English version.</li></ul>"
            f"<p><a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Open in Google Maps</a>. More about the café in our "
            "<a href=\"/blog/coffee-shop-in-san-isidro-lima-wasi-cafe\">visitor's guide</a>.</p>")},
    ],
    "faq": [
        {"p": "Does Wasi Café host weddings?", "r": "Yes, small weddings of 20 to 30 guests, with the venue exclusively yours, decoration, food and cake."},
        {"p": "How much does a small wedding at Wasi Café cost?", "r": "It depends on the date, the number of guests and the menu. Quotes on WhatsApp at +51 908 724 496."},
        {"p": "Which days are available?", "r": "Any day of the week, depending on availability."},
    ],
    "relacionados": rel('coffee-shop-in-san-isidro-lima-wasi-cafe', 'peruvian-drinks-to-try-in-lima'),
})

json.dump(fichas, open(AQUI / 'bodas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(fichas), 'fichas | guiones largos:', json.dumps(fichas, ensure_ascii=False).count('—'))
