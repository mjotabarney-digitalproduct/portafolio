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
    'dek': L('Four years turning regulated, high-friction processes into flows people actually finish: insurance enrollment, health questionnaires, a 3,800-person intranet. I win arguments with evidence, not taste.',
             'Cuatro años convirtiendo procesos regulados y llenos de fricción en flujos que la gente sí termina: afiliación a seguros, cuestionarios de salud, una intranet de 3.800 personas. Gano las discusiones con evidencia, no con gusto.'),
    'meta': [L('<i class="dot"></i>Available now', '<i class="dot"></i>Disponible ahora'),
             L('Cali, Colombia · open to relocating to Bogotá', 'Cali, Colombia · con disponibilidad de traslado a Bogotá'),
             L('English C2 · Spanish native', 'Inglés C2 · Español nativo')],
    'cta1': L('See the work ↓', 'Ver los casos ↓'),
    'cta2': L('Email me', 'Escríbeme'),
}

STATS = {
    'label': L('By the numbers', 'En cifras'),
    'intro': L('A few results from recent projects, each one tied to a decision I made. Every number comes from a usability test, an inventory or a delivered project.',
               'Algunos resultados de proyectos recientes, cada uno ligado a una decisión que tomé. Cada número sale de una prueba de usabilidad, un inventario o un proyecto entregado.'),
    'bars': [
        ('4', L('Years designing digital products professionally, across insurance, health, a corporate intranet and a B2B startup.',
                'Años diseñando productos digitales de forma profesional, en seguros, salud, una intranet corporativa y una startup B2B.')),
        ('3', L('Insurance products designed end to end for a multinational health company, from first research to developer handoff.',
                'Productos de seguros diseñados de punta a punta para una multinacional del sector salud, desde la investigación hasta la entrega a desarrollo.')),
        ('27%', L('Of people testing a health plan checkout thought they were done after paying. The extra step I proposed to fix it was adopted.',
                  'De quienes probaron la compra de un plan de salud creyeron que habían terminado al pagar. El paso adicional que propuse para resolverlo se adoptó.')),
        ('1', L('Health questionnaire for up to 20 people on a policy, instead of one per person, with a question model I proposed.',
                'Cuestionario de salud para hasta 20 personas de una póliza, en lugar de uno por persona, con un modelo de pregunta que propuse.')),
        ('+44%', L('More employees can reach their company intranet after I split it into an office version and a remote one for plant staff.',
                   'Más colaboradores pueden entrar a la intranet de su empresa desde que la dividí en una versión de oficina y una remota para el personal de planta.')),
        ('124', L('Usability issues I found and ranked by severity on a banking platform of more than 200 screens, 12 of them critical.',
                  'Problemas de usabilidad que encontré y clasifiqué por severidad en una plataforma bancaria de más de 200 pantallas, 12 de ellos críticos.')),
    ],
}
# Spanish number formatting for the one value with a thousands separator
STATS_ES_NUM = {'3,832': '3.832'}

WORK = {
    'label': L('Case studies', 'Casos de estudio'),
    'intro': L('Each case follows the same spine: the context, the problem as it was handed to me, the evidence, the hard call and what actually happened, including what didn’t ship. Client names are withheld where an NDA applies.',
               'Cada caso sigue la misma columna: el contexto, el problema tal como me llegó, la evidencia, la decisión difícil y lo que pasó de verdad, incluido lo que no salió. Donde hay acuerdo de confidencialidad, el cliente va anónimo.'),
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
    'intro': L('Four habits that show up in every project below. They’re the reason the case studies read more like decision logs than galleries.',
               'Cuatro hábitos que aparecen en todos los proyectos. Son la razón por la que los casos se leen más como bitácoras de decisiones que como galerías.'),
    'items': [
        (L('Design the unhappy path first', 'Diseñar primero el camino que falla'),
         L('Invalid coverage, exceeded limits, a dropped connection, a failed OTP. I delivered those exception flows as their own artifact on a project where nobody had scoped them, because that’s where real users end up.',
           'Cobertura inválida, límites excedidos, una conexión caída, un OTP fallido. Entregué esos flujos de excepción como un artefacto propio en un proyecto donde nadie los había definido, porque ahí es donde termina la gente real.'),
         'esencial-dental'),
        (L('Bring evidence into the room', 'Llevar evidencia a la reunión'),
         L('Both of my hardest calls at a large health insurer were won the same way: with test data and documented patterns from other companies, not with my opinion against a stakeholder’s.',
           'Mis dos decisiones más difíciles en una gran aseguradora de salud se ganaron igual: con datos de prueba y patrones documentados de otras empresas, no con mi opinión contra la de un stakeholder.'),
         'salud-activa'),
        (L('Scope is a design decision', 'El alcance también es diseño'),
         L('On an intranet redesign I rewrote my own objective into something measurable, then proposed a second version of the product that added cost, and brought 44% more of the company into it.',
           'En el rediseño de una intranet reescribí mi propio objetivo para que fuera medible, y luego propuse una segunda versión del producto que sumaba costo, y que metió al 44% más de la empresa.'),
         'tqnet'),
        (L('Write down what nobody owns', 'Dejar por escrito lo que nadie asume'),
         L('A purchase run by one vendor, daily use run by another, and six scope changes nobody filed. Writing them down turned silent design debt into decisions someone had to make.',
           'Una compra en manos de un proveedor, el uso diario en manos de otro, y seis cambios de alcance que nadie tramitó. Escribirlos convirtió deuda silenciosa de diseño en decisiones que alguien tenía que tomar.'),
         'poliza-bienestar'),
    ],
    'link': L('See it in the case →', 'Verlo en el caso →'),
}

