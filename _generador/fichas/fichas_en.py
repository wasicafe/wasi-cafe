"""Guías en inglés para visitantes y extranjeros (28/10/2026).

San Isidro concentra embajadas, hoteles y oficinas internacionales, y quien busca
en inglés no encontraba nada de Wasi Café. Mismas reglas que las guías en español:
precios y descripciones de la carta del POS (carta-wasi.json), horario y servicios
de la portada, «lo más pedido» de las ventas reales. Nada que no conste.
Uso: python3 fichas_en.py [--rel]  → escribe en.json (con --rel, con enlaces cruzados)
"""
import json, pathlib, sys

AQUI = pathlib.Path(__file__).resolve().parent
CARTA = {x['n']: x for x in json.load(open(AQUI / 'carta-wasi.json', encoding='utf-8'))}
HOY = '2026-10-28'
MAPA = 'https://maps.google.com/?q=Wasi+Cafe+Luis+Felipe+Villaran+904+San+Isidro+Lima'
WA = 'https://wa.me/51908724496'
HOURS = ('Monday to Friday from <strong>8:00 a.m. to 9:00 p.m.</strong> and Saturday from '
         '<strong>9:00 a.m. to 9:00 p.m.</strong>; closed on Sundays')
ORIGIN = 'Cusco, Cajamarca, Junín, Amazonas and San Martín'
SLUGS = ['coffee-shop-in-san-isidro-lima-wasi-cafe', 'peruvian-breakfast-in-lima-what-to-order',
         'peruvian-drinks-to-try-in-lima']


def foto(nombre, en, pie=None):
    x = CARTA[nombre]
    if not x.get('img'):
        raise SystemExit(f'sin foto: {nombre}')
    return {'src': '/' + x['img'].split('wasicafe.com/')[1], 'alt': f"{en} at Wasi Café, San Isidro, Lima",
            'pie': pie or f"{en} · S/ {x['p']:.2f}"}


def s(n):
    return f"S/ {CARTA[n]['p']:.2f}"


def where(extra=''):
    return {"h2": "Where we are", "html": (
        f"<p>Wasi Café is at <strong>Luis Felipe Villarán 904, San Isidro, Lima</strong>, a short walk from Javier Prado Avenue, "
        f"close to El Olivar park and the financial district. We are open {HOURS}. {extra}"
        f"<a href=\"{MAPA}\" target=\"_blank\" rel=\"noopener\">Open it in Google Maps</a>, or message us on "
        f"<a href=\"{WA}\" target=\"_blank\" rel=\"noopener\">WhatsApp at +51 908 724 496</a>.</p>")}


def rel(slug):
    return [x for x in SLUGS if x != slug] if '--rel' in sys.argv else []


fichas = []

