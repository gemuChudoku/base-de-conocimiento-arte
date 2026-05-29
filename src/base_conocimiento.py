# =============================================================
# BASE DE CONOCIMIENTO
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================
# Cada predicado representa una característica observable del
# usuario/proyecto. El motor de inferencia los evalúa para
# recomendar la herramienta más adecuada.
# =============================================================

PREDICADOS = {
    # --- Dispositivo disponible ---
    "tiene_ipad":            "El usuario tiene un iPad (cualquier modelo)",
    "tiene_tablet_android":  "El usuario tiene una tablet Android con lápiz",
    "tiene_pc_windows":      "El usuario trabaja en PC o laptop con Windows",
    "tiene_mac":             "El usuario trabaja en Mac (MacBook o iMac)",
    "tiene_tableta_grafica": "El usuario tiene una tableta gráfica (ej: Wacom) conectada al PC",

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
    "hace_animacion":        "El usuario quiere crear animaciones o GIFs",

    # --- Restricciones ---
    "presupuesto_bajo":      "El usuario prefiere herramientas gratuitas o de pago único bajo",
    "requiere_colaboracion": "El usuario necesita colaborar en tiempo real con otros",
}


REGLAS = [
    # ── GRUPO A: Recomendaciones para iPad ────────────────────

    {
        "nombre": "R1",
        "descripcion": "iPad + ilustración → Procreate",
        "condiciones": [
            ("tiene_ipad", True),
            ("hace_ilustracion", True),
        ],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.95,
        "justificacion": (
            "Procreate es la herramienta de ilustración más popular para iPad. "
            "Ofrece pinceles naturales, alto rendimiento y una curva de aprendizaje "
            "accesible tanto para principiantes como profesionales."
        ),
    },
    {
        "nombre": "R2",
        "descripcion": "iPad + manga/cómic → Clip Studio Paint",
        "condiciones": [
            ("tiene_ipad", True),
            ("hace_manga_comic", True),
        ],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.92,
        "justificacion": (
            "Clip Studio Paint es el estándar de la industria para manga y cómic. "
            "Disponible en iPad con funciones específicas como paneles, globos de "
            "diálogo y pinceles de tinta optimizados."
        ),
    },
    {
        "nombre": "R3",
        "descripcion": "iPad + concept art → Procreate",
        "condiciones": [
            ("tiene_ipad", True),
            ("hace_concept_art", True),
        ],
        "conclusion": ("recomendar_procreate", True),
        "certeza": 0.90,
        "justificacion": (
            "Procreate es ampliamente usado en la industria del entretenimiento "
            "para concept art gracias a su velocidad, portabilidad y pinceles "
            "personalizables que simulan medios tradicionales."
        ),
    },

    # ── GRUPO B: Recomendaciones para PC/Windows ──────────────

    {
        "nombre": "R4",
        "descripcion": "PC + presupuesto bajo + ilustración → Krita",
        "condiciones": [
            ("tiene_pc_windows", True),
            ("presupuesto_bajo", True),
            ("hace_ilustracion", True),
        ],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.93,
        "justificacion": (
            "Krita es gratuito y de código abierto, con herramientas profesionales "
            "de pintura digital. Es la alternativa libre más completa para "
            "ilustración y concept art en Windows."
        ),
    },
    {
        "nombre": "R5",
        "descripcion": "PC + tableta gráfica + profesional → Photoshop",
        "condiciones": [
            ("tiene_pc_windows", True),
            ("tiene_tableta_grafica", True),
            ("es_profesional", True),
        ],
        "conclusion": ("recomendar_photoshop", True),
        "certeza": 0.88,
        "justificacion": (
            "Adobe Photoshop es el estándar de la industria para retoque y "
            "pintura digital profesional. Con tableta gráfica, ofrece la "
            "experiencia más completa para artistas avanzados."
        ),
    },
    {
        "nombre": "R6",
        "descripcion": "PC + manga/cómic → Clip Studio Paint",
        "condiciones": [
            ("tiene_pc_windows", True),
            ("hace_manga_comic", True),
        ],
        "conclusion": ("recomendar_clip_studio", True),
        "certeza": 0.94,
        "justificacion": (
            "Clip Studio Paint en su versión de escritorio para Windows es la "
            "herramienta preferida por mangakas y artistas de cómic, con "
            "perspectivas 3D, paneles automáticos y tramas integradas."
        ),
    },
    {
        "nombre": "R7",
        "descripcion": "PC + animación + presupuesto bajo → Krita",
        "condiciones": [
            ("tiene_pc_windows", True),
            ("hace_animacion", True),
            ("presupuesto_bajo", True),
        ],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.80,
        "justificacion": (
            "Krita incluye un módulo de animación frame-by-frame completamente "
            "gratuito, ideal para quienes comienzan en animación 2D sin presupuesto."
        ),
    },

    # ── GRUPO C: Recomendaciones para vectorial ───────────────

    {
        "nombre": "R8",
        "descripcion": "Vectorial + profesional → Adobe Illustrator",
        "condiciones": [
            ("hace_vectorial", True),
            ("es_profesional", True),
        ],
        "conclusion": ("recomendar_illustrator", True),
        "certeza": 0.95,
        "justificacion": (
            "Adobe Illustrator es el software vectorial líder en la industria del "
            "diseño gráfico. Para uso profesional en logos, ilustración vectorial "
            "e impresión, no tiene rival en compatibilidad y funciones."
        ),
    },
    {
        "nombre": "R9",
        "descripcion": "Vectorial + presupuesto bajo → Inkscape",
        "condiciones": [
            ("hace_vectorial", True),
            ("presupuesto_bajo", True),
        ],
        "conclusion": ("recomendar_inkscape", True),
        "certeza": 0.88,
        "justificacion": (
            "Inkscape es la alternativa gratuita y de código abierto a Illustrator. "
            "Cubre el 90% de los casos de uso vectorial sin costo alguno, siendo "
            "ideal para principiantes e intermedios con presupuesto limitado."
        ),
    },
    {
        "nombre": "R10",
        "descripcion": "Vectorial + sin suscripción + profesional → Affinity Designer",
        "condiciones": [
            ("hace_vectorial", True),
            ("es_profesional", True),
            ("presupuesto_bajo", False),
        ],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.85,
        "justificacion": (
            "Affinity Designer ofrece capacidades profesionales de diseño vectorial "
            "con pago único (sin suscripción mensual), siendo una alternativa "
            "sólida a Illustrator para quienes rechazan el modelo de suscripción."
        ),
    },

    # ── GRUPO D: UI/UX y colaboración ────────────────────────

    {
        "nombre": "R11",
        "descripcion": "UI/UX → Figma",
        "condiciones": [
            ("hace_uiux", True),
        ],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": (
            "Figma es el estándar absoluto para diseño UI/UX. Funciona en el "
            "navegador, permite colaboración en tiempo real, prototipado interactivo "
            "y es gratuito para uso individual."
        ),
    },
    {
        "nombre": "R12",
        "descripcion": "Colaboración en tiempo real → Figma",
        "condiciones": [
            ("requiere_colaboracion", True),
            ("hace_uiux", True),
        ],
        "conclusion": ("recomendar_figma", True),
        "certeza": 0.97,
        "justificacion": (
            "Figma es la única herramienta de diseño con colaboración nativa en "
            "tiempo real comparable a Google Docs, siendo ideal para equipos de "
            "diseño que trabajan simultáneamente."
        ),
    },

    # ── GRUPO E: Mac ──────────────────────────────────────────

    {
        "nombre": "R13",
        "descripcion": "Mac + vectorial + profesional → Affinity Designer",
        "condiciones": [
            ("tiene_mac", True),
            ("hace_vectorial", True),
            ("es_profesional", True),
        ],
        "conclusion": ("recomendar_affinity", True),
        "certeza": 0.87,
        "justificacion": (
            "Affinity Designer en Mac ofrece rendimiento nativo excepcional "
            "con pago único, siendo la alternativa más popular a Illustrator "
            "entre diseñadores que usan ecosistema Apple."
        ),
    },

    # ── GRUPO F: Principiantes ────────────────────────────────

    {
        "nombre": "R14",
        "descripcion": "Principiante + PC + ilustración → Krita",
        "condiciones": [
            ("es_principiante", True),
            ("tiene_pc_windows", True),
            ("hace_ilustracion", True),
        ],
        "conclusion": ("recomendar_krita", True),
        "certeza": 0.91,
        "justificacion": (
            "Krita es la herramienta más recomendada para principiantes en PC: "
            "gratuita, con tutoriales abundantes, interfaz clara y sin la presión "
            "de una suscripción paga mientras se aprende."
        ),
    },
    {
        "nombre": "R15",
        "descripcion": "Principiante + tablet Android → Sketchbook",
        "condiciones": [
            ("es_principiante", True),
            ("tiene_tablet_android", True),
        ],
        "conclusion": ("recomendar_sketchbook", True),
        "certeza": 0.85,
        "justificacion": (
            "Autodesk Sketchbook es gratuito, intuitivo y disponible en Android. "
            "Su interfaz minimalista elimina la complejidad innecesaria, permitiendo "
            "que los principiantes se enfoquen en dibujar sin distracciones."
        ),
    },
]


# Mapeo de conclusiones a nombres legibles para la interfaz
NOMBRES_HERRAMIENTAS = {
    "recomendar_procreate":    "🎨 Procreate",
    "recomendar_clip_studio":  "📖 Clip Studio Paint",
    "recomendar_krita":        "🖌️ Krita",
    "recomendar_photoshop":    "📷 Adobe Photoshop",
    "recomendar_illustrator":  "✏️ Adobe Illustrator",
    "recomendar_inkscape":     "🔷 Inkscape",
    "recomendar_affinity":     "💎 Affinity Designer",
    "recomendar_figma":        "🖥️ Figma",
    "recomendar_sketchbook":   "📓 Autodesk Sketchbook",
}
