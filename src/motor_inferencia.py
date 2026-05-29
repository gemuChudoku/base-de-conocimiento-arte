# =============================================================
# MOTOR DE INFERENCIA
# Sistema Experto: Recomendador de Herramienta de Dibujo Digital
# =============================================================
# Implementa encadenamiento hacia adelante (forward chaining).
# Aplica las reglas de la base de conocimiento iterativamente
# hasta alcanzar el punto fijo (no hay nuevos hechos que derivar).
# =============================================================


def encadenamiento_adelante(base_conocimiento, hechos_iniciales):
    """
    Motor de inferencia con encadenamiento hacia adelante.

    Algoritmo:
        1. Inicializar la memoria de trabajo con los hechos iniciales.
        2. Recorrer todas las reglas en cada iteración.
        3. Si TODAS las condiciones de una regla se cumplen y su
           conclusión aún no está en memoria → dispararla.
        4. Repetir hasta que ninguna regla nueva se dispare (punto fijo).

    Parámetros:
        base_conocimiento (list): Lista de reglas del dominio.
        hechos_iniciales  (dict): Diccionario {predicado: bool} con los
                                  hechos conocidos al inicio.

    Retorna:
        tuple:
            - hechos_finales   (dict):  Todos los hechos tras la inferencia.
            - reglas_aplicadas (list):  Lista de reglas que se dispararon,
                                        en orden de aplicación.
    """
    # Copia para no modificar el diccionario original
    hechos = dict(hechos_iniciales)
    reglas_aplicadas = []
    iteracion = 0
    max_iteraciones = 100  # Límite para detectar ciclos infinitos

    while iteracion < max_iteraciones:
        iteracion += 1
        nuevos_hechos = False

        for regla in base_conocimiento:
            # Saltar si la conclusión ya fue derivada
            conclusion_pred, conclusion_val = regla["conclusion"]
            if hechos.get(conclusion_pred) == conclusion_val:
                continue

            # Verificar si TODAS las condiciones se satisfacen
            if _todas_condiciones_satisfechas(regla["condiciones"], hechos):
                # Disparar la regla: agregar la conclusión a la memoria
                hechos[conclusion_pred] = conclusion_val
                nuevos_hechos = True
                reglas_aplicadas.append({
                    "iteracion":    iteracion,
                    "regla":        regla["nombre"],
                    "descripcion":  regla["descripcion"],
                    "condiciones":  regla["condiciones"],
                    "conclusion":   regla["conclusion"],
                    "certeza":      regla["certeza"],
                    "justificacion": regla["justificacion"],
                })

        # Punto fijo: no se derivó ningún hecho nuevo → terminar
        if not nuevos_hechos:
            break

    return hechos, reglas_aplicadas


def _todas_condiciones_satisfechas(condiciones, hechos):
    """
    Verifica si TODAS las condiciones de una regla se satisfacen.

    Cada condición es una tupla (predicado, valor_esperado):
        - ("tiene_ipad", True)  → el hecho debe estar presente y ser True
        - ("presupuesto_bajo", False) → el hecho debe ser False o estar ausente

    Parámetros:
        condiciones (list): Lista de tuplas (predicado, valor_esperado).
        hechos      (dict): Memoria de trabajo actual.

    Retorna:
        bool: True si todas las condiciones se cumplen.
    """
    for predicado, valor_esperado in condiciones:
        valor_actual = hechos.get(predicado, False)
        if valor_actual != valor_esperado:
            return False
    return True


def explicar_razonamiento(reglas_aplicadas):
    """
    Genera una explicación legible de la cadena de inferencia completa.
    Muestra qué reglas se dispararon, en qué orden y por qué.

    Parámetros:
        reglas_aplicadas (list): Lista generada por encadenamiento_adelante().

    Retorna:
        str: Texto explicativo con toda la cadena de razonamiento.
    """
    if not reglas_aplicadas:
        return (
            "⚠️ No se aplicó ninguna regla con los datos proporcionados.\n"
            "Verifique que las características seleccionadas sean suficientes "
            "para activar al menos una regla del sistema."
        )

    lineas = ["📋 CADENA DE RAZONAMIENTO APLICADA\n", "=" * 50]

    for i, reg in enumerate(reglas_aplicadas, start=1):
        pred_concl, val_concl = reg["conclusion"]
        lineas.append(f"\nPaso {i} — Regla {reg['regla']}: {reg['descripcion']}")
        lineas.append(f"  Iteración: {reg['iteracion']}")
        lineas.append("  Condiciones verificadas:")
        for pred, val in reg["condiciones"]:
            simbolo = "✔" if val else "✘ NO"
            lineas.append(f"    {simbolo} {pred}")
        lineas.append(f"  Conclusión derivada: {pred_concl} = {val_concl}")
        lineas.append(f"  Factor de certeza  : {reg['certeza']}")
        lineas.append(f"  Justificación      : {reg['justificacion']}")
        lineas.append("-" * 50)

    return "\n".join(lineas)


def porque(conclusion_buscada, reglas_aplicadas):
    """
    Explica por qué el sistema llegó a una conclusión específica.
    Busca en el historial la regla que originó esa conclusión.

    Parámetros:
        conclusion_buscada (str):  Nombre del predicado de conclusión.
        reglas_aplicadas   (list): Historial generado por encadenamiento_adelante().

    Retorna:
        str: Explicación detallada de la conclusión, o mensaje de no encontrado.
    """
    for reg in reglas_aplicadas:
        pred_concl, _ = reg["conclusion"]
        if pred_concl == conclusion_buscada:
            lineas = [
                f"🔍 ¿Por qué se recomendó: {conclusion_buscada}?\n",
                f"Fue derivada por la regla {reg['regla']}: {reg['descripcion']}",
                "\nPorque se cumplieron estas condiciones:",
            ]
            for pred, val in reg["condiciones"]:
                if val:
                    lineas.append(f"  • El usuario SÍ tiene/hace: {pred}")
                else:
                    lineas.append(f"  • El usuario NO tiene/hace: {pred}")
            lineas.append(f"\nJustificación experta:\n  {reg['justificacion']}")
            lineas.append(f"\nFactor de certeza: {reg['certeza']}")
            return "\n".join(lineas)

    return (
        f"⚠️ La conclusión '{conclusion_buscada}' no fue derivada en esta sesión.\n"
        "Verifique que los hechos iniciales activen la regla correspondiente."
    )


def obtener_recomendaciones(hechos_finales, hechos_iniciales):
    """
    Filtra los hechos finales y retorna únicamente las recomendaciones
    derivadas por el motor (excluye los hechos ingresados por el usuario).

    Parámetros:
        hechos_finales   (dict): Todos los hechos tras la inferencia.
        hechos_iniciales (dict): Hechos con los que comenzó el sistema.

    Retorna:
        list: Lista de predicados de conclusión derivados (que empiezan con
              "recomendar_").
    """
    recomendaciones = []
    for pred, val in hechos_finales.items():
        if pred.startswith("recomendar_") and val is True:
            if pred not in hechos_iniciales:
                recomendaciones.append(pred)
    return sorted(recomendaciones)
