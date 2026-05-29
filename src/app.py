# =============================================================
# INTERFAZ WEB - STREAMLIT
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================
# Para ejecutar:
#   cd src
#   streamlit run app.py
# =============================================================

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from base_conocimiento import REGLAS, PREDICADOS, NOMBRES_HERRAMIENTAS
from motor_inferencia import (
    encadenamiento_adelante,
    explicar_razonamiento,
    porque,
    obtener_recomendaciones,
)

# ── Configuración de la página ────────────────────────────────
st.set_page_config(
    page_title="Recomendador de Herramienta de Dibujo",
    page_icon="🎨",
    layout="wide",
)

# ── Estilos personalizados ────────────────────────────────────
st.markdown("""
<style>
    .titulo-principal {
        font-size: 2rem;
        font-weight: 700;
        color: #4A90D9;
        margin-bottom: 0.2rem;
    }
    .subtitulo {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    .recomendacion-card {
        background: linear-gradient(135deg, #667eea22, #764ba222);
        border: 2px solid #667eea;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        font-size: 1.2rem;
        font-weight: 600;
    }
    .certeza-badge {
        background-color: #28a74522;
        border: 1px solid #28a745;
        border-radius: 8px;
        padding: 0.2rem 0.6rem;
        font-size: 0.85rem;
        color: #28a745;
    }
    .sin-resultado {
        background-color: #ffc10722;
        border: 1px solid #ffc107;
        border-radius: 10px;
        padding: 1rem;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)


# ── Encabezado ────────────────────────────────────────────────
st.markdown('<p class="titulo-principal">🎨 Recomendador de Herramienta de Dibujo Digital</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Responde las preguntas sobre tu perfil y el sistema experto te recomendará la herramienta más adecuada.</p>', unsafe_allow_html=True)
st.divider()

# ── Sidebar: casos de prueba precargados ─────────────────────
with st.sidebar:
    st.header("🧪 Casos de prueba")
    st.caption("Carga un caso de ejemplo para probar el sistema.")

    casos = {
        "— Seleccionar —": None,
        "Caso 1: Ilustrador con iPad": {
            "tiene_ipad": True, "hace_ilustracion": True,
        },
        "Caso 2: Diseñador UI/UX profesional": {
            "tiene_pc_windows": True, "hace_uiux": True,
            "es_profesional": True, "requiere_colaboracion": True,
        },
        "Caso 3: Principiante con PC sin presupuesto": {
            "tiene_pc_windows": True, "es_principiante": True,
            "hace_ilustracion": True, "presupuesto_bajo": True,
        },
        "Caso 4: Artista de manga en PC": {
            "tiene_pc_windows": True, "hace_manga_comic": True,
            "tiene_tableta_grafica": True,
        },
        "Caso 5: Sin coincidencias (caso borde)": {
            "tiene_tablet_android": True, "hace_animacion": True,
        },
    }

    caso_seleccionado = st.selectbox("Cargar caso:", list(casos.keys()))

    if casos[caso_seleccionado]:
        st.caption("Hechos del caso:")
        for pred, val in casos[caso_seleccionado].items():
            icono = "✅" if val else "❌"
            st.write(f"{icono} {PREDICADOS.get(pred, pred)}")

    st.divider()
    st.caption("💡 Puedes cargar un caso y luego ajustarlo manualmente.")


# ── Layout principal: dos columnas ───────────────────────────
col_entrada, col_resultados = st.columns([1, 1], gap="large")

# ── COLUMNA IZQUIERDA: Formulario de entrada ──────────────────
with col_entrada:
    st.subheader("📝 Características del usuario")

    # Prepoblar con el caso seleccionado si existe
    caso_datos = casos.get(caso_seleccionado) or {}

    st.markdown("**💻 Dispositivo disponible**")
    tiene_ipad           = st.checkbox("Tengo un iPad", value=caso_datos.get("tiene_ipad", False))
    tiene_tablet_android = st.checkbox("Tengo tablet Android con lápiz", value=caso_datos.get("tiene_tablet_android", False))
    tiene_pc_windows     = st.checkbox("Trabajo en PC/laptop con Windows", value=caso_datos.get("tiene_pc_windows", False))
    tiene_mac            = st.checkbox("Trabajo en Mac", value=caso_datos.get("tiene_mac", False))
    tiene_tableta_grafica= st.checkbox("Tengo tableta gráfica (Wacom u otra)", value=caso_datos.get("tiene_tableta_grafica", False))

    st.markdown("**🎓 Nivel de experiencia**")
    nivel = st.radio(
        "¿Cuál describe mejor tu nivel?",
        ["Principiante", "Intermedio", "Profesional"],
        index=["Principiante", "Intermedio", "Profesional"].index(
            "Principiante" if caso_datos.get("es_principiante") else
            "Profesional"  if caso_datos.get("es_profesional")  else
            "Intermedio"
        ),
        horizontal=True,
    )
    es_principiante = nivel == "Principiante"
    es_intermedio   = nivel == "Intermedio"
    es_profesional  = nivel == "Profesional"

    st.markdown("**🖼️ Tipo de arte o uso**")
    hace_ilustracion = st.checkbox("Ilustración digital (personajes, escenas)", value=caso_datos.get("hace_ilustracion", False))
    hace_vectorial   = st.checkbox("Gráficos vectoriales (logos, íconos)",      value=caso_datos.get("hace_vectorial", False))
    hace_concept_art = st.checkbox("Concept art / arte conceptual",              value=caso_datos.get("hace_concept_art", False))
    hace_manga_comic = st.checkbox("Manga, cómic o novela gráfica",              value=caso_datos.get("hace_manga_comic", False))
    hace_uiux        = st.checkbox("Diseño de interfaces (UI/UX)",               value=caso_datos.get("hace_uiux", False))
    hace_animacion   = st.checkbox("Animación o GIFs",                           value=caso_datos.get("hace_animacion", False))

    st.markdown("**⚙️ Restricciones**")
    presupuesto_bajo      = st.checkbox("Prefiero herramientas gratuitas o de pago único bajo", value=caso_datos.get("presupuesto_bajo", False))
    requiere_colaboracion = st.checkbox("Necesito colaborar en tiempo real con otros",           value=caso_datos.get("requiere_colaboracion", False))

    # Validación: debe seleccionarse al menos un dispositivo y un tipo de arte
    dispositivo_seleccionado = any([tiene_ipad, tiene_tablet_android, tiene_pc_windows, tiene_mac])
    tipo_seleccionado        = any([hace_ilustracion, hace_vectorial, hace_concept_art, hace_manga_comic, hace_uiux, hace_animacion])

    if not dispositivo_seleccionado:
        st.warning("⚠️ Selecciona al menos un dispositivo.")
    if not tipo_seleccionado:
        st.warning("⚠️ Selecciona al menos un tipo de arte o uso.")

    ejecutar = st.button(
        "🔍 Obtener recomendación",
        type="primary",
        use_container_width=True,
        disabled=not (dispositivo_seleccionado and tipo_seleccionado),
    )

# ── COLUMNA DERECHA: Resultados ───────────────────────────────
with col_resultados:
    st.subheader("🏆 Resultados")

    if ejecutar:
        # Construir diccionario de hechos iniciales
        hechos_iniciales = {
            "tiene_ipad":            tiene_ipad,
            "tiene_tablet_android":  tiene_tablet_android,
            "tiene_pc_windows":      tiene_pc_windows,
            "tiene_mac":             tiene_mac,
            "tiene_tableta_grafica": tiene_tableta_grafica,
            "es_principiante":       es_principiante,
            "es_intermedio":         es_intermedio,
            "es_profesional":        es_profesional,
            "hace_ilustracion":      hace_ilustracion,
            "hace_vectorial":        hace_vectorial,
            "hace_concept_art":      hace_concept_art,
            "hace_manga_comic":      hace_manga_comic,
            "hace_uiux":             hace_uiux,
            "hace_animacion":        hace_animacion,
            "presupuesto_bajo":      presupuesto_bajo,
            "requiere_colaboracion": requiere_colaboracion,
        }

        # Guardar en session_state para usar en las pestañas de explicación
        st.session_state["hechos_iniciales"] = hechos_iniciales

        with st.spinner("Analizando tu perfil..."):
            hechos_finales, reglas_aplicadas = encadenamiento_adelante(REGLAS, hechos_iniciales)
            recomendaciones = obtener_recomendaciones(hechos_finales, hechos_iniciales)

        st.session_state["hechos_finales"]   = hechos_finales
        st.session_state["reglas_aplicadas"] = reglas_aplicadas
        st.session_state["recomendaciones"]  = recomendaciones

    # Mostrar resultados si existen en session_state
    if "recomendaciones" in st.session_state:
        recomendaciones  = st.session_state["recomendaciones"]
        reglas_aplicadas = st.session_state["reglas_aplicadas"]

        if recomendaciones:
            st.success(f"✅ Se encontraron {len(recomendaciones)} recomendación(es):")
            for pred in recomendaciones:
                nombre = NOMBRES_HERRAMIENTAS.get(pred, pred)
                # Buscar certeza de la regla que originó esta recomendación
                certeza = next(
                    (r["certeza"] for r in reglas_aplicadas if r["conclusion"][0] == pred),
                    None
                )
                st.markdown(
                    f'<div class="recomendacion-card">{nombre} '
                    f'<span class="certeza-badge">FC: {certeza}</span></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div class="sin-resultado">⚠️ No se pudo generar una recomendación con las '
                'características seleccionadas. Intente agregar más detalles sobre su perfil.</div>',
                unsafe_allow_html=True,
            )

        # ── Sección de explicación ────────────────────────────
        st.divider()
        st.subheader("🔍 Explicación del razonamiento")

        tab1, tab2, tab3 = st.tabs(["📋 Cadena completa", "❓ ¿Por qué?", "📊 Reglas aplicadas"])

        with tab1:
            explicacion = explicar_razonamiento(reglas_aplicadas)
            st.text(explicacion)

        with tab2:
            if recomendaciones:
                herramienta_seleccionada = st.selectbox(
                    "Selecciona una recomendación para explicar:",
                    recomendaciones,
                    format_func=lambda x: NOMBRES_HERRAMIENTAS.get(x, x),
                )
                if herramienta_seleccionada:
                    explicacion_porque = porque(herramienta_seleccionada, reglas_aplicadas)
                    st.text(explicacion_porque)
            else:
                st.info("No hay recomendaciones que explicar.")

        with tab3:
            if reglas_aplicadas:
                st.write(f"**Total de reglas disparadas:** {len(reglas_aplicadas)}")
                for reg in reglas_aplicadas:
                    with st.expander(f"Regla {reg['regla']}: {reg['descripcion']}"):
                        st.write(f"**Certeza:** {reg['certeza']}")
                        st.write(f"**Iteración:** {reg['iteracion']}")
                        st.write("**Condiciones:**")
                        for pred, val in reg["condiciones"]:
                            icono = "✅" if val else "❌"
                            st.write(f"  {icono} {PREDICADOS.get(pred, pred)}")
                        pred_c, val_c = reg["conclusion"]
                        st.write(f"**Conclusión:** {pred_c} = {val_c}")
                        st.write(f"**Justificación:** {reg['justificacion']}")
            else:
                st.info("No se aplicaron reglas.")

        # ── Botón de reseteo ──────────────────────────────────
        st.divider()
        if st.button("🔄 Limpiar y empezar de nuevo", use_container_width=True):
            for key in ["hechos_iniciales", "hechos_finales", "reglas_aplicadas", "recomendaciones"]:
                st.session_state.pop(key, None)
            st.rerun()

    else:
        st.info("👈 Completa el formulario y presiona **Obtener recomendación**.")
