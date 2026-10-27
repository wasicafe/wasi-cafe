"""Segunda ola de guías del blog de Wasi Café (27/10/2026).

Mismas reglas que fichas_pilares.py: precios y fotos de la carta del POS
(carta-wasi.json, regenerada hoy desde carta.html), horario y servicios de la
portada, «lo más pedido» de las ventas reales de 60 días. Nada inventado:
no se afirma lo que no consta (por ejemplo, enchufes).
Uso: python3 fichas_ola2.py  → escribe almuerzo.json y mejoras.json
"""
import json, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-27'


def foto(nombre, pie=None):
    x = CARTA[nombre]
    if not x.get('img'):
        raise SystemExit(f'sin foto: {nombre}')
    precio = f"S/ {x['p']:.2f}"
    return {'src': '/' + x['img'].split('wasicafe.com/')[1], 'alt': f"{nombre} en Wasi Café, San Isidro",
            'pie': pie or f"{nombre} · {precio}"}


def s(n):
    return f"S/ {CARTA[n]['p']:.2f}"


def li(n, texto=None):
    d = texto if texto is not None else CARTA[n].get('d', '')
    return f"<li><strong>{n} ({s(n)})</strong>{': ' + d[0].lower() + d[1:] + '.' if d else '.'}</li>"


MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
HORARIO_TXT = ('de lunes a viernes de <strong>8:00 a. m. a 9:00 p. m.</strong> y los sábados de '
               '<strong>9:00 a. m. a 9:00 p. m.</strong>; los domingos estamos cerrados')
COMBOS = [('Combo Filete', 'filete de pollo a la plancha'), ('Combo Bistec', 'bistec a la plancha'),
          ('Combo Chuleta', 'chuleta de cerdo'), ('Combo Milanesa', 'milanesa empanizada'),
          ('Combo Suprema', 'suprema de pollo'), ('Combo Hamburguesa', 'hamburguesa clásica')]

