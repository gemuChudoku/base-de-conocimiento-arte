# =============================================================
# BASE DE CONOCIMIENTO v2
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================

PREDICADOS = {
    # --- Dispositivo disponible ---
    "tiene_ipad":            "El usuario tiene un iPad (cualquier modelo)",
    "tiene_tablet_android":  "El usuario tiene una tablet Android con lápiz",
    "tiene_pc_windows":      "El usuario trabaja en PC o laptop con Windows",
    "tiene_mac":             "El usuario trabaja en Mac (MacBook o iMac)",
    "tiene_tableta_grafica": "El usuario tiene una tableta gráfica (ej: Wacom) conectada al PC",
    "tiene_iphone":          "El usuario tiene un iPhone",
    "tiene_pc_potente":      "El usuario tiene un PC con buena GPU (para 3D/renderizado)",

    # --- Perfil y experiencia ---
    "es_principiante":       "El usuario está comenzando, sin experiencia previa en arte digital",
    "es_intermedio":         "El usuario tiene experiencia básica-media en arte digital",
    "es_profesional":        "El usuario trabaja o estudia arte/diseño de forma profesional",

    # --- Tipo de arte o uso ---
    "hace_ilustracion":      "El usuario quiere hacer ilustración digital (personajes, escenas)",
    "hace_vectorial":        "El usuario necesita trabajar con gráficos vectoriales (logos, íconos)",
    "hace_concept_art":      "El usuario quiere hacer concept art o arte conceptual",
    "hace_manga_comic":      "El usuario quiere hacer manga, cómic o novela gráfica",
    "hace_uiux":             "El usuario trabaja en diseño de interfaces (UI/UX)",
    "hace_animacion":        "El usuario quiere crear animaciones o GIFs frame-by-frame",
    "hace_animacion_2d":     "El usuario quiere hacer animación 2D avanzada con rigging",
    "hace_pixel_art":        "El usuario quiere crear pixel art (videojuegos retro, sprites)",
    "hace_modelado_3d":      "El usuario quiere modelar objetos o personajes en 3D",
    "hace_escultura_3d":     "El usuario quiere escultura digital (personajes orgánicos, criaturas)",
    "hace_render_3d":        "El usuario quiere crear renders fotorealistas o escenas 3D",
    "hace_arte_videojuegos": "El usuario crea assets o arte específicamente para videojuegos",

    # --- Restricciones ---
    "presupuesto_bajo":      "El usuario prefiere herramientas gratuitas o de pago único bajo",
    "requiere_colaboracion": "El usuario necesita colaborar en tiempo real con otros",
    "requiere_portabilidad": "El usuario necesita trabajar desde el móvil frecuentemente",
}


