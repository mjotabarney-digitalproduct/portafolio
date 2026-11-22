# Home page content. Each text is {'en':..., 'es':...}
def L(en, es): return {'en': en, 'es': es}

SITE = {
    'name': 'María José Barney',
    'email': 'mjotabarney@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/mariajosebarney/',
    'behance': 'https://www.behance.net/mariajosebarney',
    'role': L('Product Designer · UI, UX &amp; Research', 'Diseñadora de Producto · UI, UX e Investigación'),
    'desc': L('Product designer from Colombia. Case studies on regulated, high-friction digital products: insurance enrollment, health questionnaires, a corporate intranet.',
              'Diseñadora de producto en Colombia. Casos de estudio sobre productos digitales regulados y de alta fricción: afiliación a seguros, cuestionarios de salud, una intranet corporativa.'),
}

NAV = [
    ('#work', L('Work', 'Casos')),
    ('#approach', L('Approach', 'Cómo pienso')),
    ('#about', L('About', 'Sobre mí')),
    ('#contact', L('Contact', 'Contacto')),
]

HERO = {
    'label': L('Product Designer · UI, UX &amp; Research', 'Diseñadora de Producto · UI, UX e Investigación'),
    'h1': L('Where things get complicated,<br><em>I get curious.</em>',
            'Cuando algo se complica,<br><em>me da curiosidad.</em>'),
    'dek': L('Four years turning regulated, high-friction processes into flows people actually finish. Steady under pressure, happiest in a team.',
             'Cuatro años convirtiendo procesos regulados y llenos de fricción en flujos que la gente sí termina. Serena bajo presión, feliz en equipo.'),
    'meta': [L('<i class="dot"></i>Available now', '<i class="dot"></i>Disponible ahora'),
             L('Cali, Colombia', 'Cali, Colombia'),
             L('English C2 · Spanish native', 'Inglés C2 · Español nativo')],
    'cta1': L('See the work ↓', 'Ver los casos ↓'),
    'cta2': L('Email me', 'Escríbeme'),
}

STATS = {
    'label': L('By the numbers', 'En cifras'),
    'intro': L('A few results from recent projects, each one tied to a decision I made.',
               'Algunos resultados de proyectos recientes, cada uno ligado a una decisión que tomé.'),
    # (number, title, subtext or None)
    'bars': [
        ('4', L('Years of professional product design', 'Años de diseño de producto profesional'),
              L('Across insurance, health, a corporate intranet and a B2B startup.', 'En seguros, salud, una intranet corporativa y una startup B2B.')),
        ('3', L('Insurance products, end to end', 'Productos de seguros, de punta a punta'),
              L('For a multinational health company, from research to development handoff.', 'Para una multinacional del sector salud, desde la investigación hasta la entrega a desarrollo.')),
        ('95%', L('Fewer answers in a health questionnaire', 'Menos respuestas en un cuestionario de salud'),
                L('Up to 20 people answer once together, 31 answers instead of 620.', 'Hasta 20 personas responden una sola vez en conjunto: 31 respuestas en lugar de 620.')),
        ('+44%', L('Intranet coverage', 'Cubrimiento de la intranet'),
                 L('After splitting it into an office and a remote version.', 'Al dividirla en una versión de oficina y una remota.')),
        ('124', L('Usability issues ranked by severity', 'Problemas de usabilidad clasificados por severidad'),
                L('On a 200+ screen banking platform.', 'En una plataforma bancaria de más de 200 pantallas.')),
    ],
}
# Spanish number formatting for the one value with a thousands separator
STATS_ES_NUM = {'3,832': '3.832'}

WORK = {
    'label': L('Case studies', 'Casos de estudio'),
    'intro': L('Projects in insurance, health, internal tools and a B2B startup, told through the decisions behind them.',
               'Proyectos en seguros, salud, herramientas internas y una startup B2B, contados a través de las decisiones detrás de cada uno.'),
    'see': L('Read the case', 'Leer el caso'),
}

BEHANCE = {
    'label': L('More work', 'Más trabajo'),
    'h': L('Collaborative case studies, <em>on Behance.</em>', 'Casos colaborativos, <em>en Behance.</em>'),
    'p': L('Projects designed together with other designers, developers and clients across fintech, energy and digital products, with the full visual process.',
           'Proyectos diseñados junto a otras diseñadoras, desarrolladores y clientes en fintech, energía y productos digitales, con todo el proceso visual.'),
    'cta': L('See them on Behance ↗', 'Verlos en Behance ↗'),
}