almuerzo = [{
    "slug": "almuerzo-en-san-isidro-combos-y-precios",
    "tituloSeo": "Almuerzo en San Isidro: combos y precios | Wasi Café",
    "h1": "Almuerzo en San Isidro cerca de Javier Prado: combos, precios y horario",
    "tituloCorto": "Almuerzo en San Isidro",
    "ogTitulo": "Almorzar en San Isidro: los combos de Wasi Café con precios",
    "descripcion": "Almuerzo en San Isidro de lunes a sábado, de 12 a 4 p. m.: combos con papas andinas y bebida desde S/ 25.90, a pasos de Javier Prado.",
    "eyebrow": "almuerzo en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Almuerzo", "San Isidro", "Javier Prado"],
    "intro": (
        "<p>Si trabajas en San Isidro, el almuerzo tiene que cumplir tres cosas: estar cerca, salir rápido y no costar una fortuna. "
        "En <strong>Wasi Café</strong>, en Luis Felipe Villarán 904, a pasos de la avenida <strong>Javier Prado</strong>, tenemos combos de almuerzo "
        "a precio cerrado de lunes a sábado. Esta guía te dice qué trae cada uno, cuánto cuesta y qué más puedes pedir si no quieres combo.</p>"
        "<p>Los precios son los de nuestra <a href=\"/carta\">carta en línea</a>, que se actualiza sola desde la caja: si algo cambia, ahí está el dato al día.</p>"),
    "secciones": [
        {"h2": "Horario del almuerzo", "html": (
            "<p>Los combos de almuerzo se sirven de <strong>lunes a sábado, de 12:00 p. m. a 4:00 p. m.</strong> Es un horario amplio a propósito: "
            "sirve para quien sale a la una en punto y también para quien recién se libera de una reunión a las tres.</p>"
            f"<p>Fuera de ese horario la cocina sigue abierta con el resto de la carta: atendemos {HORARIO_TXT}. "
            "Si quieres asegurar mesa para un grupo, reserva desde la <a href=\"/#reservar\">web</a> y te confirmamos por WhatsApp.</p>")},
        {"h2": "Los combos de almuerzo, con precio", "html": (
            "<p>Todos los combos incluyen el plato principal, una porción de <strong>papas andinas</strong> y una <strong>bebida a elección</strong>. "
            "Pides uno y ya tienes el almuerzo completo, sin sumar cosas sueltas:</p><ul>"
            + ''.join(f"<li><strong>{n} ({s(n)})</strong>: {d}, papas andinas y bebida.</li>" for n, d in COMBOS)
            + "</ul><p>Frente a pedir cada cosa por separado, el combo te ahorra entre S/ 12.90 y S/ 18.90. "
            "El <strong>Combo Filete</strong> es el más pedido por nuestros clientes, seguido del <strong>Combo Bistec</strong> y el "
            "<strong>Combo Milanesa</strong>.</p>"),
         "fotos": [foto('Papas Andinas', 'Papas andinas, el acompañamiento de todos los combos')]},
        {"h2": "Si prefieres un sándwich o algo más ligero", "html": (
            "<p>No todos los días se tiene ganas de plato de fondo. Estas son las opciones que más se piden al mediodía fuera de los combos:</p><ul>"
            + li('Filete de Pollo') + li('Club Sandwich') + li('Pollo con Palta') + li('Hamburguesa Wasi')
            + li('Sándwich de Milanesa') + li('Chicharrón') + "</ul>"
            "<p>El <strong>Filete de Pollo</strong> es el sándwich más vendido de la carta. Si vienes con hambre de verdad, el "
            "<strong>Club Sandwich</strong> trae cuatro porciones y papas andinas, y alcanza para compartir.</p>"),
         "fotos": [foto('Filete de Pollo'), foto('Club Sandwich'), foto('Pollo con Palta'), foto('Hamburguesa Wasi')]},
        {"h2": "Ensaladas y opciones para picar", "html": (
            "<p>Para un almuerzo más fresco hay dos ensaladas completas, con proteína incluida:</p><ul>"
            + li('Ensalada César') + li('Ensalada de Pollo') + "</ul>"
            "<p>Y si es para compartir en la mesa o para algo rápido entre reuniones: "
            f"<strong>Salchipapa Especial ({s('Salchipapa Especial')})</strong> con papas, chorizo, hot dog, huevo y queso, o una "
            f"<strong>empanada ({s('Empanada de Carne')})</strong> de carne, pollo o mixta, recién horneada.</p>"),
         "fotos": [foto('Ensalada César'), foto('Ensalada de Pollo'), foto('Salchipapa Especial'), foto('Empanada de Carne')]},
        {"h2": "Almorzar sin perder tiempo", "html": (
            "<p>Si tu hora de almuerzo es corta, hay tres cosas que ayudan:</p><ul>"
            "<li><strong>Pedido desde la mesa.</strong> Escaneas el código QR de tu mesa, eliges y el pedido llega directo a la barra. "
            "Desde el mismo celular puedes pedir la cuenta cuando terminas.</li>"
            "<li><strong>Para llevar.</strong> Todo lo de la carta se puede pedir para llevar a la oficina.</li>"
            "<li><strong>Factura para la empresa.</strong> Emitimos boleta o factura electrónica; ten tu RUC a la mano al pagar. "
            "Aceptamos efectivo, tarjeta, Yape y Plin.</li></ul>")},
        {"h2": "El café y el postre de después", "html": (
            "<p>Un almuerzo de oficina en Lima no termina sin cafecito. Somos una cafetería de especialidad, así que el café de sobremesa va en serio: "
            f"un <strong>Americano ({s('Americano')})</strong>, un <strong>Cortado ({s('Cortado')})</strong> o un "
            f"<strong>Capuchino ({s('Capuchino')})</strong>, con café 100 % peruano de Cusco, Cajamarca, Junín, Amazonas y San Martín.</p>"
            "<p>Si además quieres algo dulce, los combos de la <strong>Dulce Pausa</strong> juntan postre y café a precio cerrado, como el "
            f"<strong>Pie de limón + Café Americano ({s('Pie de limón + Café Americano')})</strong> o la "
            f"<strong>Crema volteada + Café Americano ({s('Crema volteada + Café Americano')})</strong>. "
            "Cambiar el americano por capuchino cuesta S/ 2 más.</p>"),
         "fotos": [foto('Pie de limón + Café Americano'), foto('Crema volteada + Café Americano')]},
        {"h2": "Cómo llegar", "html": (
            "<p>Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado: si trabajas en el centro "
            "financiero o en las torres de la zona, llegas caminando. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Abre la ubicación en Google Maps</a>. "
            "Para más detalles de horario y acceso, revisa la guía de <a href=\"/blog/cafeteria-en-san-isidro-horario-como-llegar\">horario y cómo llegar</a>.</p>")},
    ],
    "faq": [
        {"p": "¿A qué hora hay almuerzo en Wasi Café?", "r": "Los combos de almuerzo se sirven de lunes a sábado, de 12:00 p. m. a 4:00 p. m."},
        {"p": "¿Qué incluyen los combos de almuerzo?", "r": "El plato principal, papas andinas y una bebida a elección. El Combo Filete cuesta S/ 25.90 y los demás S/ 29.90."},
        {"p": "¿Se puede pedir el almuerzo para llevar?", "r": "Sí, todo lo de la carta se puede pedir para llevar."},
        {"p": "¿Dan factura?", "r": "Sí, emitimos boleta o factura electrónica. Aceptamos efectivo, tarjeta, Yape y Plin."},
        {"p": "¿Abren los domingos?", "r": "No, los domingos Wasi Café está cerrado."},
    ],
    "relacionados": ["sandwiches-peruanos-y-hamburguesas-san-isidro", "cafe-cerca-de-javier-prado-san-isidro", "reuniones-de-trabajo-en-cafeteria-san-isidro"],
}]