REGLAS = [
    # ══════════════════════════════════════════════════════════
    # GRUPO A: Aplicaciones para iPad
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R1",
        "descripcion": "iPad + ilustración → Procreate",
        "condiciones": [("tiene_ipad", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.95,
        "justificacion": (
            "Procreate es la herramienta de ilustración más popular para iPad. "
            "Ofrece pinceles naturales, alto rendimiento y curva de aprendizaje accesible."
        ),
    },
    {
        "nombre": "R2",
        "descripcion": "iPad + manga/cómic → Clip Studio Paint",
        "condiciones": [("tiene_ipad", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.92,
        "justificacion": (
            "Clip Studio Paint en iPad es el estándar para manga y cómic, "
            "con paneles automáticos, globos de diálogo y pinceles de tinta optimizados."
        ),
    },
    {
        "nombre": "R3",
        "descripcion": "iPad + concept art → Procreate",
        "condiciones": [("tiene_ipad", True), ("hace_concept_art", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.90,
        "justificacion": (
            "Procreate es ampliamente usado en la industria del entretenimiento "
            "para concept art gracias a su portabilidad y pinceles personalizables."
        ),
    },
    {
        "nombre": "R4",
        "descripcion": "iPad + animación avanzada → Procreate Dreams",
        "condiciones": [("tiene_ipad", True), ("hace_animacion_2d", True)],
        "conclusion": ("recomendar_procreate_dreams", True),
        "certeza": 0.88,
        "justificacion": (
            "Procreate Dreams es la app de animación 2D de los creadores de Procreate, "
            "diseñada específicamente para iPad con una línea de tiempo profesional."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO B: Móvil (iPhone / Android)
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R5",
        "descripcion": "Android + principiante → Sketchbook",
        "condiciones": [("tiene_tablet_android", True), ("es_principiante", True)],
        "conclusion": ("recomendar_sketchbook", True),
        "certeza": 0.85,
        "justificacion": (
            "Autodesk Sketchbook es gratuito e intuitivo en Android, ideal para "
            "principiantes que quieren empezar sin complejidad innecesaria."
        ),
    },
    {
        "nombre": "R6",
        "descripcion": "Android/iPhone + portabilidad + ilustración → Ibis Paint",
        "condiciones": [("requiere_portabilidad", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.87,
        "justificacion": (
            "Ibis Paint X es gratuita, disponible en Android e iPhone, muy popular "
            "para ilustración móvil con una gran biblioteca de pinceles y texturas."
        ),
    },
    {
        "nombre": "R7",
        "descripcion": "Portabilidad + manga/cómic → Ibis Paint",
        "condiciones": [("requiere_portabilidad", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.84,
        "justificacion": (
            "Ibis Paint X incluye herramientas específicas para manga como tramas, "
            "efectos de velocidad y paneles, siendo ideal para trabajar desde el móvil."
        ),
    },
    {
        "nombre": "R8",
        "descripcion": "iPhone + ilustración → Procreate",
        "condiciones": [("tiene_iphone", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.80,
        "justificacion": (
            "Procreate para iPhone (Procreate Pocket) ofrece las mismas capacidades "
            "de ilustración que la versión iPad, adaptada a pantalla pequeña."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO C: PC Windows - Ilustración y 2D
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R9",
        "descripcion": "PC + presupuesto bajo + ilustración → Krita",
        "condiciones": [("tiene_pc_windows", True), ("presupuesto_bajo", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.93,
        "justificacion": (
            "Krita es gratuito y open-source, con herramientas profesionales de pintura "
            "digital. La alternativa libre más completa para ilustración en Windows."
        ),
    },
    {
        "nombre": "R10",
        "descripcion": "PC + tableta gráfica + profesional → Photoshop",
        "condiciones": [("tiene_pc_windows", True), ("tiene_tableta_grafica", True), ("es_profesional", True)],
        "conclusion": ("recomendar_photoshop", True),
        "certeza": 0.88,
        "justificacion": (
            "Adobe Photoshop es el estándar de la industria para retoque y pintura "
            "digital profesional. Con tableta gráfica ofrece la experiencia más completa."
        ),
    },
    {
        "nombre": "R11",
        "descripcion": "PC + manga/cómic → Clip Studio Paint",
        "condiciones": [("tiene_pc_windows", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.94,
        "justificacion": (
            "Clip Studio Paint en Windows es la herramienta preferida por mangakas, "
            "con perspectivas 3D, paneles automáticos y tramas integradas."
        ),
    },
    {
        "nombre": "R12",
        "descripcion": "PC + animación frame-by-frame + presupuesto bajo → Krita",
        "condiciones": [("tiene_pc_windows", True), ("hace_animacion", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.80,
        "justificacion": (
            "Krita incluye un módulo de animación frame-by-frame completamente gratuito, "
            "ideal para quienes comienzan en animación 2D sin presupuesto."
        ),
    },
    {
        "nombre": "R13",
        "descripcion": "PC + principiante + ilustración → Krita",
        "condiciones": [("es_principiante", True), ("tiene_pc_windows", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.91,
        "justificacion": (
            "Krita es la herramienta más recomendada para principiantes en PC: "
            "gratuita, con tutoriales abundantes e interfaz clara."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO D: Animación 2D avanzada
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R14",
        "descripcion": "Animación 2D avanzada + PC → Spine",
        "condiciones": [("hace_animacion_2d", True), ("tiene_pc_windows", True)],
        "conclusion": ("recomendar_spine", True),
        "certeza": 0.91,
        "justificacion": (
            "Spine es el software de referencia para animación 2D con rigging y bones, "
            "muy usado en la industria de videojuegos para personajes animados."
        ),
    },
    {
        "nombre": "R15",
        "descripcion": "Animación 2D + arte videojuegos + presupuesto bajo → FlipaClip",
        "condiciones": [("hace_animacion_2d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_flipaclip", True),
        "certeza": 0.82,
        "justificacion": (
            "FlipaClip es una app gratuita de animación frame-by-frame disponible en "
            "Android e iOS, ideal para aprender animación 2D sin costo."
        ),
    },
    {
        "nombre": "R16",
        "descripcion": "Animación 2D + Mac → Spine o Krita",
        "condiciones": [("hace_animacion_2d", True), ("tiene_mac", True)],
        "conclusion": ("recomendar_spine", True),
        "certeza": 0.88,
        "justificacion": (
            "Spine está disponible en Mac y es la opción profesional para animación "
            "2D con rigging en el ecosistema Apple."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO E: Pixel Art
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R17",
        "descripcion": "Pixel art → Aseprite",
        "condiciones": [("hace_pixel_art", True)],
        "conclusion": ("recomendar_aseprite", True),
        "certeza": 0.97,
        "justificacion": (
            "Aseprite es el editor de pixel art más popular entre desarrolladores de "
            "videojuegos indie. Incluye animación frame-by-frame, capas y exportación "
            "a sprites. Es de pago único o compilable gratis desde el código fuente."
        ),
    },
    {
        "nombre": "R18",
        "descripcion": "Pixel art + arte videojuegos → Aseprite",
        "condiciones": [("hace_pixel_art", True), ("hace_arte_videojuegos", True)],
        "conclusion": ("recomendar_aseprite", True),
        "certeza": 0.97,
        "justificacion": (
            "Para assets de videojuegos en pixel art, Aseprite es el estándar absoluto. "
            "Su integración con motores como Unity y Godot es directa."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO F: Modelado y Escultura 3D
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R19",
        "descripcion": "Modelado 3D + presupuesto bajo → Blender",
        "condiciones": [("hace_modelado_3d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.97,
        "justificacion": (
            "Blender es completamente gratuito y open-source, con capacidades "
            "profesionales de modelado, rigging, animación y renderizado. "
            "Es la opción más completa del mercado para cualquier presupuesto."
        ),
    },
    {
        "nombre": "R20",
        "descripcion": "Modelado 3D + render fotorealista → Blender",
        "condiciones": [("hace_modelado_3d", True), ("hace_render_3d", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.93,
        "justificacion": (
            "Blender con Cycles o EEVEE produce renders fotorealistas de alta calidad. "
            "Es usado en producción cinematográfica y arquitectura."
        ),
    },
    {
        "nombre": "R21",
        "descripcion": "Modelado 3D + arte videojuegos + PC potente → Cinema 4D",
        "condiciones": [("hace_modelado_3d", True), ("hace_arte_videojuegos", True), ("tiene_pc_potente", True), ("es_profesional", True)],
        "conclusion": ("recomendar_cinema4d", True),
        "certeza": 0.85,
        "justificacion": (
            "Cinema 4D es el estándar en motion graphics y producción para videojuegos "
            "AAA. Su flujo de trabajo con motion graphics es superior al de Blender."
        ),
    },
    {
        "nombre": "R22",
        "descripcion": "Render 3D + profesional + PC potente → Cinema 4D",
        "condiciones": [("hace_render_3d", True), ("es_profesional", True), ("tiene_pc_potente", True)],
        "conclusion": ("recomendar_cinema4d", True),
        "certeza": 0.83,
        "justificacion": (
            "Cinema 4D con Redshift ofrece renders de nivel publicitario y "
            "cinematográfico, siendo muy usado en estudios de producción profesional."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO G: Escultura digital
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R23",
        "descripcion": "Escultura 3D + profesional → ZBrush",
        "condiciones": [("hace_escultura_3d", True), ("es_profesional", True)],
        "conclusion": ("recomendar_zbrush", True),
        "certeza": 0.96,
        "justificacion": (
            "ZBrush es el estándar de la industria para escultura digital. Usado en "
            "películas de Hollywood, videojuegos AAA y arte conceptual 3D. "
            "Permite trabajar con millones de polígonos de forma fluida."
        ),
    },
    {
        "nombre": "R24",
        "descripcion": "Escultura 3D + presupuesto bajo → Blender",
        "condiciones": [("hace_escultura_3d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.88,
        "justificacion": (
            "El modo de escultura de Blender es gratuito y cubre la mayoría de "
            "necesidades de escultura orgánica, siendo una excelente alternativa "
            "a ZBrush para quienes comienzan o tienen presupuesto limitado."
        ),
    },
    {
        "nombre": "R25",
        "descripcion": "Escultura 3D + arte videojuegos → ZBrush",
        "condiciones": [("hace_escultura_3d", True), ("hace_arte_videojuegos", True)],
        "conclusion": ("recomendar_zbrush", True),
        "certeza": 0.92,
        "justificacion": (
            "En la industria de videojuegos, ZBrush es la herramienta estándar para "
            "crear personajes de alta resolución que luego se retopoizan para el motor."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO H: Vectorial
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R26",
        "descripcion": "Vectorial + profesional → Illustrator",
        "condiciones": [("hace_vectorial", True), ("es_profesional", True)],
        "conclusion": ("recomendar_illustrator", True),
        "certeza": 0.95,
        "justificacion": (
            "Adobe Illustrator es el software vectorial líder en la industria del "
            "diseño gráfico para logos, ilustración vectorial e impresión."
        ),
    },
    {
        "nombre": "R27",
        "descripcion": "Vectorial + presupuesto bajo → Inkscape",
        "condiciones": [("hace_vectorial", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_inkscape", True),
        "certeza": 0.88,
        "justificacion": (
            "Inkscape es la alternativa gratuita y open-source a Illustrator. "
            "Cubre el 90% de los casos de uso vectorial sin costo alguno."
        ),
    },
    {
        "nombre": "R28",
        "descripcion": "Vectorial + profesional + sin suscripción → Affinity Designer",
        "condiciones": [("hace_vectorial", True), ("es_profesional", True), ("presupuesto_bajo", False)],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.85,
        "justificacion": (
            "Affinity Designer ofrece capacidades vectoriales profesionales "
            "con pago único, siendo la alternativa preferida a Illustrator "
            "para quienes rechazan el modelo de suscripción."
        ),
    },
    {
        "nombre": "R29",
        "descripcion": "Mac + vectorial + profesional → Affinity Designer",
        "condiciones": [("tiene_mac", True), ("hace_vectorial", True), ("es_profesional", True)],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.87,
        "justificacion": (
            "Affinity Designer en Mac ofrece rendimiento nativo excepcional "
            "con pago único, siendo muy popular entre diseñadores del ecosistema Apple."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO I: UI/UX y colaboración
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R30",
        "descripcion": "UI/UX → Figma",
        "condiciones": [("hace_uiux", True)],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": (
            "Figma es el estándar absoluto para diseño UI/UX. Funciona en el navegador, "
            "permite colaboración en tiempo real y es gratuito para uso individual."
        ),
    },
    {
        "nombre": "R31",
        "descripcion": "Colaboración + UI/UX → Figma",
        "condiciones": [("requiere_colaboracion", True), ("hace_uiux", True)],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": (
            "Figma es la única herramienta de diseño con colaboración nativa "
            "en tiempo real, ideal para equipos que trabajan simultáneamente."
        ),
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO J: Arte para videojuegos
    # ══════════════════════════════════════════════════════════

    {
        "nombre": "R32",
        "descripcion": "Arte videojuegos + ilustración + PC → Krita",
        "condiciones": [("hace_arte_videojuegos", True), ("hace_ilustracion", True), ("tiene_pc_windows", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.88,
        "justificacion": (
            "Krita es muy popular en la industria indie para crear concept art "
            "y assets 2D de videojuegos, siendo gratuito y compatible con PSD."
        ),
    },
    {
        "nombre": "R33",
        "descripcion": "Arte videojuegos + animación + presupuesto bajo → Align Motion",
        "condiciones": [("hace_arte_videojuegos", True), ("hace_animacion_2d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_align_motion", True),
        "certeza": 0.78,
        "justificacion": (
            "Align Motion es una herramienta accesible de animación 2D para "
            "videojuegos, orientada a artistas indie con presupuesto limitado."
        ),
    },
]


# ── Mapeo de conclusiones a nombres legibles ─────────────────
NOMBRES_HERRAMIENTAS = {
    "recomendar_procreate":        "🎨 Procreate",
    "recomendar_procreate_dreams": "🎬 Procreate Dreams",
    "recomendar_clip_studio":      "📖 Clip Studio Paint",
    "recomendar_krita":            "🖌️ Krita",
    "recomendar_photoshop":        "📷 Adobe Photoshop",
    "recomendar_illustrator":      "✏️ Adobe Illustrator",
    "recomendar_inkscape":         "🔷 Inkscape",
    "recomendar_affinity":         "💎 Affinity Designer",
    "recomendar_figma":            "🖥️ Figma",
    "recomendar_sketchbook":       "📓 Autodesk Sketchbook",
    "recomendar_ibis_paint":       "📱 Ibis Paint X",
    "recomendar_blender":          "🟠 Blender",
    "recomendar_cinema4d":         "🎥 Cinema 4D",
    "recomendar_zbrush":           "🗿 ZBrush",
    "recomendar_aseprite":         "👾 Aseprite",
    "recomendar_spine":            "🦴 Spine",
    "recomendar_flipaclip":        "✍️ FlipaClip",
    "recomendar_align_motion":     "⚡ Align Motion",
}
