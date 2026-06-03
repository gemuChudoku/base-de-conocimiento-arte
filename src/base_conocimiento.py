# =============================================================
# BASE DE CONOCIMIENTO v3
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================

PREDICADOS = {
    # --- Dispositivo disponible ---
    "tiene_ipad":            "El usuario tiene un iPad (cualquier modelo)",
    "tiene_tablet_android":  "El usuario tiene una tablet Android con lápiz",
    "tiene_pc_windows":      "El usuario trabaja en PC o laptop con Windows",
    "tiene_mac":             "El usuario trabaja en Mac (MacBook o iMac)",
    "tiene_tableta_grafica": "El usuario tiene una tableta gráfica (ej: Wacom)",
    "tiene_iphone":          "El usuario tiene un iPhone",
    "tiene_pc_potente":      "El usuario tiene un PC con buena GPU (para 3D)",

    # --- Nivel de experiencia ---
    "es_principiante":       "El usuario está comenzando sin experiencia previa",
    "es_intermedio":         "El usuario tiene experiencia básica-media",
    "es_profesional":        "El usuario trabaja o estudia arte/diseño profesionalmente",

    # --- Tipo de arte 2D ---
    "hace_ilustracion":      "El usuario quiere hacer ilustración digital",
    "hace_vectorial":        "El usuario necesita trabajar con gráficos vectoriales",
    "hace_concept_art":      "El usuario quiere hacer concept art",
    "hace_manga_comic":      "El usuario quiere hacer manga, cómic o novela gráfica",
    "hace_uiux":             "El usuario trabaja en diseño de interfaces UI/UX",
    "hace_animacion":        "El usuario quiere crear animaciones frame-by-frame",
    "hace_animacion_2d":     "El usuario quiere animación 2D avanzada con rigging",
    "hace_pixel_art":        "El usuario quiere crear pixel art",

    # --- Tipo de arte 3D ---
    "hace_modelado_3d":      "El usuario quiere modelar objetos o personajes en 3D",
    "hace_escultura_3d":     "El usuario quiere escultura digital orgánica",
    "hace_render_3d":        "El usuario quiere renderizado 3D fotorealista",
    "hace_arte_videojuegos": "El usuario crea assets o arte para videojuegos",

    # --- Objetivo del proyecto ---
    "objetivo_personal":     "El proyecto es de uso personal u hobby",
    "objetivo_profesional":  "El proyecto tiene fines profesionales o laborales",
    "objetivo_educativo":    "El proyecto es para aprendizaje o estudio",
    "objetivo_freelance":    "El proyecto es para trabajo freelance o clientes",

    # --- Industria o sector ---
    "sector_videojuegos":    "El usuario trabaja o apunta al sector de videojuegos",
    "sector_cine_tv":        "El usuario trabaja o apunta al sector de cine o TV",
    "sector_redes_sociales": "El contenido es principalmente para redes sociales",
    "sector_impresion":      "El trabajo es para impresión (editorial, merchandising)",

    # --- Tiempo disponible para aprender ---
    "tiempo_poco":           "El usuario tiene poco tiempo para aprender (quiere algo intuitivo)",
    "tiempo_moderado":       "El usuario tiene tiempo moderado para aprender",
    "tiempo_mucho":          "El usuario tiene mucho tiempo y disposición para aprender",

    # --- Restricciones ---
    "presupuesto_bajo":      "El usuario prefiere herramientas gratuitas o pago único bajo",
    "requiere_colaboracion": "El usuario necesita colaborar en tiempo real",
    "requiere_portabilidad": "El usuario necesita trabajar desde el móvil frecuentemente",
}


