"""Quinta ola (28/10/2026): tres artículos viejos y genéricos reescritos con datos reales:
embajadas y hoteles, desayunar cerca de El Olivar, y pet friendly.
Distancia a El Olivar: ~0,9 km en línea recta desde las coordenadas del local
(-12.10158, -77.02894) al centro del bosque; se dice «menos de un kilómetro».
Uso: python3 fichas_ola5.py  → escribe ola5.json
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


def donde(extra=''):
    return {"h2": "Dónde estamos", "html": (
        f"<p>Wasi Café está en <strong>Luis Felipe Villarán 904, San Isidro</strong>, a pasos de la avenida Javier Prado. Atendemos {HORARIO}. {extra}"
        f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver en Google Maps</a>.</p>")}


fichas = []

# ------------------------------------------------------------ Embajadas y hoteles
fichas.append({
    "slug": "cafe-cerca-de-embajadas-y-hoteles-san-isidro",
    "tituloSeo": "Café cerca de embajadas y hoteles en San Isidro | Wasi Café",
    "h1": "Café cerca de embajadas y hoteles de San Isidro: qué pedir, cómo pagar y horario",
    "tituloCorto": "Café cerca de embajadas y hoteles",
    "ogTitulo": "Café de especialidad cerca de embajadas y hoteles de San Isidro",
    "descripcion": "Café de especialidad en San Isidro para visitantes, diplomáticos y huéspedes de hotel: horario, pago con tarjeta, carta en inglés y qué probar en Wasi Café.",
    "eyebrow": "visitantes en San Isidro",
    "fecha": "2026-06-15", "modificado": HOY,
    "about": ["Café de especialidad", "San Isidro", "Visitantes"],
    "intro": (
        "<p>San Isidro concentra buena parte de las embajadas, hoteles y oficinas internacionales de Lima. Si estás de paso, alojado en la zona o trabajando "
        "en una misión, <strong>Wasi Café</strong>, en Luis Felipe Villarán 904, es una cafetería de especialidad a pasos de la avenida Javier Prado. "
        "Esta guía responde lo práctico: cuándo abre, cómo se paga y qué vale la pena probar.</p>"
        "<p><strong>In English:</strong> read our <a href=\"/blog/coffee-shop-in-san-isidro-lima-wasi-cafe\">visitor's guide to Wasi Café</a>, "
        "with menu, prices and opening hours.</p>"),
    "secciones": [
        {"h2": "Lo práctico para un visitante", "html": (
            "<ul><li><strong>Pagos:</strong> efectivo, tarjeta de crédito o débito, Yape y Plin.</li>"
            "<li><strong>Idioma:</strong> la <a href=\"/carta\">carta en línea</a> tiene versión en inglés.</li>"
            "<li><strong>WiFi:</strong> gratis para clientes.</li>"
            "<li><strong>Pedido:</strong> desde la mesa, escaneando el código QR, con fotos de cada plato.</li>"
            "<li><strong>Comprobantes:</strong> boleta o factura electrónica, si la misión o la empresa la necesita.</li>"
            "<li><strong>Para llevar:</strong> todo se puede pedir para llevar al hotel o a la oficina.</li></ul>")},
        {"h2": "Horario", "html": (
            f"<p>Atendemos {HORARIO}, de corrido, sin cerrar al mediodía. Según nuestras ventas, las mañanas de 9 a 12 son las más tranquilas, "
            "buenas para una reunión o para leer; las horas de más movimiento son de 1:00 a 2:00 p. m. y de 5:00 a 8:00 p. m.</p>")},
        {"h2": "El café: 100 % peruano", "html": (
            f"<p>Si vienes de fuera, el café peruano merece probarse solo. El nuestro es de especialidad, de {ORIGEN}. Para conocerlo:</p>"
            + lista('Espresso', 'Café Filtrado', 'Capuchino', 'Cortado')
            + "<p>Más sobre los orígenes en la guía de <a href=\"/blog/cafe-peruano-de-origen-cajamarca-cusco-amazonas-san-martin\">café peruano por regiones</a>.</p>"),
         "fotos": [foto('Espresso'), foto('Café Filtrado'), foto('Capuchino'), foto('Cortado')]},
        {"h2": "Lo peruano que vale la pena probar", "html": (
            lista('Chicharrón', 'Tamal Criollo', 'Chicha Morada', 'Lúcuma con Leche', 'Pisco Sour')
            + "<p>El pan con chicharrón y el tamal son el desayuno limeño clásico; la chicha morada es la bebida de maíz morado de toda la vida, y la lúcuma, "
            "una fruta andina difícil de encontrar fresca fuera del Perú. Detalle en <a href=\"/blog/desayuno-criollo-pan-con-chicharron-y-tamal-san-isidro\">desayuno criollo</a> "
            "y <a href=\"/blog/peruvian-drinks-to-try-in-lima\">Peruvian drinks to try in Lima</a>.</p>"),
         "fotos": [foto('Chicharrón'), foto('Tamal Criollo'), foto('Chicha Morada'), foto('Pisco Sour')]},
        {"h2": "Desayuno antes de una reunión", "html": (
            f"<p>Desde las 8:00 a. m. de lunes a viernes. Lo más rápido es el <strong>Dúo Café ({s('Dúo Café')})</strong>, café y un mixto; si hay más tiempo, "
            f"el <strong>Desayuno Americano ({s('Desayuno Americano')})</strong> o el <strong>Light ({s('Light')})</strong>, con huevos y palta. "
            "La carta completa está en <a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>")},
        {"h2": "Reuniones y grupos", "html": (
            "<p>Para una reunión de trabajo, una despedida o un desayuno de equipo, se puede reservar mesa desde la <a href=\"/#reservar\">web</a>, "
            "y para grupos hay paquetes de café, brunch o cumpleaños: mira <a href=\"/blog/eventos-y-cumpleanos-en-cafeteria-san-isidro\">eventos en San Isidro</a>.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Wasi Café acepta tarjetas extranjeras?", "r": "Acepta tarjeta de crédito y débito, además de efectivo, Yape y Plin."},
        {"p": "¿La carta está en inglés?", "r": "Sí, la carta en línea en wasicafe.com/carta tiene versión en inglés."},
        {"p": "¿Emiten factura?", "r": "Sí, boleta o factura electrónica."},
        {"p": "¿Abre los domingos?", "r": "No. De lunes a viernes de 8:00 a. m. a 9:00 p. m. y los sábados de 9:00 a. m. a 9:00 p. m."},
    ],
    "relacionados": ["coffee-shop-in-san-isidro-lima-wasi-cafe", "san-isidro-para-turistas-guia-cafe", "reuniones-de-trabajo-en-cafeteria-san-isidro"],
})

# ------------------------------------------------------------ El Olivar
fichas.append({
    "slug": "donde-desayunar-cerca-de-el-olivar-san-isidro",
    "tituloSeo": "Dónde desayunar cerca de El Olivar, San Isidro | Wasi Café",
    "h1": "Desayunar cerca de El Olivar: un plan de mañana en San Isidro, con precios",
    "tituloCorto": "Desayunar cerca de El Olivar",
    "ogTitulo": "Paseo por El Olivar y desayuno en Wasi Café",
    "descripcion": "Plan de mañana en San Isidro: un paseo por el Bosque El Olivar y desayuno en Wasi Café, a menos de un kilómetro, con combos desde S/ 19.90.",
    "eyebrow": "desayuno cerca de El Olivar",
    "fecha": "2026-06-14", "modificado": HOY,
    "about": ["Desayuno", "El Olivar", "San Isidro"],
    "intro": (
        "<p>El <strong>Bosque El Olivar</strong> es el parque más querido de San Isidro: olivos centenarios, caminos de tierra y gente paseando a sus perros desde temprano. "
        "Después de una vuelta, el plan natural es desayunar. <strong>Wasi Café</strong> está a menos de un kilómetro, en Luis Felipe Villarán 904, "
        "y abre a las 8:00 a. m. de lunes a viernes y a las 9:00 a. m. los sábados.</p>"),
    "secciones": [
        {"h2": "El plan, paso a paso", "html": (
            "<ul><li><strong>Temprano:</strong> paseo por El Olivar, cuando el bosque está más tranquilo.</li>"
            "<li><strong>Después:</strong> unos minutos caminando hasta Wasi Café, en Luis Felipe Villarán 904. "
            f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Ver la ruta en Google Maps</a>.</li>"
            "<li><strong>Desayuno:</strong> un combo con café, o algo a tu medida de la carta.</li></ul>"
            "<p>Si vas con tu perro, también es bienvenido: Wasi es pet friendly. Lee la guía para "
            "<a href=\"/blog/cafeterias-pet-friendly-san-isidro\">ir a la cafetería con tu mascota</a>.</p>")},
        {"h2": "Combos de desayuno con precio", "html": (
            "<ul>"
            f"<li><strong>Continental ({s('Continental')})</strong>: café, jugo de papaya o piña, tostadas, mermelada y mantequilla.</li>"
            f"<li><strong>Dúo Café ({s('Dúo Café')})</strong>: café y mixto clásico de jamón y queso.</li>"
            f"<li><strong>Light ({s('Light')})</strong>: café, huevos, porción de palta y tostadas. Ideal después de caminar.</li>"
            f"<li><strong>Desayuno Americano ({s('Desayuno Americano')})</strong>: café, jugo, huevos revueltos o fritos y tostadas.</li>"
            f"<li><strong>Amanecer Criollo ({s('Amanecer Criollo')})</strong>: café americano y pan con chicharrón.</li></ul>"
            "<p>El Light y el Desayuno Americano son de los más pedidos. Todos los combos, en "
            "<a href=\"/blog/desayunos-en-san-isidro-carta-precios-horario\">desayunos en San Isidro</a>.</p>")},
        {"h2": "Si prefieres armarlo a tu gusto", "html": (
            lista('Omelette Completo', 'Huevos Revueltos', 'Croissant Huevos y Jamón', 'Tamal Criollo')
            + "<p>Hay siete omelettes en total: los tienes en <a href=\"/blog/omelettes-y-huevos-en-san-isidro\">omelettes y huevos en San Isidro</a>.</p>"),
         "fotos": [foto('Omelette Completo'), foto('Huevos Revueltos'), foto('Croissant Huevos y Jamón'), foto('Tamal Criollo')]},
        {"h2": "Algo fresco después de caminar", "html": (
            lista('Jugo de Papaya', 'Jugo de Naranja', 'Jugo Surtido', 'Fresa con Leche')
            + "<p>El de papaya es el jugo más pedido de la casa. Si hace calor, un frozen de fruta también entra bien: hay once sabores en "
            "<a href=\"/blog/jugos-y-batidos-en-san-isidro-precios\">jugos, batidos y frozen</a>.</p>"),
         "fotos": [foto('Jugo de Papaya'), foto('Jugo de Naranja'), foto('Jugo Surtido'), foto('Fresa con Leche')]},
        {"h2": "El café", "html": (
            f"<p>Somos cafetería de especialidad: café 100 % peruano de {ORIGEN}. Para después de un paseo, un "
            f"<strong>capuchino ({s('Capuchino')})</strong> o un <strong>café filtrado ({s('Café Filtrado')})</strong>. Si es tu primera vez, "
            "la guía de <a href=\"/blog/cafe-de-especialidad-san-isidro-guia\">café de especialidad en San Isidro</a> te ayuda a elegir.</p>")},
        {"h2": "El sábado, sin apuro", "html": (
            "<p>El sábado abrimos a las 9:00 a. m., una buena hora para combinar el paseo con un desayuno largo o un brunch. "
            "Los domingos estamos cerrados. Para el plan de sábado, mira la guía de "
            "<a href=\"/blog/brunch-en-san-isidro-que-pedir-como-elegir\">brunch en San Isidro</a>.</p>")},
        donde("Todo se puede pedir para llevar. "),
    ],
    "faq": [
        {"p": "¿Qué tan lejos está Wasi Café de El Olivar?", "r": "A menos de un kilómetro, unos minutos caminando, en Luis Felipe Villarán 904, San Isidro."},
        {"p": "¿A qué hora abre para desayunar?", "r": "A las 8:00 a. m. de lunes a viernes y a las 9:00 a. m. los sábados. Los domingos está cerrado."},
        {"p": "¿Puedo ir con mi perro después del paseo?", "r": "Sí, Wasi Café es pet friendly."},
        {"p": "¿Cuánto cuesta desayunar?", "r": f"Los combos de desayuno con café empiezan en {s('Continental')}."},
    ],
    "relacionados": ["cafe-cerca-del-parque-el-olivar-san-isidro", "desayunos-en-san-isidro-carta-precios-horario", "cafeterias-pet-friendly-san-isidro"],
})

# ------------------------------------------------------------ Pet friendly
fichas.append({
    "slug": "cafeterias-pet-friendly-san-isidro",
    "tituloSeo": "Cafetería pet friendly en San Isidro | Wasi Café",
    "h1": "Cafetería pet friendly en San Isidro: ir a Wasi Café con tu perro",
    "tituloCorto": "Pet friendly en San Isidro",
    "ogTitulo": "Ir con tu perro a una cafetería de San Isidro",
    "descripcion": "Wasi Café es una cafetería pet friendly en San Isidro: consejos para ir con tu perro, qué pedir, horario y cómo llegar desde El Olivar.",
    "eyebrow": "pet friendly en San Isidro",
    "fecha": "2026-06-14", "modificado": HOY,
    "about": ["Pet friendly", "San Isidro", "Cafetería"],
    "intro": (
        "<p>En San Isidro mucha gente pasea a su perro por El Olivar o por los parques del distrito, y no tiene por qué dejarlo en casa para ir por un café. "
        "<strong>Wasi Café</strong>, en Luis Felipe Villarán 904, es <strong>pet friendly</strong>: tu perro es bienvenido. "
        "Aquí van consejos para que la visita salga bien para todos, y qué pedir.</p>"),
    "secciones": [
        {"h2": "Consejos para ir con tu perro", "html": (
            "<ul><li><strong>Con correa:</strong> así está cómodo y no incomoda a otras mesas.</li>"
            "<li><strong>Después de caminar:</strong> un perro que ya paseó se queda más tranquilo mientras tomas tu café.</li>"
            "<li><strong>Elige la hora:</strong> según nuestras ventas, las mañanas de 9 a 12 son las más tranquilas; de 1 a 2 p. m. y de 5 a 8 p. m. hay más gente.</li>"
            "<li><strong>Lleva su agua y algo para él:</strong> sobre todo en verano.</li>"
            "<li><strong>Una mesa amplia:</strong> si vas con un perro grande, avísanos al llegar para ubicarte cómodo.</li></ul>")},
        {"h2": "Qué pedir para ti", "html": (
            "<p>Desayuno desde las 8:00 a. m. de lunes a viernes, con combos que incluyen café:</p><ul>"
            f"<li><strong>Light ({s('Light')})</strong>: café, huevos, palta y tostadas.</li>"
            f"<li><strong>Continental ({s('Continental')})</strong>: café, jugo y tostadas.</li>"
            f"<li><strong>Amanecer Criollo ({s('Amanecer Criollo')})</strong>: americano y pan con chicharrón.</li></ul>"
            "<p>Y si es la tarde, un postre de la vitrina con café: mira <a href=\"/blog/postres-artesanales-cafeteria-san-isidro\">postres en San Isidro</a>.</p>"),
         "fotos": [foto('Capuchino'), foto('Chicharrón'), foto('Cheesecake de Frutos del Bosque')]},
        {"h2": "Para llevar, si tu perro no se queda quieto", "html": (
            "<p>No todos los perros disfrutan de esperar en una cafetería. En ese caso, todo se puede pedir <strong>para llevar</strong>: "
            f"un <strong>americano ({s('Americano')})</strong>, un <strong>café helado ({s('Café Helado')})</strong> o un sándwich para seguir el paseo.</p>"
            "<p>La carta completa, con precios al día, está en <a href=\"/carta\">wasicafe.com/carta</a>.</p>")},
        {"h2": "Un plan completo: El Olivar y desayuno", "html": (
            "<p>Wasi Café está a menos de un kilómetro del Bosque El Olivar. Un paseo temprano con tu perro y luego desayuno es uno de los planes de mañana "
            "más simples de San Isidro: lo contamos en <a href=\"/blog/donde-desayunar-cerca-de-el-olivar-san-isidro\">desayunar cerca de El Olivar</a>.</p>")},
        {"h2": "Pedir sin levantarte", "html": (
            "<p>Con el perro al lado, pararse a la barra no siempre es cómodo. En cada mesa hay un <strong>código QR</strong>: lo escaneas, ves la carta con fotos "
            "y el pedido llega directo a la barra. Desde el mismo celular pides la cuenta. Aceptamos efectivo, tarjeta, Yape y Plin.</p>")},
        {"h2": "Si tu perro es cachorro o se pone nervioso", "html": (
            "<ul><li><strong>Empieza con visitas cortas:</strong> un café rápido de quince minutos antes de quedarte toda una mañana.</li>"
            "<li><strong>Lleva su manta o su juguete:</strong> algo que huela a casa lo ayuda a echarse tranquilo.</li>"
            "<li><strong>Siéntate cerca de la salida:</strong> si necesita salir un momento, no tienes que cruzar todo el local.</li>"
            "<li><strong>En verano, de diciembre a abril:</strong> evita las horas de más calor para el paseo y para el camino hasta la cafetería.</li></ul>"
            f"<p>Y para ti, en esos días de calor, un <strong>frozen de maracuyá ({s('Frozen Maracuyá')})</strong> o una <strong>limonada ({s('Limonada')})</strong>.</p>")},
        {"h2": "Para trabajar con tu perro al lado", "html": (
            "<p>Si trabajas remoto y tu perro te acompaña, hay WiFi gratis y abrimos de corrido todo el día. Mira la guía de "
            "<a href=\"/blog/cafeterias-para-trabajar-laptop-san-isidro\">trabajar con laptop en San Isidro</a>.</p>")},
        donde(),
    ],
    "faq": [
        {"p": "¿Wasi Café acepta perros?", "r": "Sí, Wasi Café es pet friendly: tu perro es bienvenido."},
        {"p": "¿A qué hora conviene ir con mascota?", "r": "Las mañanas de 9 a 12 son las más tranquilas, según las ventas del local."},
        {"p": "¿Está cerca de El Olivar?", "r": "Sí, a menos de un kilómetro, en Luis Felipe Villarán 904, San Isidro."},
    ],
    "relacionados": ["donde-desayunar-cerca-de-el-olivar-san-isidro", "cafe-cerca-del-parque-el-olivar-san-isidro", "cafeterias-para-trabajar-laptop-san-isidro"],
})

json.dump(fichas, open(AQUI / 'ola5.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(fichas), 'fichas | guiones largos:', json.dumps(fichas, ensure_ascii=False).count('—'))
