"""Tercera ola de guías del blog de Wasi Café (28/10/2026).

Mismas reglas que las olas anteriores: precios, descripciones y fotos de la carta
del POS (carta-wasi.json); horario, paquetes de eventos, sellos y curso tal como
los dice la portada (index.html) y curso.html; «lo más pedido» y horas de más
movimiento de las ventas reales de 60 días. Nada que no conste.
Uso: python3 fichas_ola3.py  → escribe ola3.json
"""
import json, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-28'
MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
WA = 'https://wa.me/51908724496'
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


def donde(extra=''):
    return {"h2": "Dónde estamos", "html": (
        f"<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado. "
        f"Atendemos {HORARIO}. {extra}"
        f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>. "
        "Si es tu primera vez, la guía de <a href=\"/blog/cafeteria-en-san-isidro-horario-como-llegar\">horario y cómo llegar</a> "
        "te cuenta todo lo práctico: pagos, pedido desde la mesa por QR y reservas.</p>")}


fichas = []

# ------------------------------------------------------------ 1. Jugos y batidos
fichas.append({
    "slug": "jugos-y-batidos-en-san-isidro-precios",
    "tituloSeo": "Jugos y batidos en San Isidro: carta y precios | Wasi Café",
    "h1": "Jugos naturales, batidos y frozen en San Isidro: la carta de Wasi Café con precios",
    "tituloCorto": "Jugos y batidos en San Isidro",
    "ogTitulo": "Jugos, batidos y frozen en San Isidro, con precios",
    "descripcion": "Jugos naturales, batidos con leche y frozen en San Isidro con precios reales: papaya, surtido, lúcuma, maracuyá y más en Wasi Café, cerca de Javier Prado.",
    "eyebrow": "jugos en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Jugos naturales", "Batidos", "San Isidro"],
    "intro": (
        "<p>En Lima, un jugo bien hecho es casi un desayuno en sí mismo. En <strong>Wasi Café</strong>, en San Isidro, tenemos tres familias de bebidas de fruta: "
        "<strong>jugos naturales</strong>, <strong>batidos con leche</strong> y <strong>frozen</strong>, que son granizados de fruta. "
        "Aquí está la carta completa con precios, para que elijas antes de llegar.</p>"
        "<p>Los precios son los de nuestra <a href=\"/carta\">carta en línea</a>, que se actualiza sola desde la caja.</p>"),
    "secciones": [
        {"h2": "Jugos naturales", "html": (
            lista('Jugo de Papaya', 'Jugo de Piña', 'Jugo Surtido', 'Jugo de Naranja', 'Jugo de Fresa', 'Jugo de Mango', 'Jugo Especial')
            + "<p>Los más pedidos por nuestros clientes son, en ese orden, el de <strong>papaya</strong>, el <strong>surtido</strong>, el de "
            "<strong>piña</strong> y el de <strong>naranja</strong>. El <strong>Jugo Especial</strong>, con algarrobina, es el más contundente: "
            "casi una comida.</p>"
            "<p>El jugo de papaya o de piña también viene incluido en varios combos de desayuno, como el Continental o el Desayuno Americano. "
            "Mira la guía de <a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>"),
         "fotos": [foto('Jugo de Papaya'), foto('Jugo Surtido'), foto('Jugo de Naranja'), foto('Jugo Especial')]},
        {"h2": "Batidos con leche", "html": (
            lista('Fresa con Leche', 'Lúcuma con Leche', 'Plátano con Leche', 'Papaya con Leche', 'Piña con Leche', 'Mango con Leche', 'Palta con Leche')
            + "<p>Si vienes de fuera de Lima o del extranjero, prueba el de <strong>lúcuma</strong>: es una fruta peruana de sabor parecido al caramelo, "
            "que es difícil de encontrar fresca fuera del Perú. El de <strong>palta con leche</strong> también es muy nuestro, aunque suene raro la primera vez.</p>"),
         "fotos": [foto('Fresa con Leche'), foto('Lúcuma con Leche'), foto('Plátano con Leche'), foto('Palta con Leche')]},
        {"h2": "Frozen: granizados de fruta", "html": (
            lista('Frozen Lúcuma', 'Frozen Chicha Morada', 'Frozen Fresa', 'Frozen Mango', 'Frozen Maracuyá', 'Frozen Limón',
                  'Frozen Piña', 'Frozen Naranja', 'Frozen Tuti Fruti', 'Frozen Jamaica', 'Frozen Zanahoria con Limón')
            + "<p>Para los días de calor en Lima, de diciembre a abril, el frozen es lo más refrescante de la carta. El de "
            "<strong>chicha morada</strong> lleva el sabor del maíz morado, y el de <strong>maracuyá</strong> es para quien le gusta lo ácido.</p>"),
         "fotos": [foto('Frozen Lúcuma'), foto('Frozen Chicha Morada'), foto('Frozen Maracuyá'), foto('Frozen Mango')]},
        {"h2": "Bebidas frías clásicas", "html": (
            lista('Chicha Morada', 'Limonada', 'Maracuyá', 'Milk Shake')
            + "<p>La <strong>chicha morada</strong> es la bebida peruana de maíz morado de toda la vida, y combina muy bien con un sándwich de chicharrón. "
            "La <strong>limonada</strong> es natural, con limón peruano.</p>"),
         "fotos": [foto('Chicha Morada'), foto('Limonada'), foto('Milk Shake')]},
        {"h2": "Cómo elegir según el momento", "html": (
            "<ul><li><strong>En el desayuno:</strong> un jugo de papaya o de naranja, más ligeros.</li>"
            "<li><strong>Después de entrenar o si no desayunaste:</strong> un batido de plátano o el Jugo Especial, que llenan.</li>"
            "<li><strong>A media tarde y con calor:</strong> un frozen de maracuyá, limón o chicha morada.</li>"
            "<li><strong>Para acompañar el almuerzo:</strong> chicha morada o limonada. En los combos de almuerzo la bebida ya viene incluida.</li></ul>"
            "<p>Si quieres saber más sobre las frutas, lee <a href=\"/blog/jugos-naturales-beneficios-como-elegir\">jugos naturales: beneficios y cómo elegir</a>.</p>")},
        donde("Todas las bebidas se pueden pedir para llevar. "),
    ],
    "faq": [
        {"p": "¿Cuál es el jugo más pedido en Wasi Café?", "r": "El jugo de papaya, seguido del surtido, el de piña y el de naranja."},
        {"p": "¿Cuánto cuesta un jugo natural?", "r": f"Desde {s('Jugo de Papaya')} el de papaya o piña; el Jugo Especial cuesta {s('Jugo Especial')}."},
        {"p": "¿Qué es un frozen?", "r": "Un granizado de fruta licuada con hielo. Hay 11 sabores, desde S/ 16.90."},
        {"p": "¿Tienen batido de lúcuma?", "r": f"Sí, la lúcuma con leche cuesta {s('Lúcuma con Leche')}, y también hay frozen de lúcuma."},
    ],
    "relacionados": ["jugos-naturales-beneficios-como-elegir", "desayunos-en-san-isidro-carta-precios-horario", "mejores-bebidas-frias-de-cafe-verano-lima"],
})