# ------------------------------------------------------------ 1. Visitors guide
fichas.append({
    "idioma": "en",
    "slug": SLUGS[0],
    "tituloSeo": "Coffee shop in San Isidro, Lima: menu and hours | Wasi Café",
    "h1": "Wasi Café: a specialty coffee shop in San Isidro, Lima, with menu, prices and hours",
    "tituloCorto": "Coffee shop in San Isidro",
    "ogTitulo": "Wasi Café, specialty coffee in San Isidro, Lima",
    "descripcion": "Specialty Peruvian coffee, breakfast, brunch and lunch in San Isidro, Lima: Wasi Café menu with prices, opening hours, payments and WiFi.",
    "eyebrow": "coffee in San Isidro, Lima",
    "fecha": HOY, "modificado": HOY,
    "about": ["Specialty coffee", "San Isidro", "Lima"],
    "intro": (
        "<p>If you are staying or working in <strong>San Isidro</strong>, Lima's business district, and want good coffee without a long taxi ride, "
        "<strong>Wasi Café</strong> is a specialty coffee shop on Luis Felipe Villarán 904, a short walk from Javier Prado Avenue. "
        "<em>Wasi</em> means «house» in Quechua. This guide has everything a visitor needs: hours, what to order, prices and how to pay.</p>"
        "<p>All prices are in Peruvian soles (S/) and come from our <a href=\"/carta\">online menu</a>, which is also available in English "
        "and updates automatically from our register.</p>"),
    "secciones": [
        {"h2": "Opening hours", "html": (
            f"<p>We are open {HOURS}. We don't close at midday, so you can come for breakfast and stay through lunch.</p>"
            "<p>According to our sales, the busiest times are 1 to 2 p.m. (lunch) and 5 to 8 p.m.; mornings from 9 to 12 are the quietest, "
            "which makes them a good time to work or read.</p>")},
        {"h2": "The coffee", "html": (
            f"<p>All our coffee is 100% Peruvian specialty coffee from {ORIGIN}. Some prices from the bar:</p><ul>"
            f"<li><strong>Espresso ({s('Espresso')})</strong> and <strong>Americano ({s('Americano')})</strong>. The Americano is by far our most served coffee.</li>"
            f"<li><strong>Cortado ({s('Cortado')})</strong>, <strong>Cappuccino ({s('Capuchino')})</strong> and <strong>Latte, «café con leche» ({s('Café con Leche')})</strong>.</li>"
            f"<li><strong>Filter coffee ({s('Café Filtrado')})</strong>.</li>"
            f"<li><strong>Iced coffee ({s('Café Helado')})</strong>, <strong>iced latte ({s('Café con Leche Helado')})</strong> and frappés from {s('Frappé de Café mediano')}.</li></ul>"
            "<p>If you've never tried Peruvian coffee, start with an espresso or a filter coffee to taste the bean on its own.</p>"),
         "fotos": [foto('Espresso', 'Espresso'), foto('Capuchino', 'Cappuccino'), foto('Café Filtrado', 'Filter coffee'), foto('Café Helado', 'Iced coffee')]},
        {"h2": "Breakfast and brunch", "html": (
            "<p>Breakfast combos all include coffee, and several add a fresh papaya or pineapple juice:</p><ul>"
            f"<li><strong>Continental ({s('Continental')})</strong>: coffee, juice, toast, jam and butter.</li>"
            f"<li><strong>American breakfast ({s('Desayuno Americano')})</strong>: coffee, juice, scrambled or fried eggs and toast.</li>"
            f"<li><strong>Light ({s('Light')})</strong>: coffee, eggs, avocado and toast.</li>"
            f"<li><strong>Amanecer Criollo ({s('Amanecer Criollo')})</strong>: Americano and a pan con chicharrón, the classic Lima breakfast sandwich.</li></ul>"
            "<p>The Light and the American breakfast are the most ordered. On Saturdays, from 9 a.m., brunch is the plan. "
            "For the Peruvian options, read our guide to a <a href=\"/blog/peruvian-breakfast-in-lima-what-to-order\">Peruvian breakfast in Lima</a>.</p>"),
         "fotos": [foto('Omelette Completo', 'Omelette'), foto('Croissant Huevos y Jamón', 'Egg and ham croissant'), foto('Tamal Criollo', 'Peruvian tamal')]},
        {"h2": "Lunch from 12 to 4", "html": (
            "<p>Monday to Saturday, from 12 to 4 p.m., there are lunch combos with a main dish, Andean potatoes and a drink of your choice: "
            f"the <strong>chicken fillet combo ({s('Combo Filete')})</strong>, our most ordered, and steak, pork chop, breaded cutlet, chicken breast "
            f"or burger combos at {s('Combo Bistec')}. There are also sandwiches, burgers and salads all day.</p>"),
         "fotos": [foto('Filete de Pollo', 'Chicken fillet sandwich'), foto('Hamburguesa Wasi', 'Wasi burger'), foto('Ensalada César', 'Caesar salad')]},
        {"h2": "Peruvian things to try", "html": (
            "<ul>"
            f"<li><strong>Chicha morada ({s('Chicha Morada')})</strong>: a traditional drink made from purple corn.</li>"
            f"<li><strong>Lúcuma</strong>: a Peruvian fruit that tastes a bit like caramel. Try it as a milkshake ({s('Lúcuma con Leche')}) or a frozen drink.</li>"
            f"<li><strong>Pisco sour ({s('Pisco Sour')})</strong>: Peru's signature cocktail, with pisco, lime, syrup and egg white.</li>"
            f"<li><strong>Affogato with pisco ({s('Affogato Wasi + Pisco')})</strong>: espresso over ice cream with half an ounce of pisco, a house recipe.</li></ul>"
            "<p>More in our guide to <a href=\"/blog/peruvian-drinks-to-try-in-lima\">Peruvian drinks to try in Lima</a>.</p>"),
         "fotos": [foto('Chicha Morada', 'Chicha morada'), foto('Lúcuma con Leche', 'Lúcuma milkshake'), foto('Pisco Sour', 'Pisco sour')]},
        {"h2": "Practical information for visitors", "html": (
            "<ul><li><strong>Payments:</strong> cash, credit and debit cards, and the local apps Yape and Plin.</li>"
            "<li><strong>WiFi:</strong> free for customers.</li>"
            "<li><strong>Pets:</strong> dogs are welcome.</li>"
            "<li><strong>Ordering:</strong> scan the QR code on your table to see the menu with photos and order directly; you can also ask for the bill from your phone.</li>"
            "<li><strong>Take away:</strong> everything on the menu can be ordered to go.</li>"
            "<li><strong>Reservations:</strong> from our <a href=\"/#reservar\">website</a>; we confirm by WhatsApp.</li></ul>")},
        where(),
    ],
    "faq": [
        {"p": "Is Wasi Café open on Sundays?", "r": "No. It is open Monday to Friday from 8:00 a.m. to 9:00 p.m. and Saturday from 9:00 a.m. to 9:00 p.m."},
        {"p": "Do you accept credit cards?", "r": "Yes, cash, credit and debit cards, Yape and Plin."},
        {"p": "Is there WiFi?", "r": "Yes, free WiFi for customers."},
        {"p": "Is the menu available in English?", "r": "Yes, the online menu at wasicafe.com/carta has an English version."},
        {"p": "Where is Wasi Café?", "r": "At Luis Felipe Villarán 904, San Isidro, Lima, a short walk from Javier Prado Avenue."},
    ],
    "relacionados": rel(SLUGS[0]),
})

