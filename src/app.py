# =============================================================
# INTERFAZ WEB - STREAMLIT v3
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from base_conocimiento import REGLAS, PREDICADOS, NOMBRES_HERRAMIENTAS
from motor_inferencia import (
    encadenamiento_adelante, explicar_razonamiento,
    porque, obtener_recomendaciones,
)

st.set_page_config(page_title="Recomendador de Herramienta de Dibujo", page_icon="🎨", layout="wide")

st.markdown("""
<style>
    .titulo-principal { font-size: 2rem; font-weight: 700; color: #4A90D9; }
    .subtitulo { font-size: 1rem; color: #666; margin-bottom: 1rem; }
    .seccion-label { font-weight: 700; color: #2E5FA3; font-size: 0.95rem;
                     margin-top: 1rem; margin-bottom: 0.2rem; border-left: 3px solid #4A90D9;
                     padding-left: 8px; }
    .recomendacion-card { background: linear-gradient(135deg,#667eea22,#764ba222);
        border: 2px solid #667eea; border-radius: 12px;
        padding: 0.8rem 1.2rem; margin: 0.4rem 0; font-size: 1.1rem; font-weight: 600; }
    .certeza-badge { background-color:#28a74522; border:1px solid #28a745;
        border-radius:8px; padding:0.2rem 0.5rem; font-size:0.8rem; color:#28a745; }
    .sin-resultado { background-color:#ffc10722; border:1px solid #ffc107;
        border-radius:10px; padding:1rem; color:#856404; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo-principal">🎨 Recomendador de Herramienta de Dibujo Digital</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Describe tu perfil y el sistema experto te recomendará la herramienta más adecuada.</p>', unsafe_allow_html=True)
st.divider()

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("🧪 Casos de prueba")
    st.caption("Carga un perfil de ejemplo para probar el sistema.")
    casos = {
        "— Seleccionar —": None,
        "Caso 1: Ilustrador con iPad":            {"tiene_ipad": True, "hace_ilustracion": True},
        "Caso 2: Diseñador UI/UX profesional":    {"tiene_pc_windows": True, "hace_uiux": True, "es_profesional": True, "requiere_colaboracion": True},
        "Caso 3: Principiante PC sin presupuesto":{"tiene_pc_windows": True, "es_principiante": True, "hace_ilustracion": True, "presupuesto_bajo": True, "tiempo_poco": True},
        "Caso 4: Artista manga en PC":            {"tiene_pc_windows": True, "hace_manga_comic": True, "tiene_tableta_grafica": True},
        "Caso 5: Game artist 3D profesional":     {"tiene_pc_potente": True, "hace_escultura_3d": True, "sector_videojuegos": True, "es_profesional": True},
        "Caso 6: Pixel artist indie":             {"tiene_pc_windows": True, "hace_pixel_art": True, "sector_videojuegos": True, "presupuesto_bajo": True},
        "Caso 7: Freelance ilustración":          {"objetivo_freelance": True, "hace_ilustracion": True, "es_profesional": True, "tiene_pc_windows": True},
        "Caso 8: Contenido para redes rápido":    {"sector_redes_sociales": True, "hace_ilustracion": True, "tiempo_poco": True, "requiere_portabilidad": True},
        "Caso 9: Estudiante 3D con tiempo":       {"hace_modelado_3d": True, "objetivo_educativo": True, "tiempo_moderado": True, "presupuesto_bajo": True},
        "Caso 10: Sin coincidencias (borde)":     {"tiene_tablet_android": True, "hace_animacion": True},
    }
    caso_sel = st.selectbox("Cargar caso:", list(casos.keys()))
    if casos[caso_sel]:
        st.caption("Hechos del caso:")
        for pred, val in casos[caso_sel].items():
            st.write(f"{'✅' if val else '❌'} {PREDICADOS.get(pred, pred)}")
    st.divider()
    st.caption("💡 Puedes cargar un caso y ajustarlo manualmente.")

caso_datos = casos.get(caso_sel) or {}

# ── Layout principal ──────────────────────────────────────────
col_entrada, col_resultados = st.columns([1, 1], gap="large")

with col_entrada:
    st.subheader("📝 Características del usuario")

    # 1. Dispositivo
    st.markdown('<p class="seccion-label">💻 1. Dispositivo disponible</p>', unsafe_allow_html=True)
    tiene_ipad            = st.checkbox("iPad (cualquier modelo)",               value=caso_datos.get("tiene_ipad", False))
    tiene_iphone          = st.checkbox("iPhone",                                value=caso_datos.get("tiene_iphone", False))
    tiene_tablet_android  = st.checkbox("Tablet Android con lápiz",              value=caso_datos.get("tiene_tablet_android", False))
    tiene_pc_windows      = st.checkbox("PC / laptop Windows",                   value=caso_datos.get("tiene_pc_windows", False))
    tiene_mac             = st.checkbox("Mac (MacBook o iMac)",                  value=caso_datos.get("tiene_mac", False))
    tiene_tableta_grafica = st.checkbox("Tableta gráfica (Wacom u otra)",        value=caso_datos.get("tiene_tableta_grafica", False))
    tiene_pc_potente      = st.checkbox("PC con buena GPU (para 3D/renderizado)", value=caso_datos.get("tiene_pc_potente", False))

    # 2. Experiencia
    st.markdown('<p class="seccion-label">🎓 2. Nivel de experiencia</p>', unsafe_allow_html=True)
    nivel = st.radio("Nivel:", ["Principiante", "Intermedio", "Profesional"],
        index=0 if caso_datos.get("es_principiante") else 2 if caso_datos.get("es_profesional") else 1,
        horizontal=True, label_visibility="collapsed")
    es_principiante = nivel == "Principiante"
    es_intermedio   = nivel == "Intermedio"
    es_profesional  = nivel == "Profesional"

    # 3. Tipo de arte 2D
    st.markdown('<p class="seccion-label">🖼️ 3. Tipo de arte — 2D</p>', unsafe_allow_html=True)
    hace_ilustracion  = st.checkbox("Ilustración digital (personajes, escenas)",  value=caso_datos.get("hace_ilustracion", False))
    hace_vectorial    = st.checkbox("Gráficos vectoriales (logos, íconos)",       value=caso_datos.get("hace_vectorial", False))
    hace_concept_art  = st.checkbox("Concept art / arte conceptual",              value=caso_datos.get("hace_concept_art", False))
    hace_manga_comic  = st.checkbox("Manga, cómic o novela gráfica",              value=caso_datos.get("hace_manga_comic", False))
    hace_uiux         = st.checkbox("Diseño de interfaces (UI/UX)",               value=caso_datos.get("hace_uiux", False))
    hace_animacion    = st.checkbox("Animación / GIFs frame-by-frame",            value=caso_datos.get("hace_animacion", False))
    hace_animacion_2d = st.checkbox("Animación 2D avanzada con rigging/bones",    value=caso_datos.get("hace_animacion_2d", False))
    hace_pixel_art    = st.checkbox("Pixel art (sprites, videojuegos retro)",     value=caso_datos.get("hace_pixel_art", False))

    # 4. Tipo de arte 3D
    st.markdown('<p class="seccion-label">🗿 4. Tipo de arte — 3D</p>', unsafe_allow_html=True)
    hace_modelado_3d      = st.checkbox("Modelado 3D (objetos, personajes)",      value=caso_datos.get("hace_modelado_3d", False))
    hace_escultura_3d     = st.checkbox("Escultura digital 3D (orgánica)",        value=caso_datos.get("hace_escultura_3d", False))
    hace_render_3d        = st.checkbox("Renderizado 3D fotorealista",            value=caso_datos.get("hace_render_3d", False))
    hace_arte_videojuegos = st.checkbox("Assets / arte para videojuegos",         value=caso_datos.get("hace_arte_videojuegos", False))

    # 5. Objetivo
    st.markdown('<p class="seccion-label">🎯 5. Objetivo del proyecto</p>', unsafe_allow_html=True)
    objetivo = st.radio("¿Para qué es tu proyecto?",
        ["Personal / hobby", "Profesional / laboral", "Educativo / estudio", "Freelance / clientes"],
        index=(
            0 if caso_datos.get("objetivo_personal") else
            1 if caso_datos.get("objetivo_profesional") else
            2 if caso_datos.get("objetivo_educativo") else
            3 if caso_datos.get("objetivo_freelance") else 0
        ),
        label_visibility="collapsed")
    objetivo_personal     = objetivo == "Personal / hobby"
    objetivo_profesional  = objetivo == "Profesional / laboral"
    objetivo_educativo    = objetivo == "Educativo / estudio"
    objetivo_freelance    = objetivo == "Freelance / clientes"

    # 6. Industria
    st.markdown('<p class="seccion-label">🏭 6. Industria o sector</p>', unsafe_allow_html=True)
    sector_videojuegos    = st.checkbox("Videojuegos",                            value=caso_datos.get("sector_videojuegos", False))
    sector_cine_tv        = st.checkbox("Cine / TV / animación",                  value=caso_datos.get("sector_cine_tv", False))
    sector_redes_sociales = st.checkbox("Redes sociales / contenido digital",     value=caso_datos.get("sector_redes_sociales", False))
    sector_impresion      = st.checkbox("Impresión (editorial, merchandising)",   value=caso_datos.get("sector_impresion", False))

    # 7. Tiempo
    st.markdown('<p class="seccion-label">⏱️ 7. Tiempo disponible para aprender</p>', unsafe_allow_html=True)
    tiempo = st.radio("¿Cuánto tiempo tienes para aprender la herramienta?",
        ["Poco (quiero algo intuitivo ya)", "Moderado (puedo dedicarle semanas)", "Mucho (dispuesto a aprender a fondo)"],
        index=(
            0 if caso_datos.get("tiempo_poco") else
            2 if caso_datos.get("tiempo_mucho") else 1
        ),
        label_visibility="collapsed")
    tiempo_poco     = tiempo == "Poco (quiero algo intuitivo ya)"
    tiempo_moderado = tiempo == "Moderado (puedo dedicarle semanas)"
    tiempo_mucho    = tiempo == "Mucho (dispuesto a aprender a fondo)"

    # 8. Restricciones
    st.markdown('<p class="seccion-label">⚙️ 8. Restricciones</p>', unsafe_allow_html=True)
    presupuesto_bajo      = st.checkbox("Prefiero gratuitas o pago único bajo",   value=caso_datos.get("presupuesto_bajo", False))
    requiere_colaboracion = st.checkbox("Necesito colaborar en tiempo real",      value=caso_datos.get("requiere_colaboracion", False))
    requiere_portabilidad = st.checkbox("Necesito trabajar desde el móvil",       value=caso_datos.get("requiere_portabilidad", False))

    # Validación
    dispositivo_ok = any([tiene_ipad, tiene_iphone, tiene_tablet_android,
                          tiene_pc_windows, tiene_mac, tiene_pc_potente])
    tipo_ok = any([hace_ilustracion, hace_vectorial, hace_concept_art,
                   hace_manga_comic, hace_uiux, hace_animacion, hace_animacion_2d,
                   hace_pixel_art, hace_modelado_3d, hace_escultura_3d,
                   hace_render_3d, hace_arte_videojuegos])

    if not dispositivo_ok:
        st.warning("⚠️ Selecciona al menos un dispositivo.")
    if not tipo_ok:
        st.warning("⚠️ Selecciona al menos un tipo de arte.")

    ejecutar = st.button("🔍 Obtener recomendación", type="primary",
                         use_container_width=True,
                         disabled=not (dispositivo_ok and tipo_ok))

# ── Resultados ────────────────────────────────────────────────
with col_resultados:
    st.subheader("🏆 Resultados")

    if ejecutar:
        hechos_iniciales = {
            "tiene_ipad": tiene_ipad, "tiene_iphone": tiene_iphone,
            "tiene_tablet_android": tiene_tablet_android, "tiene_pc_windows": tiene_pc_windows,
            "tiene_mac": tiene_mac, "tiene_tableta_grafica": tiene_tableta_grafica,
            "tiene_pc_potente": tiene_pc_potente,
            "es_principiante": es_principiante, "es_intermedio": es_intermedio, "es_profesional": es_profesional,
            "hace_ilustracion": hace_ilustracion, "hace_vectorial": hace_vectorial,
            "hace_concept_art": hace_concept_art, "hace_manga_comic": hace_manga_comic,
            "hace_uiux": hace_uiux, "hace_animacion": hace_animacion,
            "hace_animacion_2d": hace_animacion_2d, "hace_pixel_art": hace_pixel_art,
            "hace_modelado_3d": hace_modelado_3d, "hace_escultura_3d": hace_escultura_3d,
            "hace_render_3d": hace_render_3d, "hace_arte_videojuegos": hace_arte_videojuegos,
            "objetivo_personal": objetivo_personal, "objetivo_profesional": objetivo_profesional,
            "objetivo_educativo": objetivo_educativo, "objetivo_freelance": objetivo_freelance,
            "sector_videojuegos": sector_videojuegos, "sector_cine_tv": sector_cine_tv,
            "sector_redes_sociales": sector_redes_sociales, "sector_impresion": sector_impresion,
            "tiempo_poco": tiempo_poco, "tiempo_moderado": tiempo_moderado, "tiempo_mucho": tiempo_mucho,
            "presupuesto_bajo": presupuesto_bajo, "requiere_colaboracion": requiere_colaboracion,
            "requiere_portabilidad": requiere_portabilidad,
        }
        st.session_state["hechos_iniciales"] = hechos_iniciales
        with st.spinner("Analizando tu perfil..."):
            hechos_finales, reglas_aplicadas = encadenamiento_adelante(REGLAS, hechos_iniciales)
            recomendaciones = obtener_recomendaciones(hechos_finales, hechos_iniciales)
        st.session_state.update({
            "hechos_finales": hechos_finales,
            "reglas_aplicadas": reglas_aplicadas,
            "recomendaciones": recomendaciones,
        })

    if "recomendaciones" in st.session_state:
        recomendaciones  = st.session_state["recomendaciones"]
        reglas_aplicadas = st.session_state["reglas_aplicadas"]

        if recomendaciones:
            st.success(f"✅ Se encontraron {len(recomendaciones)} recomendación(es):")
            for pred in recomendaciones:
                nombre  = NOMBRES_HERRAMIENTAS.get(pred, pred)
                certeza = next((r["certeza"] for r in reglas_aplicadas if r["conclusion"][0] == pred), None)
                st.markdown(
                    f'<div class="recomendacion-card">{nombre} '
                    f'<span class="certeza-badge">FC: {certeza}</span></div>',
                    unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="sin-resultado">⚠️ No se pudo generar una recomendación. '
                'Intente agregar más detalles sobre su perfil.</div>',
                unsafe_allow_html=True)

        st.divider()
        st.subheader("🔍 Explicación del razonamiento")
        tab1, tab2, tab3 = st.tabs(["📋 Cadena completa", "❓ ¿Por qué?", "📊 Reglas aplicadas"])

        with tab1:
            st.text(explicar_razonamiento(reglas_aplicadas))

        with tab2:
            if recomendaciones:
                sel = st.selectbox("Selecciona una recomendación:",
                    recomendaciones, format_func=lambda x: NOMBRES_HERRAMIENTAS.get(x, x))
                if sel:
                    st.text(porque(sel, reglas_aplicadas))
            else:
                st.info("No hay recomendaciones que explicar.")

        with tab3:
            if reglas_aplicadas:
                st.write(f"**Total de reglas disparadas:** {len(reglas_aplicadas)}")
                for reg in reglas_aplicadas:
                    with st.expander(f"Regla {reg['regla']}: {reg['descripcion']}"):
                        st.write(f"**Certeza:** {reg['certeza']}")
                        st.write("**Condiciones:**")
                        for pred, val in reg["condiciones"]:
                            st.write(f"  {'✅' if val else '❌'} {PREDICADOS.get(pred, pred)}")
                        pred_c, val_c = reg["conclusion"]
                        st.write(f"**Conclusión:** {pred_c} = {val_c}")
                        st.write(f"**Justificación:** {reg['justificacion']}")
            else:
                st.info("No se aplicaron reglas.")

        st.divider()
        if st.button("🔄 Limpiar y empezar de nuevo", use_container_width=True):
            for key in ["hechos_iniciales","hechos_finales","reglas_aplicadas","recomendaciones"]:
                st.session_state.pop(key, None)
            st.rerun()
    else:
        st.info("👈 Completa el formulario y presiona **Obtener recomendación**.")