# ------------------------------------------------------------ 2. Frappés y café helado
fichas.append({
    "slug": "frappes-y-cafe-helado-en-san-isidro",
    "tituloSeo": "Frappé y café helado en San Isidro: precios | Wasi Café",
    "h1": "Frappés y café helado en San Isidro: tamaños, sabores y precios en Wasi Café",
    "tituloCorto": "Frappés en San Isidro",
    "ogTitulo": "Frappés y café helado en San Isidro, con precios",
    "descripcion": "Frappés en San Isidro desde S/ 15.90 en tamaño mediano o grande: café, moca, caramelo y chocolate, más café helado, iced latte y affogato en Wasi Café.",
    "eyebrow": "frappés en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Frappé", "Café helado", "San Isidro"],
    "intro": (
        "<p>Cuando aprieta el calor en Lima, el café caliente le cede el turno al frío. En <strong>Wasi Café</strong>, en San Isidro, hay frappés en dos tamaños, "
        f"café helado, iced latte y affogato, todos hechos con nuestro café de especialidad 100 % peruano de {ORIGEN}. "
        "Esta es la carta completa con precios.</p>"),
    "secciones": [
        {"h2": "Frappés en tamaño mediano y grande", "html": (
            "<p>Cuatro sabores, cada uno en tamaño mediano o grande:</p>"
            "<table style=\"width:100%;border-collapse:collapse;margin:1rem 0 1.4rem\">"
            "<tr><th style=\"text-align:left;padding:.5rem 0;border-bottom:1px solid var(--line)\">Sabor</th>"
            "<th style=\"text-align:right;padding:.5rem 0;border-bottom:1px solid var(--line)\">Mediano</th>"
            "<th style=\"text-align:right;padding:.5rem 0;border-bottom:1px solid var(--line)\">Grande</th></tr>"
            + ''.join(f"<tr><td style=\"padding:.5rem 0;border-bottom:1px solid var(--line)\">{n}</td>"
                      f"<td style=\"padding:.5rem 0;border-bottom:1px solid var(--line);text-align:right\">{s('Frappé de ' + n + ' mediano')}</td>"
                      f"<td style=\"padding:.5rem 0;border-bottom:1px solid var(--line);text-align:right\">{s('Frappé de ' + n + ' Grande')}</td></tr>"
                      for n in ('Café', 'Moca', 'Caramelo', 'Chocolate'))
            + "</table><p>El más pedido es el <strong>frappé de moca mediano</strong>: café, chocolate y hielo, en el punto justo entre dulce y cafetero. "
            "Si quieres sentir más el café, pide el de café; si buscas algo más de postre, el de caramelo.</p>")},
        {"h2": "Café helado e iced latte", "html": (
            lista('Café Helado', 'Café con Leche Helado', 'Chocolate Helado', 'Tepuchino Helado')
            + "<p>La diferencia con el frappé: el café helado no se licúa con hielo, así que el sabor del café se siente más limpio. "
            "El <strong>iced latte</strong> (café con leche helado) es el punto medio para quien quiere algo frío pero suave.</p>"),
         "fotos": [foto('Café Helado'), foto('Café con Leche Helado'), foto('Chocolate Helado'), foto('Tepuchino Helado')]},
        {"h2": "Affogato: café caliente sobre helado", "html": (
            lista('Affogato Clásico', 'Affogato Wasi + Pisco')
            + "<p>El affogato es un postre italiano: un espresso recién hecho que se vierte sobre una bola de helado de vainilla. "
            "El nuestro, con media onza de pisco, es una de las recetas de la casa.</p>"),
         "fotos": [foto('Affogato Clásico'), foto('Affogato Wasi + Pisco')]},
        {"h2": "Milk shake y opciones sin café", "html": (
            lista('Milk Shake', 'Frozen Lúcuma', 'Frozen Maracuyá')
            + "<p>Si no tomas café, el <strong>milk shake</strong> de helado artesanal o un <strong>frozen</strong> de fruta son la alternativa. "
            "Hay 11 sabores de frozen en la guía de <a href=\"/blog/jugos-y-batidos-en-san-isidro-precios\">jugos y batidos en San Isidro</a>.</p>"),
         "fotos": [foto('Milk Shake'), foto('Frozen Lúcuma'), foto('Frozen Maracuyá')]},
        {"h2": "Qué pedir según lo que te gusta", "html": (
            "<ul><li><strong>Te gusta el café fuerte:</strong> café helado o affogato clásico.</li>"
            "<li><strong>Te gusta suave y cremoso:</strong> iced latte o frappé de café.</li>"
            "<li><strong>Quieres algo de postre:</strong> frappé de moca, de caramelo o de chocolate.</li>"
            "<li><strong>Vienes con amigos al final de la tarde:</strong> affogato Wasi con pisco.</li></ul>"
            "<p>Para prepararlo en casa, mira <a href=\"/blog/como-preparar-cold-brew-en-casa\">cómo hacer cold brew</a> y las "
            "<a href=\"/blog/mejores-bebidas-frias-de-cafe-verano-lima\">mejores bebidas frías de café para el verano</a>.</p>")},
        donde("Todas las bebidas frías se pueden pedir para llevar. "),
    ],
    "faq": [
        {"p": "¿Cuánto cuesta un frappé en Wasi Café?", "r": "Desde S/ 15.90 el mediano y desde S/ 22.90 el grande, según el sabor."},
        {"p": "¿Qué sabores de frappé hay?", "r": "Café, moca, caramelo y chocolate, en tamaño mediano o grande."},
        {"p": "¿Cuál es la diferencia entre frappé y café helado?", "r": "El frappé se licúa con hielo y queda cremoso; el café helado es café con hielo, sin licuar, y se siente más el café."},
        {"p": "¿Qué es el affogato?", "r": "Un espresso caliente servido sobre helado de vainilla. En Wasi también hay una versión con media onza de pisco."},
    ],
    "relacionados": ["mejores-bebidas-frias-de-cafe-verano-lima", "como-preparar-cold-brew-en-casa", "cafe-de-especialidad-san-isidro-guia"],
})

