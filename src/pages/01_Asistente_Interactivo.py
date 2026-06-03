import streamlit as st
from base_conocimiento import REGLAS, NOMBRES_HERRAMIENTAS
from motor_inferencia import encadenamiento_adelante, obtener_recomendaciones, porque

st.set_page_config(page_title="Asistente Interactivo", page_icon="🎨", layout="centered")

st.title("🎨 Asistente Interactivo")
st.caption("Responde por pasos y obtén una recomendación personalizada.")

PASOS = [
    "Dispositivos",
    "Experiencia",
    "Arte 2D",
    "Arte 3D",
    "Objetivo",
    "Industria",
    "Tiempo",
    "Restricciones"
]

if "paso_actual" not in st.session_state:
    st.session_state.paso_actual = 0

paso = st.session_state.paso_actual

st.progress((paso + 1) / len(PASOS))
st.write(f"### Paso {paso + 1} de {len(PASOS)} — {PASOS[paso]}")

# ---------- PASO 1 ----------
if paso == 0:
    st.session_state["tiene_ipad"] = st.checkbox("iPad", value=st.session_state.get("tiene_ipad", False))
    st.session_state["tiene_iphone"] = st.checkbox("iPhone", value=st.session_state.get("tiene_iphone", False))
    st.session_state["tiene_tablet_android"] = st.checkbox("Tablet Android", value=st.session_state.get("tiene_tablet_android", False))
    st.session_state["tiene_pc_windows"] = st.checkbox("PC Windows", value=st.session_state.get("tiene_pc_windows", False))
    st.session_state["tiene_mac"] = st.checkbox("Mac", value=st.session_state.get("tiene_mac", False))
    st.session_state["tiene_tableta_grafica"] = st.checkbox("Tableta gráfica", value=st.session_state.get("tiene_tableta_grafica", False))
    st.session_state["tiene_pc_potente"] = st.checkbox("PC potente", value=st.session_state.get("tiene_pc_potente", False))

# ---------- PASO 2 ----------
elif paso == 1:
    nivel = st.radio(
        "Nivel de experiencia",
        ["Principiante", "Intermedio", "Profesional"],
        index=0 if st.session_state.get("es_principiante") else 2 if st.session_state.get("es_profesional") else 1
    )

    st.session_state["es_principiante"] = nivel == "Principiante"
    st.session_state["es_intermedio"] = nivel == "Intermedio"
    st.session_state["es_profesional"] = nivel == "Profesional"

# ---------- PASO 3 ----------
elif paso == 2:
    for item in [
        "hace_ilustracion",
        "hace_vectorial",
        "hace_concept_art",
        "hace_manga_comic",
        "hace_uiux",
        "hace_animacion",
        "hace_animacion_2d",
        "hace_pixel_art"
    ]:
        st.session_state[item] = st.checkbox(item.replace("_", " ").title(),
                                             value=st.session_state.get(item, False))

# ---------- PASO 4 ----------
elif paso == 3:
    for item in [
        "hace_modelado_3d",
        "hace_escultura_3d",
        "hace_render_3d",
        "hace_arte_videojuegos"
    ]:
        st.session_state[item] = st.checkbox(item.replace("_", " ").title(),
                                             value=st.session_state.get(item, False))

# ---------- PASO 5 ----------
elif paso == 4:
    objetivo = st.radio(
        "Objetivo",
        ["Personal", "Profesional", "Educativo", "Freelance"]
    )

    st.session_state["objetivo_personal"] = objetivo == "Personal"
    st.session_state["objetivo_profesional"] = objetivo == "Profesional"
    st.session_state["objetivo_educativo"] = objetivo == "Educativo"
    st.session_state["objetivo_freelance"] = objetivo == "Freelance"

# ---------- PASO 6 ----------
elif paso == 5:
    for item in [
        "sector_videojuegos",
        "sector_cine_tv",
        "sector_redes_sociales",
        "sector_impresion"
    ]:
        st.session_state[item] = st.checkbox(item.replace("_", " ").title(),
                                             value=st.session_state.get(item, False))

# ---------- PASO 7 ----------
elif paso == 6:
    tiempo = st.radio(
        "Tiempo disponible",
        ["Poco", "Moderado", "Mucho"]
    )

    st.session_state["tiempo_poco"] = tiempo == "Poco"
    st.session_state["tiempo_moderado"] = tiempo == "Moderado"
    st.session_state["tiempo_mucho"] = tiempo == "Mucho"

# ---------- PASO 8 ----------
elif paso == 7:
    st.session_state["presupuesto_bajo"] = st.checkbox(
        "Presupuesto bajo",
        value=st.session_state.get("presupuesto_bajo", False)
    )

    st.session_state["requiere_colaboracion"] = st.checkbox(
        "Necesita colaboración",
        value=st.session_state.get("requiere_colaboracion", False)
    )

    st.session_state["requiere_portabilidad"] = st.checkbox(
        "Necesita portabilidad",
        value=st.session_state.get("requiere_portabilidad", False)
    )

col1, col2 = st.columns(2)

with col1:
    if paso > 0:
        if st.button("⬅️ Anterior"):
            st.session_state.paso_actual -= 1
            st.rerun()

with col2:
    if paso < len(PASOS) - 1:
        if st.button("➡️ Siguiente"):
            st.session_state.paso_actual += 1
            st.rerun()

if paso == len(PASOS) - 1:

    st.divider()

    if st.button("🎯 Obtener recomendación", type="primary", use_container_width=True):

        hechos = {}

        for k, v in st.session_state.items():
            if isinstance(v, bool):
                hechos[k] = v

        hechos_finales, reglas_aplicadas = encadenamiento_adelante(
            REGLAS,
            hechos
        )

        recomendaciones = obtener_recomendaciones(
            hechos_finales,
            hechos
        )

        st.session_state["resultado"] = recomendaciones
        st.session_state["reglas"] = reglas_aplicadas

if "resultado" in st.session_state:

    st.divider()
    st.subheader("🏆 Recomendaciones")

    recomendaciones = st.session_state["resultado"]
    reglas_aplicadas = st.session_state["reglas"]

    if recomendaciones:

        ranking = []

        for rec in recomendaciones:

            fc = 0

            for regla in reglas_aplicadas:
                if regla["conclusion"][0] == rec:
                    fc = max(fc, regla["certeza"])

            ranking.append((rec, fc))

        ranking.sort(key=lambda x: x[1], reverse=True)

        medallas = ["🥇", "🥈", "🥉"]

        for i, (pred, fc) in enumerate(ranking):

            nombre = NOMBRES_HERRAMIENTAS.get(pred, pred)

            icono = medallas[i] if i < 3 else "🏅"

            st.success(
                f"{icono} {nombre} — FC: {fc:.2f}"
            )

        with st.expander("🔍 Ver explicación detallada"):
            for rec, _ in ranking:
                st.text(porque(rec, reglas_aplicadas))

    else:
        st.warning("No se encontraron recomendaciones.")

    if st.button("🔄 Reiniciar asistente"):
        st.session_state.clear()
        st.rerun()
