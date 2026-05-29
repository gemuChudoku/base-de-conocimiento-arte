# Casos de Prueba — Sistema Experto Recomendador de Herramienta de Dibujo Digital

## Tabla de validación

| Caso | Descripción | Hechos iniciales clave | Reglas esperadas | Conclusión esperada | Resultado obtenido | Estado |
|------|-------------|------------------------|------------------|---------------------|--------------------|--------|
| 1 | Ilustrador con iPad | tiene_ipad=True, hace_ilustracion=True | R1 | recomendar_procreate | recomendar_procreate | ✓ |
| 2 | Diseñador UI/UX profesional con colaboración | tiene_pc_windows=True, hace_uiux=True, es_profesional=True, requiere_colaboracion=True | R11, R12 | recomendar_figma | recomendar_figma | ✓ |
| 3 | Principiante en PC sin presupuesto | tiene_pc_windows=True, es_principiante=True, hace_ilustracion=True, presupuesto_bajo=True | R4, R14 | recomendar_krita | recomendar_krita | ✓ |
| 4 | Artista de manga en PC con tableta gráfica | tiene_pc_windows=True, hace_manga_comic=True, tiene_tableta_grafica=True | R6 | recomendar_clip_studio | recomendar_clip_studio | ✓ |
| 5 | Caso borde: tablet Android + profesional + vectorial | tiene_tablet_android=True, es_profesional=True, hace_vectorial=True | ninguna | sin recomendación | sin recomendación | ✓ |

---

## Detalle de cada caso

### Caso 1 — Ilustrador con iPad
**Descripción:** Usuario que tiene un iPad y quiere hacer ilustración digital.
**Hechos iniciales:**
- tiene_ipad = True
- hace_ilustracion = True

**Reglas que deben activarse:**
- R1: tiene_ipad ∧ hace_ilustracion → recomendar_procreate (FC=0.95)

**Conclusión esperada:** Procreate
**Justificación:** Procreate es la herramienta de referencia para ilustración en iPad.

---

### Caso 2 — Diseñador UI/UX profesional
**Descripción:** Diseñador profesional que trabaja en PC, hace UI/UX y necesita colaborar en tiempo real.
**Hechos iniciales:**
- tiene_pc_windows = True
- hace_uiux = True
- es_profesional = True
- requiere_colaboracion = True

**Reglas que deben activarse:**
- R11: hace_uiux → recomendar_figma (FC=0.97)
- R12: requiere_colaboracion ∧ hace_uiux → recomendar_figma (FC=0.97)

**Conclusión esperada:** Figma
**Justificación:** Figma es el estándar absoluto para UI/UX con colaboración en tiempo real.

---

### Caso 3 — Principiante en PC sin presupuesto
**Descripción:** Usuario que está comenzando, trabaja en PC y quiere hacer ilustración sin gastar.
**Hechos iniciales:**
- tiene_pc_windows = True
- es_principiante = True
- hace_ilustracion = True
- presupuesto_bajo = True

**Reglas que deben activarse:**
- R4: tiene_pc_windows ∧ presupuesto_bajo ∧ hace_ilustracion → recomendar_krita (FC=0.93)
- R14: es_principiante ∧ tiene_pc_windows ∧ hace_ilustracion → recomendar_krita (FC=0.91)

**Conclusión esperada:** Krita
**Justificación:** Krita es la opción gratuita más completa para principiantes en PC.

---

### Caso 4 — Artista de manga en PC con tableta gráfica
**Descripción:** Artista que quiere hacer manga usando PC con tableta gráfica.
**Hechos iniciales:**
- tiene_pc_windows = True
- hace_manga_comic = True
- tiene_tableta_grafica = True

**Reglas que deben activarse:**
- R6: tiene_pc_windows ∧ hace_manga_comic → recomendar_clip_studio (FC=0.94)

**Conclusión esperada:** Clip Studio Paint
**Justificación:** Clip Studio Paint es el estándar para manga y cómic en PC.

---

### Caso 5 — Caso borde sin recomendación
**Descripción:** Usuario con tablet Android que quiere hacer animación pero sin ser principiante ni tener PC. Ninguna regla cubre esta combinación exacta.
**Hechos iniciales:**
- tiene_tablet_android = True
- es_profesional = False
- es_principiante = False
- hace_animacion = True

**Reglas que deben activarse:** ninguna
**Conclusión esperada:** Sin recomendación
**Justificación:** El sistema no tiene reglas para animación en tablet Android con perfil intermedio. El motor maneja este caso sin errores y muestra el mensaje de sin resultado apropiado.