# ------------------------------------------------------------ 3. Pisco sour y after office
fichas.append({
    "slug": "pisco-sour-y-after-office-en-san-isidro",
    "tituloSeo": "Pisco sour y after office en San Isidro | Wasi Café",
    "h1": "Pisco sour y after office en San Isidro: cócteles, affogato con pisco y algo para picar",
    "tituloCorto": "Pisco sour en San Isidro",
    "ogTitulo": "After office en San Isidro: pisco sour en Wasi Café",
    "descripcion": "After office en San Isidro hasta las 9 p. m.: pisco sour, piña colada, vino de verano y affogato con pisco desde S/ 17.90, con empanadas y algo para picar.",
    "eyebrow": "after office en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Pisco sour", "After office", "San Isidro"],
    "intro": (
        "<p>Salir de la oficina en San Isidro y no querer ir lejos es de lo más normal. <strong>Wasi Café</strong> está a pasos de la avenida Javier Prado "
        "y atiende hasta las <strong>9:00 p. m.</strong> de lunes a sábado. Además del café, la carta tiene algunos cócteles, entre ellos el "
        "<strong>pisco sour</strong>, y cosas para picar. Esta es la guía, con precios reales.</p>"),
    "secciones": [
        {"h2": "Los cócteles de la carta", "html": (
            lista('Pisco Sour', 'Piña Colada', 'Vino Tinto de Verano')
            + "<p>El <strong>pisco sour</strong> es el cóctel bandera del Perú: pisco, limón, jarabe y clara de huevo batida, con su espuma encima. "
            "Si vienes con alguien de visita en Lima, es el que hay que probar.</p>"),
         "fotos": [foto('Pisco Sour'), foto('Piña Colada'), foto('Vino Tinto de Verano')]},
        {"h2": "El affogato con pisco, una receta de la casa", "html": (
            f"<p>El <strong>Affogato Wasi + Pisco ({s('Affogato Wasi + Pisco')})</strong> junta lo mejor de una cafetería y de una sobremesa: "
            "espresso caliente sobre helado, con media onza de pisco. Es postre y bajativo a la vez, y uno de los favoritos para cerrar la tarde.</p>"
            f"<p>Si prefieres sin alcohol, el <strong>Affogato Clásico ({s('Affogato Clásico')})</strong> es la misma idea, solo café y helado.</p>"),
         "fotos": [foto('Affogato Wasi + Pisco'), foto('Affogato Clásico')]},
        {"h2": "Para picar", "html": (
            lista('Empanada de Carne', 'Empanada de Pollo', 'Salchipapa Especial', 'Pan al Ajo', 'Papas Andinas', 'Camote Frito')
            + "<p>Para un grupo, la <strong>salchipapa especial</strong> y unas papas andinas al centro de la mesa funcionan siempre. "
            "Si hay hambre de verdad, la carta de <a href=\"/blog/sandwiches-peruanos-y-hamburguesas-san-isidro\">sándwiches y hamburguesas</a> sigue disponible.</p>"),
         "fotos": [foto('Empanada de Carne'), foto('Salchipapa Especial'), foto('Pan al Ajo'), foto('Papas Andinas')]},
        {"h2": "A qué hora conviene ir", "html": (
            "<p>Según nuestras ventas, <strong>de 5:00 a 8:00 p. m.</strong> es el momento de más movimiento del día, junto con la hora del almuerzo. "
            "Es la hora de salida de las oficinas de la zona.</p>"
            "<p>Si vienen varios, aparta mesa desde la <a href=\"/#reservar\">web</a>: eliges día, hora y número de personas, y te confirmamos por WhatsApp. "
            "Cerramos a las 9:00 p. m., así que es un plan de after office temprano, no de noche larga.</p>")},
        {"h2": "Si alguien del grupo no toma alcohol", "html": (
            "<p>Nadie se queda fuera: hay <a href=\"/blog/frappes-y-cafe-helado-en-san-isidro\">frappés y café helado</a>, "
            "<a href=\"/blog/jugos-y-batidos-en-san-isidro-precios\">jugos, batidos y frozen</a>, chicha morada, limonada y, por supuesto, "
            f"café de especialidad de {ORIGEN}.</p>"
            "<p>Y para los dulces, la vitrina tiene tortas, pies y helados: la guía de <a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres en San Isidro</a> los tiene todos con precio.</p>")},
        donde("Aceptamos efectivo, tarjeta, Yape y Plin, y emitimos boleta o factura. "),
    ],
    "faq": [
        {"p": "¿Wasi Café vende pisco sour?", "r": f"Sí, el pisco sour cuesta {s('Pisco Sour')}. También hay piña colada y vino tinto de verano."},
        {"p": "¿Hasta qué hora atiende Wasi Café?", "r": "Hasta las 9:00 p. m. de lunes a sábado. Los domingos está cerrado."},
        {"p": "¿Qué hay para picar?", "r": "Empanadas, salchipapa, pan al ajo, papas andinas y camote frito, además de toda la carta de sándwiches."},
        {"p": "¿Se puede reservar para un grupo?", "r": "Sí, desde la web: eliges día, hora y personas, y te confirman por WhatsApp."},
    ],
    "relacionados": ["salir-con-amigos-a-una-cafeteria-san-isidro", "reuniones-de-trabajo-en-cafeteria-san-isidro", "postres-artesanales-cafeteria-san-isidro"],
})