REGLAS = [
    # ══════════════════════════════════════════════════════════
    # GRUPO A: iPad
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R1",
        "descripcion": "iPad + ilustración → Procreate",
        "condiciones": [("tiene_ipad", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.95,
        "justificacion": "Procreate es la herramienta de ilustración más popular para iPad, con pinceles naturales y alto rendimiento.",
    },
    {
        "nombre": "R2",
        "descripcion": "iPad + manga/cómic → Clip Studio Paint",
        "condiciones": [("tiene_ipad", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.92,
        "justificacion": "Clip Studio Paint en iPad es el estándar para manga con paneles automáticos y pinceles de tinta.",
    },
    {
        "nombre": "R3",
        "descripcion": "iPad + concept art → Procreate",
        "condiciones": [("tiene_ipad", True), ("hace_concept_art", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.90,
        "justificacion": "Procreate es muy usado en la industria del entretenimiento para concept art por su portabilidad.",
    },
    {
        "nombre": "R4",
        "descripcion": "iPad + animación 2D avanzada → Procreate Dreams",
        "condiciones": [("tiene_ipad", True), ("hace_animacion_2d", True)],
        "conclusion": ("recomendar_procreate_dreams", True),
        "certeza": 0.88,
        "justificacion": "Procreate Dreams es la app de animación 2D de los creadores de Procreate, diseñada para iPad.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO B: Móvil y portabilidad
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R5",
        "descripcion": "Android + principiante → Sketchbook",
        "condiciones": [("tiene_tablet_android", True), ("es_principiante", True)],
        "conclusion": ("recomendar_sketchbook", True),
        "certeza": 0.85,
        "justificacion": "Sketchbook es gratuito e intuitivo en Android, ideal para principiantes sin complejidad.",
    },
    {
        "nombre": "R6",
        "descripcion": "andriod + ios + Portabilidad + ilustración + concept art → Ibis Paint",
        "condiciones": [("tiene_tablet_android", True), ("tiene_iphone", True),("requiere_portabilidad", True), ("hace_ilustracion", True), ("hace_concept_art", True),("es_principiante", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.87,
        "justificacion": "Ibis Paint X es gratuita en Android e iPhone, muy popular para ilustración móvil.",
    },
    {
        "nombre": "R7",
        "descripcion": "Portabilidad + manga → Ibis Paint",
        "condiciones": [("requiere_portabilidad", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.84,
        "justificacion": "Ibis Paint incluye tramas y herramientas de manga, ideal para trabajar desde el móvil.",
    },
    {
        "nombre": "R8",
        "descripcion": "Portabilidad + redes sociales + poco tiempo → Ibis Paint",
        "condiciones": [("requiere_portabilidad", True), ("sector_redes_sociales", True), ("tiempo_poco", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.86,
        "justificacion": "Ibis Paint es ideal para crear contenido rápido para redes sociales desde el móvil.",
    },
    {
        "nombre": "R9",
        "descripcion": "iPhone + ilustración → Procreate",
        "condiciones": [("tiene_iphone", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.80,
        "justificacion": "Procreate Pocket para iPhone ofrece las mismas capacidades adaptadas a pantalla pequeña.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO C: PC Windows — 2D
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R10",
        "descripcion": "PC + presupuesto bajo + ilustración → Krita",
        "condiciones": [("tiene_pc_windows", True), ("presupuesto_bajo", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.93,
        "justificacion": "Krita es gratuito y open-source, la alternativa libre más completa para ilustración en Windows.",
    },
    {
        "nombre": "R11",
        "descripcion": "PC + tableta gráfica + profesional → Photoshop",
        "condiciones": [("tiene_pc_windows", True), ("tiene_tableta_grafica", True), ("es_profesional", True)],
        "conclusion": ("recomendar_photoshop", True),
        "certeza": 0.88,
        "justificacion": "Photoshop con tableta gráfica es el estándar profesional para pintura digital e ilustración.",
    },
    {
        "nombre": "R12",
        "descripcion": "PC + manga/cómic → Clip Studio Paint",
        "condiciones": [("tiene_pc_windows", True), ("hace_manga_comic", True)],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.94,
        "justificacion": "Clip Studio Paint en Windows es la herramienta preferida por mangakas y artistas de cómic.",
    },
    {
        "nombre": "R13",
        "descripcion": "PC + animación + presupuesto bajo → Krita",
        "condiciones": [("tiene_pc_windows", True), ("hace_animacion", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.80,
        "justificacion": "Krita incluye animación frame-by-frame gratuita, ideal para comenzar sin presupuesto.",
    },
    {
        "nombre": "R14",
        "descripcion": "PC + principiante + poco tiempo → Krita",
        "condiciones": [("es_principiante", True), ("tiene_pc_windows", True), ("tiempo_poco", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.89,
        "justificacion": "Krita tiene una curva de aprendizaje accesible y tutoriales abundantes para principiantes.",
    },
    {
        "nombre": "R15",
        "descripcion": "PC + educativo + ilustración → Krita",
        "condiciones": [("tiene_pc_windows", True), ("objetivo_educativo", True), ("hace_ilustracion", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.91,
        "justificacion": "Krita es gratuito y muy usado en instituciones educativas para enseñar arte digital.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO D: Animación 2D avanzada
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R16",
        "descripcion": "Animación 2D + PC → Spine",
        "condiciones": [("hace_animacion_2d", True), ("tiene_pc_windows", True)],
        "conclusion": ("recomendar_spine", True),
        "certeza": 0.91,
        "justificacion": "Spine es el software de referencia para animación 2D con rigging en videojuegos.",
    },
    {
        "nombre": "R17",
        "descripcion": "Animación 2D + presupuesto bajo → FlipaClip",
        "condiciones": [("hace_animacion_2d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_flipaclip", True),
        "certeza": 0.82,
        "justificacion": "FlipaClip es gratuito para Android e iOS, ideal para aprender animación 2D sin costo.",
    },
    {
        "nombre": "R18",
        "descripcion": "Animación 2D + Mac → Spine",
        "condiciones": [("hace_animacion_2d", True), ("tiene_mac", True)],
        "conclusion": ("recomendar_spine", True),
        "certeza": 0.88,
        "justificacion": "Spine está disponible en Mac y es la opción profesional para animación 2D con rigging.",
    },
    {
        "nombre": "R19",
        "descripcion": "Animación 2D + cine/TV + profesional → Spine",
        "condiciones": [("hace_animacion_2d", True), ("sector_cine_tv", True), ("es_profesional", True)],
        "conclusion": ("recomendar_spine", True),
        "certeza": 0.90,
        "justificacion": "Spine es usado en producción de series animadas y películas 2D a nivel profesional.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO E: Pixel art
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R20",
        "descripcion": "Pixel art → Aseprite",
        "condiciones": [("hace_pixel_art", True)],
        "conclusion": ("recomendar_aseprite", True),
        "certeza": 0.97,
        "justificacion": "Aseprite es el editor de pixel art más popular, con animación frame-by-frame y exportación a sprites.",
    },
    {
        "nombre": "R21",
        "descripcion": "Pixel art + videojuegos → Aseprite",
        "condiciones": [("hace_pixel_art", True), ("sector_videojuegos", True)],
        "conclusion": ("recomendar_aseprite", True),
        "certeza": 0.97,
        "justificacion": "Para assets de videojuegos en pixel art, Aseprite es el estándar con integración directa a Unity y Godot.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO F: Modelado y escultura 3D
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R22",
        "descripcion": "Modelado 3D + presupuesto bajo → Blender",
        "condiciones": [("hace_modelado_3d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.97,
        "justificacion": "Blender es gratuito y open-source con capacidades profesionales de modelado, rigging y renderizado.",
    },
    {
        "nombre": "R23",
        "descripcion": "Modelado 3D + render → Blender",
        "condiciones": [("hace_modelado_3d", True), ("hace_render_3d", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.93,
        "justificacion": "Blender con Cycles produce renders fotorealistas de alta calidad usados en producción cinematográfica.",
    },
    {
        "nombre": "R24",
        "descripcion": "Modelado 3D + cine/TV + profesional + PC potente → Cinema 4D",
        "condiciones": [("hace_modelado_3d", True), ("sector_cine_tv", True), ("es_profesional", True), ("tiene_pc_potente", True)],
        "conclusion": ("recomendar_cinema4d", True),
        "certeza": 0.87,
        "justificacion": "Cinema 4D es el estándar en motion graphics y producción para cine y TV a nivel profesional.",
    },
    {
        "nombre": "R25",
        "descripcion": "Modelado 3D + videojuegos + profesional + PC potente → Cinema 4D",
        "condiciones": [("hace_modelado_3d", True), ("sector_videojuegos", True), ("es_profesional", True), ("tiene_pc_potente", True)],
        "conclusion": ("recomendar_cinema4d", True),
        "certeza": 0.85,
        "justificacion": "Cinema 4D es usado en estudios de videojuegos AAA para modelado y motion graphics.",
    },
    {
        "nombre": "R26",
        "descripcion": "Escultura 3D + profesional → ZBrush",
        "condiciones": [("hace_escultura_3d", True), ("es_profesional", True)],
        "conclusion": ("recomendar_zbrush", True),
        "certeza": 0.96,
        "justificacion": "ZBrush es el estándar de la industria para escultura digital en películas y videojuegos AAA.",
    },
    {
        "nombre": "R27",
        "descripcion": "Escultura 3D + presupuesto bajo → Blender",
        "condiciones": [("hace_escultura_3d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.88,
        "justificacion": "El módulo de escultura de Blender es gratuito y cubre la mayoría de necesidades orgánicas.",
    },
    {
        "nombre": "R28",
        "descripcion": "Escultura 3D + videojuegos → ZBrush",
        "condiciones": [("hace_escultura_3d", True), ("sector_videojuegos", True)],
        "conclusion": ("recomendar_zbrush", True),
        "certeza": 0.92,
        "justificacion": "ZBrush es la herramienta estándar para personajes de alta resolución en la industria de videojuegos.",
    },
    {
        "nombre": "R29",
        "descripcion": "Modelado 3D + educativo + tiempo moderado → Blender",
        "condiciones": [("hace_modelado_3d", True), ("objetivo_educativo", True), ("tiempo_moderado", True)],
        "conclusion": ("recomendar_blender", True),
        "certeza": 0.92,
        "justificacion": "Blender tiene la comunidad educativa más grande del software 3D, con cursos gratuitos y documentación extensa.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO G: Vectorial
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R30",
        "descripcion": "Vectorial + profesional → Illustrator",
        "condiciones": [("hace_vectorial", True), ("es_profesional", True)],
        "conclusion": ("recomendar_illustrator", True),
        "certeza": 0.95,
        "justificacion": "Adobe Illustrator es el estándar para diseño vectorial profesional en logos e impresión.",
    },
    {
        "nombre": "R31",
        "descripcion": "Vectorial + impresión + freelance → Illustrator",
        "condiciones": [("hace_vectorial", True), ("sector_impresion", True), ("objetivo_freelance", True)],
        "conclusion": ("recomendar_illustrator", True),
        "certeza": 0.93,
        "justificacion": "Para trabajo freelance en impresión editorial, Illustrator es el formato que todos los clientes esperan.",
    },
    {
        "nombre": "R32",
        "descripcion": "Vectorial + presupuesto bajo → Inkscape",
        "condiciones": [("hace_vectorial", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_inkscape", True),
        "certeza": 0.88,
        "justificacion": "Inkscape es la alternativa gratuita y open-source a Illustrator, cubre el 90% de los casos de uso.",
    },
    {
        "nombre": "R33",
        "descripcion": "Vectorial + profesional + sin suscripción → Affinity Designer",
        "condiciones": [("hace_vectorial", True), ("es_profesional", True), ("presupuesto_bajo", False)],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.85,
        "justificacion": "Affinity Designer ofrece capacidades vectoriales profesionales con pago único sin suscripción.",
    },
    {
        "nombre": "R34",
        "descripcion": "Mac + vectorial + profesional → Affinity Designer",
        "condiciones": [("tiene_mac", True), ("hace_vectorial", True), ("es_profesional", True)],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.87,
        "justificacion": "Affinity Designer en Mac ofrece rendimiento nativo excepcional con pago único.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO H: UI/UX
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R35",
        "descripcion": "UI/UX → Figma",
        "condiciones": [("hace_uiux", True)],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": "Figma es el estándar absoluto para UI/UX con colaboración en tiempo real y prototipado.",
    },
    {
        "nombre": "R36",
        "descripcion": "Colaboración + UI/UX → Figma",
        "condiciones": [("requiere_colaboracion", True), ("hace_uiux", True)],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": "Figma es la única herramienta de diseño con colaboración nativa en tiempo real.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO I: Arte para videojuegos
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R37",
        "descripcion": "Videojuegos + ilustración + PC → Krita",
        "condiciones": [("sector_videojuegos", True), ("hace_ilustracion", True), ("tiene_pc_windows", True)],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.88,
        "justificacion": "Krita es muy popular en la industria indie para concept art y assets 2D compatibles con PSD.",
    },
    {
        "nombre": "R38",
        "descripcion": "Videojuegos + animación 2D + presupuesto bajo → Align Motion",
        "condiciones": [("sector_videojuegos", True), ("hace_animacion_2d", True), ("presupuesto_bajo", True)],
        "conclusion": ("recomendar_align_motion", True),
        "certeza": 0.78,
        "justificacion": "Align Motion es una herramienta accesible de animación 2D orientada a artistas indie.",
    },

    # ══════════════════════════════════════════════════════════
    # GRUPO J: Objetivo y tiempo — reglas cruzadas
    # ══════════════════════════════════════════════════════════
    {
        "nombre": "R39",
        "descripcion": "Freelance + ilustración + profesional → Photoshop",
        "condiciones": [("objetivo_freelance", True), ("hace_ilustracion", True), ("es_profesional", True)],
        "conclusion": ("recomendar_photoshop", True),
        "certeza": 0.87,
        "justificacion": "Para freelancers profesionales, Photoshop es el formato universal que los clientes esperan recibir.",
    },
    {
        "nombre": "R40",
        "descripcion": "Redes sociales + ilustración + poco tiempo → Ibis Paint",
        "condiciones": [("sector_redes_sociales", True), ("hace_ilustracion", True), ("tiempo_poco", True)],
        "conclusion": ("recomendar_ibis_paint", True),
        "certeza": 0.83,
        "justificacion": "Ibis Paint permite crear ilustraciones para redes sociales de forma rápida desde cualquier dispositivo.",
    },
    {
        "nombre": "R41",
        "descripcion": "Educativo + pixel art + tiempo moderado → Aseprite",
        "condiciones": [("objetivo_educativo", True), ("hace_pixel_art", True), ("tiempo_moderado", True)],
        "conclusion": ("recomendar_aseprite", True),
        "certeza": 0.90,
        "justificacion": "Aseprite es fácil de aprender y muy usado en cursos de desarrollo de videojuegos indie.",
    },
    {
        "nombre": "R42",
        "descripcion": "Personal + poco tiempo + principiante → Sketchbook",
        "condiciones": [("objetivo_personal", True), ("tiempo_poco", True), ("es_principiante", True)],
        "conclusion": ("recomendar_sketchbook", True),
        "certeza": 0.84,
        "justificacion": "Sketchbook tiene la interfaz más simple del mercado, ideal para comenzar a dibujar digitalmente sin presión.",
    },
    {
        "nombre": "R43",
        "descripcion": "Impresión + vectorial + tiempo mucho → Illustrator",
        "condiciones": [("sector_impresion", True), ("hace_vectorial", True), ("tiempo_mucho", True)],
        "conclusion": ("recomendar_illustrator", True),
        "certeza": 0.91,
        "justificacion": "Si hay tiempo para aprender, Illustrator es la inversión más rentable para trabajo de impresión profesional.",
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