PRINCIPLES = {
    'label': L('How I think', 'Cómo pienso'),
    'intro': L('Four habits I bring to every project.', 'Cuatro hábitos que llevo a cada proyecto.'),
    'items': [
        (L('Design the unhappy path first', 'Diseñar primero el camino que falla'),
         L('I think about what can go wrong before what goes right. That’s where people get frustrated, and it’s rarely planned for.',
           'Pienso en lo que puede salir mal antes que en lo que sale bien. Ahí es donde la gente se frustra, y casi nadie lo planea.'),
         'esencial-dental'),
        (L('Bring evidence into the room', 'Llevar evidencia a la reunión'),
         L('When I disagree, I bring data and examples instead of my opinion. It keeps the conversation from getting personal and makes it easier to decide together.',
           'Cuando no estoy de acuerdo, no llego con mi opinión sino con datos y ejemplos. Así la conversación deja de ser personal y se vuelve más fácil decidir juntos.'),
         'salud-activa'),
        (L('Scope is a design decision', 'El alcance también es diseño'),
         L('Before designing, I make sure the goal is clear and achievable. Sometimes the most useful thing I can do is reframe the question.',
           'Antes de diseñar, me aseguro de que el objetivo sea claro y alcanzable. A veces lo más útil que puedo hacer es replantear la pregunta.'),
         'tqnet'),
        (L('Write down what nobody owns', 'Dejar por escrito lo que nadie asume'),
         L('When something important is left hanging, I write it down and bring it to whoever needs to decide. I’d rather have an awkward conversation today than a surprise tomorrow.',
           'Cuando algo importante queda en el aire, lo escribo y se lo hago llegar a quien tiene que decidir. Prefiero una conversación incómoda hoy que una sorpresa mañana.'),
         'poliza-bienestar'),
    ],
    'link': L('See it in the case →', 'Verlo en el caso →'),
}

ABOUT = {
    'label': L('About', 'Sobre mí'),
    'big': L('I’m a product designer from Cali with a double degree in Interactive Media Design and International Marketing and Advertising.',
             'Soy diseñadora de producto, de Cali, con doble titulación en Diseño de Medios Interactivos y Mercadeo Internacional y Publicidad.'),
    'body': L('I’ve worked inside a global consultancy on a health insurer’s digital sales, in a pharmaceutical company’s internal communications team, and leading marketing at an AI consultancy.',
              'He trabajado dentro de una consultora global en la venta digital de una aseguradora de salud, en el equipo de comunicación interna de una farmacéutica y liderando el mercadeo de una consultora de IA.'),
    'qual': [L('I listen before I design', 'Escucho antes de diseñar'),
             L('I decide with evidence', 'Decido con evidencia'),
             L('I enjoy teamwork', 'Disfruto el trabajo en equipo'),
             L('Calm under pressure', 'Calma bajo presión'),
             L('Accessibility from the start', 'Accesibilidad desde el inicio')],
    'exp_label': L('Experience', 'Experiencia'),
    'exp': [
        (L('Oct 2025 to Oct 2026', 'oct 2025 a oct 2026'), L('Product Designer (UX/UI) · Indra Group', 'Diseñadora de Producto (UX/UI) · Indra Group'),
         L('Three digital-sales products for a multinational health company: two plan enrollments, a health questionnaire and a new preventive-health policy.', 'Tres productos de venta digital para una multinacional del sector salud: dos afiliaciones a planes, un cuestionario de salud y una póliza nueva de salud preventiva.')),
        (L('Apr to Sep 2026', 'abr a sep 2026'), L('Marketing Growth Lead · XTAM', 'Marketing Growth Lead · XTAM'),
         L('Responsible for B2B marketing and corporate branding at an AI consultancy, working directly with the founders. I set up the foundations and processes for the function to keep growing.', 'Responsable del mercadeo B2B y la marca corporativa de una consultora de IA, trabajando directamente con los founders. Dejé las bases y los procesos para que el área siguiera creciendo.')),
        (L('Jan to Jul 2025', 'ene a jul 2025'), L('Internal Communications &amp; UX · Tecnoquímicas', 'Comunicación Interna y UX · Tecnoquímicas'),
         L('Redesign of the TQNet intranet.', 'Rediseño de la intranet TQNet.')),
        (L('2024', '2024'), L('UX/UI Designer · UX Lab, Universidad Icesi', 'Diseñadora UX/UI · UX Lab, Universidad Icesi'),
         L('Client prototypes, usability tests and heuristic evaluations presented to stakeholders.', 'Prototipos para clientes, pruebas de usabilidad y evaluaciones heurísticas presentadas a stakeholders.')),
        (L('2023 to 2025', '2023 a 2025'), L('Service Experience Specialist · TaskUs', 'Service Experience Specialist · TaskUs'),
         L('High-volume English-language support against quality standards and SLAs.', 'Atención de alto volumen en inglés con estándares de calidad y SLA.')),
        (L('2022 to 2024', '2022 a 2024'), L('Freelance UX/UI &amp; brand designer', 'Diseñadora UX/UI y de marca independiente'),
         L('Research, prototypes, identity systems and brand manuals for emerging brands.', 'Investigación, prototipos, sistemas de identidad y manuales de marca para marcas emergentes.')),
        (L('2018 to 2025', '2018 a 2025'), L('Interactive Media Design · International Marketing and Advertising', 'Diseño de Medios Interactivos · Mercadeo Internacional y Publicidad'),
         L('Universidad Icesi, Cali. Two degrees, completed concurrently.', 'Universidad Icesi, Cali: dos carreras, cursadas en paralelo.')),
    ],
}

CONTACT = {
    'label': L('Contact', 'Contacto'),
    'h2': L('Got something complicated? <em>Let’s talk.</em>', '¿Tienes algo complicado? <em>Hablemos.</em>'),
    'fine_l': L('© 2026 María José Barney Ñañez', '© 2026 María José Barney Ñañez'),
    'fine_r': L('Client work shown with brand, prices and personal data removed.', 'El trabajo de clientes se muestra sin marca, precios ni datos personales.'),
}