# ------------------------------------------------------------ 4. Infusiones y chocolate
fichas.append({
    "slug": "infusiones-te-y-chocolate-caliente-san-isidro",
    "tituloSeo": "Infusiones, té y chocolate caliente en San Isidro | Wasi Café",
    "h1": "Si no tomas café: infusiones, té y chocolate caliente en San Isidro",
    "tituloCorto": "Infusiones y chocolate caliente",
    "ogTitulo": "Infusiones, té y chocolate caliente en San Isidro",
    "descripcion": "Qué pedir en una cafetería de San Isidro si no tomas café: infusiones a S/ 11, chocolate caliente artesanal, tepuchino y té helado en Wasi Café.",
    "eyebrow": "sin café en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Infusiones", "Chocolate caliente", "San Isidro"],
    "intro": (
        "<p>No a todo el mundo le cae bien el café, y no por eso hay que quedarse fuera del plan. En <strong>Wasi Café</strong>, en San Isidro, hay infusiones, "
        "té, chocolate caliente artesanal y una bebida propia, el <strong>tepuchino</strong>. Esta es la carta para quien viene acompañando o simplemente "
        "prefiere algo sin cafeína.</p>"),
    "secciones": [
        {"h2": "Infusiones a S/ 11", "html": (
            lista('Manzanilla', 'Anís', 'Hierba Luisa', 'Hierba Buena', 'Té', 'Jamaica')
            + "<p>La <strong>manzanilla</strong> y el <strong>anís</strong> son las clásicas para después de comer. La <strong>hierba luisa</strong> es muy limeña y "
            "aromática, y la <strong>jamaica</strong> se sirve helada, ideal en verano.</p>"),
         "fotos": [foto('Manzanilla'), foto('Anís'), foto('Hierba Luisa'), foto('Jamaica')]},
        {"h2": "Chocolate caliente", "html": (
            f"<p>El <strong>Chocolate Caliente ({s('Chocolate Caliente')})</strong> es de chocolate artesanal peruano, espeso y para tomar con calma. "
            "Está entre lo más pedido de la casa, y en los días grises del invierno limeño, de junio a septiembre, se entiende por qué.</p>"
            f"<p>Combínalo con un croissant de mantequilla ({s('Croissant')}) o, si es tarde de antojo, con el combo "
            f"<strong>Chocolate Caliente + Croissant ({s('Chocolate Caliente + Croissant')})</strong>. En verano está el "
            f"<strong>Chocolate Helado ({s('Chocolate Helado')})</strong>.</p>"),
         "fotos": [foto('Chocolate Caliente'), foto('Croissant'), foto('Chocolate Helado')]},
        {"h2": "Tepuchino: nuestra bebida de té", "html": (
            f"<p>El <strong>Tepuchino ({s('Tepuchino')})</strong> es una creación de la casa: té con espuma, servido como si fuera un capuchino. "
            "Tiene la textura cremosa del café con leche, pero sin café. "
            f"Hay versión helada, el <strong>Tepuchino Helado ({s('Tepuchino Helado')})</strong>.</p>"),
         "fotos": [foto('Tepuchino'), foto('Tepuchino Helado')]},
        {"h2": "Qué infusión elegir según el momento", "html": (
            "<ul><li><strong>Después de almorzar:</strong> anís o manzanilla. En la carta el anís figura como digestivo y la manzanilla como calmante.</li>"
            "<li><strong>A media tarde:</strong> hierba luisa, aromática y suave, o un té clásico.</li>"
            "<li><strong>Si quieres algo fresco:</strong> hierba buena, o la jamaica, que se sirve helada.</li>"
            "<li><strong>Si hace frío y hay antojo:</strong> chocolate caliente con un croissant.</li></ul>"
            "<p>Las infusiones también acompañan muy bien un postre de la vitrina: un pie de limón con hierba luisa, o una crema volteada con manzanilla, "
            "son combinaciones ligeras para cerrar una comida.</p>")},
        {"h2": "Bebidas frías sin cafeína", "html": (
            lista('Chicha Morada', 'Limonada', 'Fresa con Leche', 'Frozen Lúcuma')
            + "<p>Toda la carta de fruta está en la guía de <a href=\"/blog/jugos-y-batidos-en-san-isidro-precios\">jugos, batidos y frozen en San Isidro</a>.</p>"),
         "fotos": [foto('Chicha Morada'), foto('Limonada'), foto('Fresa con Leche')]},
        {"h2": "Para quien sí quiere un poco de café", "html": (
            "<p>Si la idea es tomar menos cafeína pero no dejar el café del todo, un <strong>cortado</strong> o un <strong>café con leche</strong> "
            "tienen menos café por taza que un americano grande. También puedes leer "
            "<a href=\"/blog/cafeina-y-sueno-a-que-hora-el-ultimo-cafe\">a qué hora tomar el último café</a> para no dormir mal.</p>"
            f"<p>Todo nuestro café es de especialidad, 100 % peruano, de {ORIGEN}.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Qué infusiones tiene Wasi Café?", "r": "Manzanilla, anís, hierba luisa, hierba buena, té y jamaica, a S/ 11 cada una."},
        {"p": "¿El chocolate caliente es artesanal?", "r": f"Sí, de chocolate artesanal peruano. Cuesta {s('Chocolate Caliente')}."},
        {"p": "¿Qué es el tepuchino?", "r": "Una bebida de la casa: té con espuma de leche, servido como un capuchino pero sin café."},
    ],
    "relacionados": ["cafeina-y-sueno-a-que-hora-el-ultimo-cafe", "postres-artesanales-cafeteria-san-isidro", "leche-de-avena-y-vegetales-para-cafe"],
})