mejoras = []

# ------------------------------------------------------------ Sándwiches
mejoras.append({
    "slug": "sandwiches-peruanos-y-hamburguesas-san-isidro",
    "tituloSeo": "Sándwiches peruanos y hamburguesas en San Isidro | Wasi Café",
    "h1": "Sándwiches peruanos y hamburguesas en San Isidro: la carta de Wasi Café con precios",
    "tituloCorto": "Sándwiches en San Isidro",
    "ogTitulo": "Sándwiches peruanos y hamburguesas en San Isidro, con precios",
    "descripcion": "Sándwiches peruanos y hamburguesas en San Isidro con precios reales: chicharrón, butifarra, filete de pollo, club sándwich y más en Wasi Café.",
    "eyebrow": "sándwiches en San Isidro",
    "fecha": "2026-06-14", "modificado": HOY,
    "about": ["Sándwich peruano", "Hamburguesa", "San Isidro"],
    "intro": (
        "<p>El sándwich es parte de la mesa limeña: el pan con chicharrón del desayuno, la butifarra, el sánguche de pollo a media tarde. "
        "En <strong>Wasi Café</strong>, en San Isidro, la carta de sándwiches es una de las más largas de la casa, con recetas peruanas, clásicos de "
        "cafetería, croissants y hamburguesas. Aquí está completa, con precios y fotos reales.</p>"
        "<p>Todos los precios son los de nuestra <a href=\"/carta\">carta en línea</a>, que se actualiza sola desde la caja.</p>"),
    "secciones": [
        {"h2": "Sándwiches peruanos", "html": (
            "<p>Los de siempre, hechos como se deben hacer:</p><ul>"
            + li('Chicharrón') + li('Butifarra', 'Jamón del país con salsa criolla, el clásico peruano')
            + li('Sándwich de Asado') + li('Pollo con Palta') + "</ul>"
            "<p>El <strong>pan con chicharrón</strong> con camote frito y salsa criolla es nuestra recomendación si es tu primera vez. "
            "En el desayuno también lo puedes pedir en combo: el <strong>Amanecer Criollo</strong> lo trae con café americano.</p>"),
         "fotos": [foto('Chicharrón'), foto('Butifarra'), foto('Sándwich de Asado'), foto('Pollo con Palta')]},
        {"h2": "Clásicos de cafetería", "html": (
            "<p>Para el almuerzo o para acompañar el café:</p><ul>"
            + li('Filete de Pollo') + li('Sándwich de Milanesa') + li('Mixto Clásico') + li('Mixto Especial')
            + li('Caprese') + li('Club Sandwich') + li('Club Wasi') + "</ul>"
            "<p>El <strong>Filete de Pollo</strong> es el sándwich más vendido de toda la carta, y el <strong>Club Sandwich</strong> "
            "viene en cuatro porciones con papas andinas fritas: alcanza para compartir.</p>"),
         "fotos": [foto('Filete de Pollo'), foto('Sándwich de Milanesa'), foto('Club Sandwich'), foto('Mixto Clásico')]},
        {"h2": "Croissants rellenos", "html": (
            "<p>Hojaldre de mantequilla, tibio, con relleno salado:</p><ul>"
            + li('Croissant Mixto') + li('Croissant de Pollo') + li('Croissant Huevos y Jamón') + li('Tropical Croissant') + "</ul>"
            "<p>El de huevos y jamón funciona muy bien como desayuno tardío, y el tropical, con durazno, es para quien le gusta el contraste dulce y salado.</p>"),
         "fotos": [foto('Croissant Mixto'), foto('Croissant de Pollo'), foto('Croissant Huevos y Jamón'), foto('Tropical Croissant')]},
        {"h2": "Hamburguesas", "html": (
            "<p>Con carne de res y pan de hamburguesa:</p><ul>"
            + li('Hamburguesa Clásica') + li('Hamburguesa Royal') + li('Hamburguesa Wasi') + "</ul>"
            "<p>La <strong>Hamburguesa Wasi</strong> es la más completa: huevo frito, tocino, jamón inglés, queso Edam y papas andinas fritas. "
            "Al mediodía, la clásica también viene en el <a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">Combo Hamburguesa</a>, con papas y bebida.</p>"),
         "fotos": [foto('Hamburguesa Clásica'), foto('Hamburguesa Royal'), foto('Hamburguesa Wasi')]},
        {"h2": "Para acompañar", "html": (
            "<p>Si quieres sumar algo al sándwich:</p><ul>"
            + li('Papas Andinas') + li('Camote Frito') + li('Ensalada Criolla') + "</ul>"
            "<p>Y para beber, desde un jugo natural hasta una limonada o una chicha morada, o un café de especialidad si es media tarde.</p>"),
         "fotos": [foto('Papas Andinas'), foto('Camote Frito'), foto('Ensalada Criolla')]},
        {"h2": "Combos de almuerzo de 12 a 4", "html": (
            "<p>De lunes a sábado, de 12:00 p. m. a 4:00 p. m., hay combos con plato principal, papas andinas y bebida a elección: "
            f"el <strong>Combo Filete ({s('Combo Filete')})</strong> y los combos de bistec, chuleta, milanesa, suprema y hamburguesa "
            f"({s('Combo Bistec')}). El detalle está en la guía de <a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">almuerzo en San Isidro</a>.</p>")},
        {"h2": "Dónde estamos", "html": (
            f"<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de Javier Prado. Atendemos {HORARIO_TXT}. "
            "Todo se puede pedir para llevar, y en el local puedes pedir desde la mesa con el código QR. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>.</p>")},
    ],
    "faq": [
        {"p": "¿Cuál es el sándwich más pedido de Wasi Café?", "r": "El Filete de Pollo, a la plancha en pan artesanal."},
        {"p": "¿Cuánto cuesta el pan con chicharrón?", "r": f"El sándwich de chicharrón, con camote frito y salsa criolla, cuesta {s('Chicharrón')}."},
        {"p": "¿Tienen hamburguesas?", "r": f"Sí: Clásica ({s('Hamburguesa Clásica')}), Royal ({s('Hamburguesa Royal')}) y Wasi ({s('Hamburguesa Wasi')})."},
        {"p": "¿Se pueden pedir para llevar?", "r": "Sí, todos los sándwiches se pueden pedir para llevar."},
    ],
    "relacionados": ["almuerzo-en-san-isidro-combos-y-precios", "desayunos-en-san-isidro-carta-precios-horario", "maridaje-cafe-y-comida-como-combinar"],
})

# ------------------------------------------------------------ Postres
mejoras.append({
    "slug": "postres-artesanales-cafeteria-san-isidro",
    "tituloSeo": "Postres en San Isidro: tortas, pies y precios | Wasi Café",
    "h1": "Postres en San Isidro: tortas, pies y helados de Wasi Café, con precios",
    "tituloCorto": "Postres en San Isidro",
    "ogTitulo": "Postres en San Isidro: la carta dulce de Wasi Café con precios",
    "descripcion": "Postres en San Isidro con precios reales: cheesecake de frutos del bosque, crema volteada, tres leches, pies y helados, con combos de postre y café.",
    "eyebrow": "postres en San Isidro",
    "fecha": "2026-06-14", "modificado": HOY,
    "about": ["Postres", "San Isidro", "Café de especialidad"],
    "intro": (
        "<p>Un buen postre con un buen café es de los planes más simples y más ricos de la tarde. En <strong>Wasi Café</strong>, en San Isidro, "
        "la vitrina tiene tortas, pies, clásicos limeños y helados, y casi todo se puede combinar con café a precio cerrado. "
        "Esta es la carta dulce completa, con precios y fotos reales.</p>"
        "<p>Los precios salen de nuestra <a href=\"/carta\">carta en línea</a>, que se actualiza sola desde la caja.</p>"),
    "secciones": [
        {"h2": "Tortas y clásicos", "html": (
            "<ul>" + li('Cheesecake de Frutos del Bosque') + li('Crema Volteada') + li('Tres Leches') + li('Torta de Chocolate')
            + li('Carrot Cake') + "</ul>"
            "<p>Los dos más pedidos son la <strong>Crema Volteada</strong> y el <strong>Cheesecake de Frutos del Bosque</strong>. "
            "La crema volteada es el flan de caramelo de toda la vida, y combina muy bien con un americano sin azúcar.</p>"),
         "fotos": [foto('Cheesecake de Frutos del Bosque'), foto('Crema Volteada'), foto('Tres Leches'), foto('Torta de Chocolate'), foto('Carrot Cake')]},
        {"h2": "Pies", "html": (
            "<ul>" + li('Pie de Limón') + li('Pie de Manzana') + li('Pie de Maracuyá') + "</ul>"
            "<p>El de limón, con merengue suizo, es el más pedido de los tres. El de maracuyá es para quien busca algo más ácido y tropical.</p>"),
         "fotos": [foto('Pie de Limón'), foto('Pie de Manzana'), foto('Pie de Maracuyá')]},
        {"h2": "Para algo rápido con el café", "html": (
            "<ul>" + li('Alfajor') + li('Alfajor Wasi') + li('Brownie') + "</ul>"
            "<p>El <strong>alfajor</strong> es lo que más sale de la vitrina: a ese precio, es difícil no pedir uno con el café.</p>"),
         "fotos": [foto('Alfajor'), foto('Alfajor Wasi'), foto('Brownie')]},
        {"h2": "Postres con helado", "html": (
            "<ul>" + li('Brownie con Helado') + li('Croissant con Helado') + li('Banana Split') + "</ul>"
            f"<p>El helado también se pide solo: <strong>1 bola ({s('1 Bola')})</strong>, 2 bolas ({s('2 Bolas')}) o 3 bolas ({s('3 Bolas')}), "
            "en chocolate, fresa, lúcuma o vainilla. La bola de helado es, de hecho, lo más vendido de toda la sección dulce.</p>"),
         "fotos": [foto('Brownie con Helado'), foto('Croissant con Helado'), foto('Banana Split'), foto('1 Bola', 'Helado artesanal · desde S/ 9.90')]},
        {"h2": "Postre y café a precio cerrado", "html": (
            "<p>Los combos de la <strong>Dulce Pausa</strong> juntan postre y café americano. Si prefieres capuchino, cuesta S/ 2 más:</p><ul>"
            + li('Torta de chocolate + Café Americano', '') + li('Crema volteada + Café Americano', '') + li('Torta tres leches + Café Americano', '')
            + li('Carrot cake + Café Americano', '') + li('Pie de limón + Café Americano', '') + li('Pie de manzana + Café Americano', '')
            + "</ul><p>Son ideales para la tarde, para una cita o para cerrar un almuerzo de trabajo.</p>"),
         "fotos": [foto('Torta de chocolate + Café Americano'), foto('Crema volteada + Café Americano'), foto('Torta tres leches + Café Americano'), foto('Carrot cake + Café Americano')]},
        {"h2": "Qué café pedir con cada postre", "html": (
            "<ul><li><strong>Postres muy dulces</strong> (tres leches, crema volteada): un americano o un espresso, que cortan el dulzor.</li>"
            "<li><strong>Chocolate</strong> (torta, brownie): un capuchino o un mocachino, que suman cremosidad.</li>"
            "<li><strong>Ácidos</strong> (pie de limón, maracuyá, cheesecake de frutos del bosque): un café filtrado, más ligero y aromático.</li></ul>"
            "<p>Todo nuestro café es de especialidad, 100 % peruano, de Cusco, Cajamarca, Junín, Amazonas y San Martín. "
            "Para más ideas, mira la guía de <a href=\"/blog/maridaje-cafe-y-comida-como-combinar\">maridaje de café y comida</a>.</p>")},
        {"h2": "Para llevar y dónde estamos", "html": (
            f"<p>Todos los postres se pueden pedir para llevar. Estamos en <strong>Luis Felipe Villarán 904, San Isidro</strong>, "
            f"a pasos de Javier Prado, y atendemos {HORARIO_TXT}. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>.</p>")},
    ],
    "faq": [
        {"p": "¿Cuál es el postre más pedido de Wasi Café?", "r": "La crema volteada y el cheesecake de frutos del bosque; en la vitrina, el alfajor."},
        {"p": "¿Hay combos de postre y café?", "r": "Sí, los combos Dulce Pausa juntan un postre con café americano; cambiarlo por capuchino cuesta S/ 2 más."},
        {"p": "¿Qué sabores de helado tienen?", "r": "Chocolate, fresa, lúcuma y vainilla, desde S/ 9.90 la bola."},
        {"p": "¿Se pueden pedir postres para llevar?", "r": "Sí, todos los postres se pueden pedir para llevar."},
    ],
    "relacionados": ["antojos-dulces-de-la-tarde-merienda-san-isidro", "maridaje-cafe-y-comida-como-combinar", "primera-cita-en-cafeteria-san-isidro"],
})

# ------------------------------------------------------------ Trabajar con laptop
mejoras.append({
    "slug": "cafeterias-para-trabajar-laptop-san-isidro",
    "tituloSeo": "Cafetería para trabajar con laptop en San Isidro | Wasi Café",
    "h1": "Cafetería para trabajar con laptop en San Isidro: WiFi, horario corrido y café de especialidad",
    "tituloCorto": "Trabajar con laptop en San Isidro",
    "ogTitulo": "Dónde trabajar con laptop en San Isidro: Wasi Café",
    "descripcion": "Cafetería para trabajar con laptop en San Isidro: WiFi gratis, abierto de corrido de 8 a. m. a 9 p. m., combos de almuerzo y café de especialidad.",
    "eyebrow": "trabajar en San Isidro",
    "fecha": "2026-06-14", "modificado": HOY,
    "about": ["Trabajo remoto", "San Isidro", "Cafetería"],
    "intro": (
        "<p>Trabajar desde una cafetería funciona cuando hay buena conexión, se puede pasar el día entero y el café ayuda en vez de distraer. "
        "<strong>Wasi Café</strong>, en Luis Felipe Villarán 904, San Isidro, a pasos de Javier Prado, tiene WiFi gratis, abre de corrido todo el día "
        "y sirve desayuno, almuerzo y café de especialidad sin que tengas que moverte. Esto es lo que encontrarás, con precios reales.</p>"),
    "secciones": [
        {"h2": "Horario corrido, de la mañana a la noche", "html": (
            f"<p>Atendemos {HORARIO_TXT}, sin cerrar al mediodía. Puedes llegar a las 8 con el primer café, almorzar sin salir y seguir hasta la noche.</p>"
            "<p>Si tienes una videollamada importante o vienes en grupo, reserva desde la <a href=\"/#reservar\">web</a> para asegurar mesa: "
            "eliges día, hora y número de personas, y te confirmamos por WhatsApp.</p>")},
        {"h2": "WiFi y pedido desde la mesa", "html": (
            "<p>El <strong>WiFi es gratis</strong> para clientes. Y para no interrumpir lo que estás haciendo, cada mesa tiene un <strong>código QR</strong>: "
            "lo escaneas, ves la carta con fotos y precios, y el pedido llega directo a la barra. Desde el mismo celular puedes llamar al mozo o pedir la cuenta.</p>"
            "<p>Si necesitas factura para tu empresa, emitimos boleta o factura electrónica. Aceptamos efectivo, tarjeta, Yape y Plin.</p>")},
        {"h2": "El café para una jornada larga", "html": (
            "<p>Somos una cafetería de especialidad con café 100 % peruano de Cusco, Cajamarca, Junín, Amazonas y San Martín. Para trabajar, estos son los que más se piden:</p><ul>"
            + li('Americano') + li('Capuchino') + li('Café Filtrado') + li('Cortado') + "</ul>"
            "<p>El <strong>americano</strong> es, por lejos, el café que más servimos. Para la tarde, si hace calor, hay frappés y café helado. "
            "Si te preocupa dormir mal, lee <a href=\"/blog/cafeina-y-sueno-a-que-hora-el-ultimo-cafe\">a qué hora tomar el último café</a>.</p>"),
         "fotos": [foto('Americano'), foto('Capuchino'), foto('Café Filtrado'), foto('Cortado')]},
        {"h2": "Desayuno sin salir del lugar", "html": (
            f"<p>Desde las 8:00 a. m. hay combos de desayuno: el <strong>Continental ({s('Continental')})</strong>, el <strong>Light ({s('Light')})</strong> "
            f"o el <strong>Desayuno Americano ({s('Desayuno Americano')})</strong>, todos con café incluido. "
            "La carta completa está en la guía de <a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>"),
         "fotos": [foto('Huevos Revueltos'), foto('Croissant Huevos y Jamón'), foto('Tamal Criollo')]},
        {"h2": "Almuerzo de 12 a 4", "html": (
            "<p>De lunes a sábado, de 12:00 p. m. a 4:00 p. m., hay combos de almuerzo con plato principal, papas andinas y bebida a elección: "
            f"el <strong>Combo Filete ({s('Combo Filete')})</strong> y los de bistec, chuleta, milanesa, suprema y hamburguesa ({s('Combo Bistec')}). "
            "Si prefieres algo ligero para seguir trabajando, hay sándwiches y ensaladas. Todo el detalle está en la guía de "
            "<a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">almuerzo en San Isidro</a>.</p>")},
        {"h2": "Algo dulce para la tarde", "html": (
            f"<p>Para el bajón de las cuatro: un <strong>alfajor ({s('Alfajor')})</strong> con el café, o un combo de la Dulce Pausa, como el "
            f"<strong>Pie de limón + Café Americano ({s('Pie de limón + Café Americano')})</strong>. "
            "La carta dulce completa está en <a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres en San Isidro</a>.</p>"),
         "fotos": [foto('Alfajor'), foto('Pie de limón + Café Americano')]},
        {"h2": "Consejos para trabajar en una cafetería", "html": (
            "<ul><li><strong>Llega con la batería cargada</strong> y lleva tu cargador: así eliges la mesa que más te guste sin depender de nada.</li>"
            "<li><strong>Usa audífonos</strong> en las llamadas, por ti y por la mesa de al lado.</li>"
            "<li><strong>Pide algo cada cierto tiempo</strong> si te quedas muchas horas: es la forma justa de usar el espacio.</li>"
            "<li><strong>Elige bien la hora.</strong> Según nuestras ventas, lo más concurrido es de 1 a 2 p. m. (almuerzo) y de 5 a 8 p. m.; las mañanas, de 9 a 12, son las más tranquilas para concentrarte.</li></ul>"
            "<p>¿Vienes a estudiar? Mira también la guía para <a href=\"/blog/estudiar-con-cafe-en-cafeteria-san-isidro\">estudiar con café en San Isidro</a>.</p>")},
        {"h2": "Cómo llegar", "html": (
            "<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado y cerca del centro financiero. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Abre la ubicación en Google Maps</a>. También somos pet friendly, por si trabajas acompañado.</p>")},
    ],
    "faq": [
        {"p": "¿Wasi Café tiene WiFi?", "r": "Sí, WiFi gratis para clientes."},
        {"p": "¿Hasta qué hora puedo quedarme a trabajar?", "r": "De lunes a viernes atendemos de 8:00 a. m. a 9:00 p. m. y los sábados de 9:00 a. m. a 9:00 p. m., de corrido. Los domingos está cerrado."},
        {"p": "¿Puedo almorzar ahí mismo?", "r": "Sí: de lunes a sábado, de 12 a 4 p. m., hay combos de almuerzo desde S/ 25.90, además de sándwiches y ensaladas."},
        {"p": "¿Dan factura?", "r": "Sí, emitimos boleta o factura electrónica."},
    ],
    "relacionados": ["estudiar-con-cafe-en-cafeteria-san-isidro", "reuniones-de-trabajo-en-cafeteria-san-isidro", "cafe-y-productividad-como-trabajar-mejor-con-cafe"],
})

for nombre, datos in (('almuerzo.json', almuerzo), ('mejoras.json', mejoras)):
    json.dump(datos, open(AQUI / nombre, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
txt = json.dumps(almuerzo + mejoras, ensure_ascii=False)
print(len(almuerzo + mejoras), 'fichas | guiones largos:', txt.count('—'))