ABOUT = {
    'label': L('About', 'Sobre mí'),
    'big': L('I’m a product designer from Cali with a double degree in Interactive Media Design and International Marketing. I like the unglamorous middle of a product: the form with twenty people on it, the error state, the decision nobody wrote down.',
             'Soy diseñadora de producto, de Cali, con doble titulación en Diseño de Medios Interactivos y Mercadeo Internacional. Me gusta el medio poco glamuroso de un producto: el formulario con veinte personas, el estado de error, la decisión que nadie escribió.'),
    'body': L('I’ve worked inside a global consultancy on a health insurer’s digital sales, inside a pharmaceutical company’s internal communications team, and as the only marketing person at an AI startup. The common thread is the same: walk in where the process is undefined, find the people it leaves out, and leave behind documentation the team can keep using without me.',
              'He trabajado dentro de una consultora global en la venta digital de una aseguradora de salud, dentro del equipo de comunicación interna de una farmacéutica y como la única persona de mercadeo en una startup de IA. El hilo es el mismo: entrar donde el proceso no está definido, encontrar a quién deja por fuera y dejar documentación que el equipo pueda seguir usando sin mí.'),
    'qual': [L('Evidence over opinion', 'Evidencia antes que opinión'),
             L('WCAG 2.1 A &amp; AA from the first wireframe', 'WCAG 2.1 A y AA desde el primer wireframe'),
             L('Figma · FigJam · Maze · Notion · HTML &amp; CSS', 'Figma · FigJam · Maze · Notion · HTML y CSS')],
    'exp_label': L('Experience', 'Experiencia'),
    'exp': [
        (L('Oct 2025 to Oct 2026', 'oct 2025 a oct 2026'), L('Product Designer (UX/UI) · Indra Group', 'Diseñadora de Producto (UX/UI) · Indra Group'),
         L('Three digital-sales products for a multinational health company: two plan enrollments, a health questionnaire and a new preventive-health policy.', 'Tres productos de venta digital para una multinacional del sector salud: dos afiliaciones a planes, un cuestionario de salud y una póliza nueva de salud preventiva.')),
        (L('Apr to Sep 2026', 'abr a sep 2026'), L('Marketing Growth Lead · XTAM', 'Marketing Growth Lead · XTAM'),
         L('Built the marketing function of a B2B AI consultancy from zero, reporting to the founders. Concurrent with Indra.', 'Construí desde cero el área de mercadeo de una consultora B2B de IA, reportando a los founders. En paralelo con Indra.')),
        (L('Jan to Jul 2025', 'ene a jul 2025'), L('Internal Communications &amp; UX intern · Tecnoquímicas', 'Practicante de Comunicación Interna y UX · Tecnoquímicas'),
         L('Professional internship on the TQNet intranet redesign.', 'Práctica profesional en el rediseño de la intranet TQNet.')),
        (L('2024', '2024'), L('UX/UI Designer · UX Lab, Universidad Icesi', 'Diseñadora UX/UI · UX Lab, Universidad Icesi'),
         L('Client prototypes, usability tests and heuristic evaluations presented to stakeholders.', 'Prototipos para clientes, pruebas de usabilidad y evaluaciones heurísticas presentadas a stakeholders.')),
        (L('2023 to 2025', '2023 a 2025'), L('Service Experience Specialist · TaskUs', 'Service Experience Specialist · TaskUs'),
         L('High-volume English-language support against quality standards and SLAs.', 'Atención de alto volumen en inglés con estándares de calidad y SLA.')),
        (L('2022 to 2024', '2022 a 2024'), L('Freelance UX/UI &amp; brand designer', 'Diseñadora UX/UI y de marca independiente'),
         L('Research, prototypes, identity systems and brand manuals for emerging brands.', 'Investigación, prototipos, sistemas de identidad y manuales de marca para marcas emergentes.')),
        (L('2018 to 2025', '2018 a 2025'), L('BA Interactive Media Design · BA International Marketing &amp; Advertising', 'Diseño de Medios Interactivos · Mercadeo Internacional y Publicidad'),
         L('Universidad Icesi, Cali. Two degrees, completed concurrently.', 'Universidad Icesi, Cali: dos carreras, cursadas en paralelo.')),
    ],
}

CONTACT = {
    'label': L('Contact', 'Contacto'),
    'h2': L('Let’s talk about the <em>messy middle.</em>', 'Hablemos del <em>medio desordenado.</em>'),
    'fine_l': L('© 2026 María José Barney Ñañez', '© 2026 María José Barney Ñañez'),
    'fine_r': L('Client work shown with brand, prices and personal data removed.', 'El trabajo de clientes se muestra sin marca, precios ni datos personales.'),
}