# ------------------------------------------------------------ 2. Peruvian breakfast
fichas.append({
    "idioma": "en",
    "slug": SLUGS[1],
    "tituloSeo": "Peruvian breakfast in Lima: what to order | Wasi Café",
    "h1": "Peruvian breakfast in Lima: what to order, from pan con chicharrón to tamal",
    "tituloCorto": "Peruvian breakfast in Lima",
    "ogTitulo": "What to order for a Peruvian breakfast in Lima",
    "descripcion": "A guide to Peruvian breakfast in Lima: pan con chicharrón, tamal, butifarra and chicha morada, with real prices at Wasi Café in San Isidro.",
    "eyebrow": "Peruvian breakfast",
    "fecha": HOY, "modificado": HOY,
    "about": ["Peruvian breakfast", "Pan con chicharrón", "Lima"],
    "intro": (
        "<p>A traditional Lima breakfast is not continental. It is fried pork in a crusty bread roll, a tamal wrapped in a banana leaf, "
        "sweet potato, a tangy onion relish called <em>salsa criolla</em>, and coffee. Here is what each one is and what it costs at "
        "<strong>Wasi Café</strong>, a specialty coffee shop in San Isidro, Lima.</p>"),
    "secciones": [
        {"h2": "Pan con chicharrón", "html": (
            "<p>The king of the Lima breakfast: slices of slow-cooked, then fried pork (<em>chicharrón</em>) in a bread roll, "
            "with fried sweet potato and salsa criolla.</p>"
            f"<p>At Wasi it costs <strong>{s('Chicharrón')}</strong>, or <strong>{s('Amanecer Criollo')}</strong> in the «Amanecer Criollo» combo with an Americano.</p>"),
         "fotos": [foto('Chicharrón', 'Pan con chicharrón'), foto('Camote Frito', 'Fried sweet potato'), foto('Ensalada Criolla', 'Salsa criolla')]},
        {"h2": "Tamal", "html": (
            "<p>A Peruvian tamal is corn dough with a filling, steamed in a banana leaf. In Lima it is eaten for breakfast with salsa criolla, "
            "often inside a <em>pan francés</em>, the local bread roll.</p>"
            f"<p>Our <strong>Tamal Criollo ({s('Tamal Criollo')})</strong> comes with salsa criolla in pan francés. "
            f"The <strong>Desayuno Tamalero ({s('Desayuno Tamalero')})</strong> adds a coffee.</p>"),
         "fotos": [foto('Tamal Criollo', 'Tamal criollo')]},
        {"h2": "Butifarra", "html": (
            f"<p>The <strong>butifarra ({s('Butifarra')})</strong> is a sandwich of <em>jamón del país</em>, a Peruvian-style cooked ham, with salsa criolla. "
            "Lighter than the chicharrón and just as local. If you want beef, try the <strong>sándwich de asado</strong> "
            f"({s('Sándwich de Asado')}), with roast beef in artisan bread.</p>"),
         "fotos": [foto('Butifarra', 'Butifarra'), foto('Sándwich de Asado', 'Roast beef sandwich')]},
        {"h2": "The full table for two", "html": (
            f"<p>If you want the whole experience, the <strong>Tradición Wasi ({s('Tradición Wasi')})</strong> is made for sharing. It includes:</p><ul>"
            "<li>2 coffees and 2 fresh juices (papaya or pineapple).</li>"
            "<li>250 g of chicharrón and a chicken tamal.</li>"
            "<li>100 g of <em>salchicha huachana</em>, a spiced sausage from the north of Lima, and 4 bread rolls.</li>"
            "<li>Fried sweet potato and salsa criolla.</li></ul>"
            "<p>It is what a Saturday breakfast looks like in many Lima homes.</p>")},
        {"h2": "What to drink", "html": (
            f"<ul><li><strong>Coffee:</strong> an Americano ({s('Americano')}) or a café con leche ({s('Café con Leche')}). Ours is Peruvian specialty coffee from {ORIGIN}.</li>"
            f"<li><strong>Fresh juice:</strong> papaya ({s('Jugo de Papaya')}) is our most ordered juice, followed by the mixed juice and pineapple.</li>"
            f"<li><strong>Chicha morada ({s('Chicha Morada')}):</strong> the purple corn drink pairs well with chicharrón.</li></ul>"),
         "fotos": [foto('Americano', 'Americano'), foto('Jugo de Papaya', 'Papaya juice'), foto('Chicha Morada', 'Chicha morada')]},
        {"h2": "Not a pork person?", "html": (
            "<p>No problem. These are breakfast options without chicharrón, all with coffee included:</p><ul>"
            f"<li><strong>Pollo Wasi ({s('Pollo Wasi')})</strong>: coffee, juice and a chicken sandwich.</li>"
            f"<li><strong>Light ({s('Light')})</strong>: coffee, eggs (boiled, scrambled or fried), avocado and toast.</li>"
            f"<li><strong>Dúo Café ({s('Dúo Café')})</strong>: coffee and a classic ham and cheese sandwich, the quickest option.</li></ul>"
            f"<p>Omelettes start at {s('Omelette de Queso')}, and the full omelette with ham, cheese, bacon, tomato and pepper costs {s('Omelette Completo')}.</p>")},
        {"h2": "When to go", "html": (
            "<p>In Lima, pan con chicharrón is often a Sunday tradition, but Wasi Café is <strong>closed on Sundays</strong>. "
            "Come Monday to Friday from 8 a.m., or on Saturday from 9 a.m. for a long, unhurried breakfast.</p>"
            "<p>If you prefer something more familiar, there are omelettes, eggs and toast too: see our "
            "<a href=\"/blog/coffee-shop-in-san-isidro-lima-wasi-cafe\">visitor's guide to Wasi Café</a>.</p>")},
        where("Everything can be ordered to go. "),
    ],
    "faq": [
        {"p": "What is a typical breakfast in Lima?", "r": "Pan con chicharrón, tamal with salsa criolla, butifarra, fried sweet potato and coffee are the classics."},
        {"p": "How much is pan con chicharrón at Wasi Café?", "r": f"The chicharrón sandwich costs {s('Chicharrón')}, or {s('Amanecer Criollo')} with an Americano."},
        {"p": "Can I have a Peruvian breakfast on Sunday at Wasi Café?", "r": "No, Wasi Café is closed on Sundays. On Saturdays it opens at 9:00 a.m."},
    ],
    "relacionados": rel(SLUGS[1]),
})