# ------------------------------------------------------------ 5. Desayuno criollo
fichas.append({
    "slug": "desayuno-criollo-pan-con-chicharron-y-tamal-san-isidro",
    "tituloSeo": "Pan con chicharrón y tamal en San Isidro | Wasi Café",
    "h1": "Desayuno criollo en San Isidro: pan con chicharrón, tamal y butifarra, con precios",
    "tituloCorto": "Desayuno criollo en San Isidro",
    "ogTitulo": "Pan con chicharrón y tamal en San Isidro: desayuno criollo",
    "descripcion": "Desayuno criollo en San Isidro: pan con chicharrón, tamal con salsa criolla, butifarra y el combo Tradición Wasi para dos, con precios reales.",
    "eyebrow": "desayuno criollo",
    "fecha": HOY, "modificado": HOY,
    "about": ["Desayuno criollo", "Pan con chicharrón", "San Isidro"],
    "intro": (
        "<p>El desayuno limeño de fin de semana tiene nombre propio: pan con chicharrón, tamal, salsa criolla y un café. En <strong>Wasi Café</strong>, "
        "en San Isidro, lo servimos todos los días que abrimos, desde las 8:00 a. m. de lunes a viernes y desde las 9:00 a. m. los sábados. "
        "Aquí están las opciones con precio.</p>"),
    "secciones": [
        {"h2": "Pan con chicharrón", "html": (
            f"<p>El <strong>sándwich de Chicharrón ({s('Chicharrón')})</strong> lleva pan con chicharrón, camote frito y salsa criolla, como debe ser. "
            f"Si lo quieres con café, el combo <strong>Amanecer Criollo ({s('Amanecer Criollo')})</strong> trae un café americano y el sándwich de chicharrón.</p>"),
         "fotos": [foto('Chicharrón'), foto('Camote Frito'), foto('Ensalada Criolla')]},
        {"h2": "Tamal", "html": (
            f"<p>El <strong>Tamal Criollo ({s('Tamal Criollo')})</strong> se sirve con salsa criolla en pan francés. Para desayunar completo, el "
            f"<strong>Desayuno Tamalero ({s('Desayuno Tamalero')})</strong> incluye café (americano, espresso o con leche), tamal, pan francés y salsa criolla.</p>"),
         "fotos": [foto('Tamal Criollo')]},
        {"h2": "Butifarra y sándwich de asado", "html": (
            lista('Butifarra', 'Sándwich de Asado')
            + "<p>La <strong>butifarra</strong> es el sándwich de jamón del país con salsa criolla, otro clásico limeño. El de asado es más contundente, "
            "con carne de res en pan artesanal.</p>"),
         "fotos": [foto('Butifarra'), foto('Sándwich de Asado')]},
        {"h2": "Tradición Wasi: el desayuno criollo para dos", "html": (
            f"<p>El combo <strong>Tradición Wasi ({s('Tradición Wasi')})</strong> está pensado para compartir. Trae:</p><ul>"
            "<li>2 cafés (americano o café con leche) y 2 jugos (papaya o piña).</li>"
            "<li>250 g de chicharrón y 1 tamal de pollo.</li>"
            "<li>100 g de salchicha huachana y 4 panes franceses.</li>"
            "<li>Camote frito y salsa criolla.</li></ul>"
            "<p>Es la mesa de desayuno de sábado en casa, pero sin tener que cocinar. Si vienen más de dos, se puede pedir uno y sumar sándwiches sueltos.</p>")},
        {"h2": "Qué tomar con el desayuno criollo", "html": (
            f"<p>Lo clásico es un <strong>café americano ({s('Americano')})</strong> o un <strong>café con leche ({s('Café con Leche')})</strong>. "
            f"Si prefieres algo frío, la <strong>chicha morada ({s('Chicha Morada')})</strong> va perfecto con el chicharrón. "
            f"Nuestro café es de especialidad, 100 % peruano, de {ORIGEN}.</p>"
            "<p>Todos los combos de desayuno, los criollos y los demás, están en la guía de "
            "<a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>")},
        {"h2": "Un detalle importante: los domingos cerramos", "html": (
            "<p>Sabemos que el pan con chicharrón es plan de domingo en muchas casas limeñas, pero <strong>Wasi Café no abre los domingos</strong>. "
            "El sábado, desde las 9:00 a. m., es el mejor día para un desayuno criollo largo y sin apuro.</p>")},
        donde("Todo se puede pedir para llevar. "),
    ],
    "faq": [
        {"p": "¿Cuánto cuesta el pan con chicharrón en Wasi Café?", "r": f"El sándwich de chicharrón cuesta {s('Chicharrón')}; con café americano, en el combo Amanecer Criollo, {s('Amanecer Criollo')}."},
        {"p": "¿Tienen tamal?", "r": f"Sí, el Tamal Criollo cuesta {s('Tamal Criollo')}, y el Desayuno Tamalero con café, {s('Desayuno Tamalero')}."},
        {"p": "¿Hay desayuno criollo los domingos?", "r": "No, los domingos Wasi Café está cerrado. Los sábados abre desde las 9:00 a. m."},
        {"p": "¿Qué trae el Tradición Wasi?", "r": "2 cafés, 2 jugos, 250 g de chicharrón, 1 tamal de pollo, 100 g de salchicha huachana, 4 panes franceses, camote frito y salsa criolla."},
    ],
    "relacionados": ["desayunos-en-san-isidro-carta-precios-horario", "sandwiches-peruanos-y-hamburguesas-san-isidro", "donde-desayunar-cerca-de-el-olivar-san-isidro"],
})

# ------------------------------------------------------------ 6. Eventos y reservas
fichas.append({
    "slug": "eventos-y-cumpleanos-en-cafeteria-san-isidro",
    "tituloSeo": "Eventos, bodas y cumpleaños en San Isidro | Wasi Café",
    "h1": "Eventos, bodas pequeñas y cumpleaños en San Isidro: paquetes y reservas en Wasi Café",
    "tituloCorto": "Eventos y cumpleaños en San Isidro",
    "ogTitulo": "Celebra en Wasi Café: eventos y cumpleaños en San Isidro",
    "descripcion": "Bodas pequeñas, cumpleaños, baby showers y reuniones en San Isidro: local exclusivo para 20 a 30 personas y paquetes Café y Brunch en Wasi Café.",
    "eyebrow": "eventos en San Isidro",
    "fecha": HOY, "modificado": HOY,
    "about": ["Eventos", "Cumpleaños", "San Isidro"],
    "intro": (
        "<p>Una cafetería es un buen lugar para celebrar sin el ruido ni el precio de un restaurante grande. En <strong>Wasi Café</strong>, en San Isidro, "
        "organizamos <strong>cumpleaños, reuniones corporativas, baby showers</strong> y otras celebraciones, y también reservamos mesa para grupos. "
        "Esta guía explica los paquetes y cómo pedirlos.</p>"),
    "secciones": [
        {"h2": "Bodas y cumpleaños con el local exclusivo", "html": (
            "<p>Para <strong>bodas pequeñas y cumpleaños de 20 a 30 personas</strong>, Wasi Café queda <strong>solo para tu celebración</strong>, "
            "con <strong>decoración, comida y torta</strong>, cualquier día que coordinemos. Lo contamos a detalle en "
            "<a href=\"/blog/bodas-pequenas-en-san-isidro-local-para-20-a-30-personas\">bodas pequeñas en San Isidro</a> y en "
            "<a href=\"/blog/local-para-cumpleanos-en-san-isidro-20-a-30-personas\">local para cumpleaños en San Isidro</a>.</p>")},
        {"h2": "Los otros paquetes", "html": (
            "<ul><li><strong>Paquete Café:</strong> café de especialidad ilimitado y mesa de postres artesanales para todos los invitados.</li>"
            "<li><strong>Paquete Brunch:</strong> sándwiches, jugos naturales, café y postres. Ideal para reuniones de 10 personas o más.</li>"
            "<li><strong>Paquete Cumpleaños:</strong> decoración temática, torta personalizada, bocaditos y bebidas para el festejado y sus invitados.</li></ul>"
            f"<p>Cada evento se cotiza según el número de personas y lo que necesites. Escríbenos por <a href=\"{WA}\" target=\"_blank\" rel=\"noopener\">WhatsApp</a> "
            "con la fecha, la hora y cuántos serán, y te enviamos la propuesta.</p>")},
        {"h2": "Qué se sirve: la carta real", "html": (
            "<p>Lo que se sirve en los eventos sale de nuestra cocina y nuestra barra de todos los días. Algunos de los más pedidos:</p>"
            + lista('Club Sandwich', 'Torta de Chocolate', 'Cheesecake de Frutos del Bosque', 'Empanada de Pollo')
            + f"<p>Y el café es de especialidad, 100 % peruano, de {ORIGEN}. Puedes revisar toda la <a href=\"/carta\">carta con precios</a> para armar tu idea.</p>"),
         "fotos": [foto('Club Sandwich'), foto('Torta de Chocolate'), foto('Cheesecake de Frutos del Bosque'), foto('Empanada de Pollo')]},
        {"h2": "Reuniones de empresa", "html": (
            "<p>Estamos a pasos de la avenida Javier Prado y del centro financiero, así que es práctico para desayunos de equipo, "
            "despedidas o reuniones con clientes. Emitimos <strong>factura electrónica</strong> a nombre de la empresa y aceptamos efectivo, tarjeta, Yape y Plin.</p>"
            "<p>Para reuniones pequeñas de trabajo, sin paquete, lee la guía de "
            "<a href=\"/blog/reuniones-de-trabajo-en-cafeteria-san-isidro\">reuniones de trabajo en San Isidro</a>.</p>")},
        {"h2": "Reservar mesa para un grupo", "html": (
            "<p>Si no necesitas un paquete y solo quieres asegurar mesa, la reserva se pide desde la <a href=\"/#reservar\">web</a>. Te pide:</p><ul>"
            "<li>Día y hora.</li><li>Número de personas.</li><li>Tu nombre y tu celular.</li>"
            "<li>Algo que debamos saber, por ejemplo si es un cumpleaños.</li></ul>"
            "<p>Te confirmamos por WhatsApp. Toma un minuto.</p>")},
        {"h2": "Cuándo conviene celebrar", "html": (
            f"<p>Atendemos {HORARIO}. Según nuestras ventas, las horas de más movimiento son de 1:00 a 2:00 p. m. y de 5:00 a 8:00 p. m.; "
            "si quieres un ambiente más tranquilo para tu evento, las mañanas y el inicio de la tarde son mejores. "
            "Para un brunch de celebración, el sábado es el día ideal: mira la guía de <a href=\"/blog/brunch-en-san-isidro-que-pedir-como-elegir\">brunch en San Isidro</a>.</p>")},
        {"h2": "Para llevar: tortas y postres", "html": (
            "<p>Si la celebración es en casa o en la oficina, todos los postres de la vitrina se pueden pedir para llevar. La carta dulce completa, con precios, "
            "está en <a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres en San Isidro</a>.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Wasi Café organiza cumpleaños?", "r": "Sí, con el Paquete Cumpleaños: decoración temática, torta personalizada, bocaditos y bebidas. Se cotiza por WhatsApp."},
        {"p": "¿Hay paquetes para empresas?", "r": "Sí, el Paquete Café y el Paquete Brunch funcionan bien para reuniones de empresa, y emitimos factura electrónica."},
        {"p": "¿Cómo reservo mesa para un grupo?", "r": "Desde la web, indicando día, hora, personas, nombre y celular. Te confirman por WhatsApp."},
        {"p": "¿Abren los domingos para eventos?", "r": "No, los domingos Wasi Café está cerrado."},
    ],
    "relacionados": ["reuniones-de-trabajo-en-cafeteria-san-isidro", "salir-con-amigos-a-una-cafeteria-san-isidro", "brunch-en-san-isidro-que-pedir-como-elegir"],
})

# ------------------------------------------------------------ 7. Tarjeta de sellos
fichas.append({
    "slug": "tarjeta-de-sellos-wasi-cafe-cafe-gratis",
    "tituloSeo": "Tarjeta de sellos de Wasi Café: tu café gratis | San Isidro",
    "h1": "La tarjeta de sellos de Wasi Café: cómo funciona y cómo ganar tu café gratis",
    "tituloCorto": "Tarjeta de sellos",
    "ogTitulo": "Tarjeta de sellos en el celular: café gratis en Wasi Café",
    "descripcion": "Cómo funciona la tarjeta de sellos de Wasi Café en San Isidro: cada café suma un sello, al completar 10 el siguiente es gratis, y se guarda en tu celular.",
    "eyebrow": "tarjeta de sellos",
    "fecha": HOY, "modificado": HOY,
    "about": ["Programa de fidelidad", "Tarjeta de sellos", "Wasi Café"],
    "intro": (
        "<p>Si vienes seguido a <strong>Wasi Café</strong>, en San Isidro, tu café número once puede salir gratis. La tarjeta de sellos vive en tu celular: "
        "no hay que descargar ninguna app ni guardar un cartón que se pierde en la billetera. Así funciona.</p>"),
    "secciones": [
        {"h2": "Cómo funciona", "html": (
            "<ul><li><strong>Cada café suma un sello.</strong></li>"
            "<li><strong>Al completar la tarjeta de 10 sellos</strong>, el siguiente café va por cuenta de la casa.</li>"
            "<li>Al pagar, das tu número de celular y el sello se suma solo.</li></ul>"
            "<p>Así de simple. No hay montos mínimos raros ni letra pequeña: tomas tu café, sumas tu sello.</p>")},
        {"h2": "Guárdala en tu celular", "html": (
            "<p>La tarjeta se guarda en <strong>Google Wallet</strong> (Android) o en <strong>Apple Wallet</strong> (iPhone), junto a tus tarjetas y entradas. "
            "Se actualiza sola cada vez que sumas un sello, así que siempre ves cuántos te faltan.</p>"
            "<p>Para verla o guardarla, entra a <a href=\"/sellos\">wasicafe.com/sellos</a> con tu número.</p>")},
        {"h2": "Qué café elegir para tu sello", "html": (
            "<p>Cualquiera de la barra cuenta. Algunos favoritos:</p>"
            + lista('Americano', 'Capuchino', 'Café con Leche', 'Cortado', 'Mocachino')
            + f"<p>El americano es el café que más servimos. Todo nuestro café es de especialidad, 100 % peruano, de {ORIGEN}. "
            "Si quieres entender las diferencias entre uno y otro, lee "
            "<a href=\"/blog/flat-white-cortado-y-capuccino-diferencias\">flat white, cortado y capuchino: diferencias</a>.</p>"),
         "fotos": [foto('Americano'), foto('Capuchino'), foto('Café con Leche'), foto('Cortado')]},
        {"h2": "Cuánto ahorras", "html": (
            f"<p>Con el americano a {s('Americano')}, completar la tarjeta te regala un café de ese valor por cada diez que tomes; con capuchino "
            f"({s('Capuchino')}), aún más. Para quien toma un café al día de lunes a viernes, es un café gratis cada dos semanas.</p>")},
        {"h2": "Otras formas de ahorrar en Wasi", "html": (
            "<p>Además de los sellos, varios combos de la carta salen más baratos que pedir todo por separado:</p><ul>"
            f"<li><strong>Combos de desayuno</strong> con café incluido, desde {s('Continental')} el Continental o el Dúo Café.</li>"
            f"<li><strong>Combos de almuerzo</strong> de lunes a sábado de 12 a 4, con plato, papas andinas y bebida, desde {s('Combo Filete')}.</li>"
            f"<li><strong>Dulce Pausa:</strong> postre y café americano juntos, como el Pie de limón + Café Americano ({s('Pie de limón + Café Americano')}).</li></ul>"
            "<p>Los detalles están en las guías de <a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos</a>, "
            "<a href=\"/blog/almuerzo-en-san-isidro-combos-y-precios\">almuerzo</a> y <a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres</a>.</p>")},
        {"h2": "Preguntas comunes", "html": (
            "<p><strong>¿Tengo que pagar algo para tener la tarjeta?</strong> No, es gratis.</p>"
            "<p><strong>¿Necesito una app?</strong> No. Se guarda en la billetera de tu celular.</p>"
            "<p><strong>¿Qué pasa si cambio de celular?</strong> La tarjeta va con tu número: entra a la página de sellos con tu número y vuelve a guardarla.</p>"
            "<p><strong>¿Los sellos se suman en cualquier compra?</strong> Se suma un sello por cada café.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Cuántos sellos necesito para el café gratis?", "r": "10 sellos. Al completar la tarjeta, el siguiente café va por cuenta de la casa."},
        {"p": "¿Dónde veo mis sellos?", "r": "En wasicafe.com/sellos con tu número, o en la tarjeta guardada en Google Wallet o Apple Wallet."},
        {"p": "¿La tarjeta tiene costo?", "r": "No, es gratis y no necesita ninguna app."},
    ],
    "relacionados": ["cafe-de-especialidad-san-isidro-guia", "flat-white-cortado-y-capuccino-diferencias", "ritual-matutino-de-cafe-como-empezar-el-dia"],
})

# ------------------------------------------------------------ 8. Curso de barista (mejora)
fichas.append({
    "slug": "curso-de-barista-en-lima-empezar-desde-cero",
    "tituloSeo": "Curso de barista en Lima: precio y temario | Wasi Café",
    "h1": "Curso de barista en Lima: precio, temario y cómo empezar desde cero en Wasi Café",
    "tituloCorto": "Curso de barista en Lima",
    "ogTitulo": "Curso de barista en Lima desde cero: precio y temario",
    "descripcion": "Curso de barista en Lima desde cero: S/ 300 al mes, 4 clases presenciales en San Isidro, materiales incluidos y certificación WasiBaristas.",
    "eyebrow": "curso de barista en Lima",
    "fecha": "2026-06-13", "modificado": HOY,
    "about": ["Curso de barista", "Lima", "Emprendimiento"],
    "intro": (
        "<p>Aprender a preparar café bien es un oficio, y en Lima también puede ser un negocio. En la Escuela del Café de <strong>Wasi Café</strong> "
        "(WasiBaristas), en San Isidro, el curso empieza desde cero: no necesitas experiencia ni una máquina de espresso en casa. "
        "Esta guía responde lo que todos preguntan: cuánto cuesta, qué se aprende y cómo inscribirse.</p>"),
    "secciones": [
        {"h2": "Precio y formato", "html": (
            "<ul><li><strong>Inversión:</strong> S/ 300 al mes.</li>"
            "<li><strong>Clases:</strong> 4 al mes, una por semana, presenciales en nuestra sede de San Isidro.</li>"
            "<li><strong>Materiales incluidos.</strong></li>"
            "<li><strong>Certificación WasiBaristas</strong> al terminar.</li></ul>"
            "<p>También hay modalidad <strong>online</strong>, para aprender a tu ritmo desde donde estés. "
            f"Para inscribirte o resolver dudas, escríbenos por <a href=\"{WA}\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>. "
            "Toda la información está en la página del <a href=\"/curso\">curso</a>.</p>")},
        {"h2": "Qué vas a aprender", "html": (
            "<p>El curso va del arte del café a la administración de un negocio. Estos son los temas del programa:</p><ul>"
            "<li><strong>Bebidas calientes sin máquina espresso:</strong> prensa francesa, V60, Chemex, moka y AeroPress; ratios de café y agua, "
            "temperatura y tiempo; espumado de leche sin vaporizador; recetas base como americano, café con leche y mocha.</li>"
            "<li><strong>Barismo para principiantes:</strong> la molienda y cómo ajustarla, cata básica (acidez, cuerpo, dulzor y defectos), "
            "rutina de dosificado y limpieza, y los primeros trazos de arte latte.</li>"
            "<li><strong>Aspectos legales y tributarios básicos:</strong> RUC y qué régimen conviene (NRUS, RER o MYPE), boletas y facturas electrónicas, "
            "licencia de funcionamiento y obligaciones mensuales ante SUNAT.</li>"
            "<li><strong>Cómo empezar con bajo presupuesto:</strong> el equipo mínimo para arrancar sin máquina espresso, dónde invertir primero, proveedores "
            "y control de merma, y modelos de arranque como carrito, barra pequeña o delivery.</li></ul>"
            "<p>En la versión presencial, además, se trabajan latte art, cata de café y postres artesanales.</p>")},
        {"h2": "Para quién es", "html": (
            "<ul><li>Para quien quiere <strong>trabajar como barista</strong> y empezar sin experiencia.</li>"
            "<li>Para quien sueña con <strong>abrir su propia cafetería</strong>, carrito o barra, y necesita entender también la parte legal y de costos.</li>"
            "<li>Para quien simplemente ama el café y quiere <strong>prepararlo mejor en casa</strong>.</li></ul>"
            "<p>Nuestro lema lo resume: <strong>«Un café, una oportunidad.»</strong></p>")},
        {"h2": "Cómo es una clase", "html": (
            "<p>Las clases presenciales son en la misma cafetería, en Luis Felipe Villarán 904, San Isidro, con práctica real y acompañamiento personalizado. "
            f"Wasi trabaja con café de especialidad 100 % peruano, de {ORIGEN}.</p>"
            "<p>Antes de la primera clase puedes adelantar lectura con nuestras guías: "
            "<a href=\"/blog/como-reconocer-un-buen-espresso\">cómo reconocer un buen espresso</a>, "
            "<a href=\"/blog/metodos-de-filtrado-v60-chemex-aeropress-prensa-francesa\">métodos de filtrado</a> y "
            "<a href=\"/blog/molienda-del-cafe-guia-por-metodo\">la molienda según el método</a>.</p>")},
        {"h2": "Cómo inscribirte", "html": (
            f"<p>Escríbenos por <a href=\"{WA}\" target=\"_blank\" rel=\"noopener\">WhatsApp al +51 908 724 496</a> diciendo si prefieres presencial u online, "
            "y te contamos las fechas del próximo grupo. Si quieres conocer el lugar antes, ven a tomar un café: atendemos "
            f"{HORARIO}.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Cuánto cuesta el curso de barista en Wasi Café?", "r": "S/ 300 al mes, por 4 clases presenciales (una por semana), con materiales incluidos."},
        {"p": "¿Necesito experiencia previa?", "r": "No, el curso empieza desde cero."},
        {"p": "¿Dan certificado?", "r": "Sí, la certificación WasiBaristas al terminar."},
        {"p": "¿Hay curso online?", "r": "Sí, además de los talleres presenciales en San Isidro hay modalidad online."},
        {"p": "¿Dónde son las clases presenciales?", "r": "En Wasi Café, Luis Felipe Villarán 904, San Isidro, Lima."},
    ],
    "relacionados": ["como-reconocer-un-buen-espresso", "metodos-de-filtrado-v60-chemex-aeropress-prensa-francesa", "ferias-y-campeonatos-de-baristas-en-peru-guia"],
})

json.dump(fichas, open(AQUI / 'ola3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
txt = json.dumps(fichas, ensure_ascii=False)
print(len(fichas), 'fichas | guiones largos:', txt.count('—'))