# ------------------------------------------------------------ 3. Peruvian drinks
fichas.append({
    "idioma": "en",
    "slug": SLUGS[2],
    "tituloSeo": "Peruvian drinks to try in Lima: chicha, lúcuma, pisco sour",
    "h1": "Peruvian drinks to try in Lima: chicha morada, lúcuma, pisco sour and specialty coffee",
    "tituloCorto": "Peruvian drinks to try in Lima",
    "ogTitulo": "Peruvian drinks you have to try in Lima",
    "descripcion": "Peruvian drinks to try in Lima: chicha morada, lúcuma and passion fruit, pisco sour and Peruvian specialty coffee, with prices at Wasi Café, San Isidro.",
    "eyebrow": "Peruvian drinks",
    "fecha": HOY, "modificado": HOY,
    "about": ["Peruvian drinks", "Pisco sour", "Lima"],
    "intro": (
        "<p>Peru has drinks you won't find anywhere else: a purple corn drink, fruits with no English name, and a national cocktail. "
        "This is a short guide to what to try, and where to try it in San Isidro: <strong>Wasi Café</strong>, a specialty coffee shop on "
        "Luis Felipe Villarán 904. All prices are in Peruvian soles.</p>"),
    "secciones": [
        {"h2": "Chicha morada", "html": (
            "<p>The most Peruvian of soft drinks: purple corn boiled with fruit and spices, served cold. It is sweet, a little spiced, "
            f"and goes with almost any meal. At Wasi a glass costs <strong>{s('Chicha Morada')}</strong>, and there is also a "
            f"<strong>chicha morada frozen</strong> blended with ice ({s('Frozen Chicha Morada')}).</p>"),
         "fotos": [foto('Chicha Morada', 'Chicha morada'), foto('Frozen Chicha Morada', 'Chicha morada frozen')]},
        {"h2": "Lúcuma", "html": (
            "<p>Lúcuma is an Andean fruit with dry, orange flesh and a flavour somewhere between caramel and sweet potato. "
            "It is hard to find fresh outside Peru, so try it here. We serve it as a "
            f"<strong>milkshake ({s('Lúcuma con Leche')})</strong> and as a <strong>frozen ({s('Frozen Lúcuma')})</strong>.</p>"),
         "fotos": [foto('Lúcuma con Leche', 'Lúcuma milkshake'), foto('Frozen Lúcuma', 'Lúcuma frozen')]},
        {"h2": "Passion fruit and other fruits", "html": (
            "<p><em>Maracuyá</em> (passion fruit) is everywhere in Lima. Try the "
            f"<strong>maracuyá drink ({s('Maracuyá')})</strong> or the <strong>maracuyá frozen ({s('Frozen Maracuyá')})</strong>. "
            "Fresh juices are a breakfast staple: papaya is our most ordered, and there is mango, pineapple, orange and strawberry too, "
            f"from {s('Jugo de Papaya')}. The <strong>Jugo Especial ({s('Jugo Especial')})</strong> mixes papaya, pineapple, strawberry, "
            "banana and <em>algarrobina</em>, a carob syrup.</p>"),
         "fotos": [foto('Maracuyá', 'Passion fruit drink'), foto('Jugo de Papaya', 'Papaya juice'), foto('Jugo Especial', 'Jugo especial')]},
        {"h2": "Pisco sour", "html": (
            "<p>Pisco is a Peruvian grape brandy, and the pisco sour is the country's signature cocktail: pisco, lime, syrup and egg white, "
            f"shaken until it foams. At Wasi it costs <strong>{s('Pisco Sour')}</strong>. If you'd rather have it with coffee, the "
            f"<strong>Affogato Wasi + Pisco ({s('Affogato Wasi + Pisco')})</strong> pours espresso over vanilla ice cream with half an ounce of pisco.</p>"),
         "fotos": [foto('Pisco Sour', 'Pisco sour'), foto('Affogato Wasi + Pisco', 'Affogato with pisco')]},
        {"h2": "Peruvian specialty coffee", "html": (
            f"<p>Peru is one of the world's coffee producers, and its high-altitude beans are what we serve: 100% Peruvian specialty coffee from {ORIGIN}. "
            f"An <strong>espresso ({s('Espresso')})</strong> or a <strong>filter coffee ({s('Café Filtrado')})</strong> are the best way to taste it. "
            "If you take milk, the cappuccino is our most popular coffee after the Americano.</p>"),
         "fotos": [foto('Espresso', 'Espresso'), foto('Café Filtrado', 'Filter coffee')]},
        {"h2": "Cold coffee for hot days", "html": (
            "<p>Lima's summer, from December to April, calls for cold drinks. With our Peruvian coffee you can have an "
            f"<strong>iced coffee ({s('Café Helado')})</strong>, an <strong>iced latte ({s('Café con Leche Helado')})</strong> or a "
            f"<strong>frappé</strong> in medium or large, from {s('Frappé de Café mediano')}. The mocha frappé is the most ordered.</p>")},
        {"h2": "Herbal teas, the Lima way", "html": (
            f"<p>After a meal, many people in Lima drink an herbal infusion instead of coffee. Each costs <strong>{s('Manzanilla')}</strong>: "
            "chamomile (<em>manzanilla</em>), anise (<em>anís</em>), lemongrass (<em>hierba luisa</em>), mint (<em>hierba buena</em>), "
            "black tea and iced hibiscus (<em>jamaica</em>). We also have the <strong>tepuchino</strong>, a house creation: tea topped with milk foam, "
            "like a cappuccino without coffee.</p>"),
         "fotos": [foto('Hierba Luisa', 'Lemongrass tea'), foto('Tepuchino', 'Tepuchino')]},
        where("Payments by cash, card, Yape or Plin. "),
    ],
    "faq": [
        {"p": "What is chicha morada?", "r": "A traditional Peruvian drink made from purple corn, served cold. At Wasi Café it costs " + s('Chicha Morada') + "."},
        {"p": "What does lúcuma taste like?", "r": "Like a mix of caramel and sweet potato. Try it as a milkshake or a frozen drink."},
        {"p": "Where can I try a pisco sour in San Isidro?", "r": f"At Wasi Café, Luis Felipe Villarán 904, for {s('Pisco Sour')}, until 9 p.m. Monday to Saturday."},
    ],
    "relacionados": rel(SLUGS[2]),
})

json.dump(fichas, open(AQUI / 'en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
txt = json.dumps(fichas, ensure_ascii=False)
print(len(fichas), 'fichas | guiones largos:', txt.count('—'))
