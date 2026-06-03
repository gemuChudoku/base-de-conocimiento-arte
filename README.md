#  Sistema Experto: Recomendador de Herramienta de Dibujo Digital

Sistema basado en conocimiento que recomienda herramientas de dibujo digital
según el perfil del usuario, implementado con Python y Streamlit.

**Autores:** [Apellido1] [Apellido2]  
**Asignatura:** Inteligencia Artificial II  
**Institución:** Fundación Universitaria Los Libertadores

---

##  Estructura del proyecto

```
proyecto-final-sbc/
├── README.md
├── requirements.txt
├── src/
│   ├── base_conocimiento.py   # Predicados y 15 reglas de producción
│   ├── motor_inferencia.py    # Motor de inferencia (encadenamiento adelante)
│   └── app.py                 # Interfaz web con Streamlit
├── docs/
│   ├── documentacion_tecnica.pdf
│   └── manual_usuario.pdf
└── tests/
    └── casos_prueba.md        # 5 casos de prueba documentados
```

---

##  Instalación

**Requisitos:** Python 3.8 o superior

```bash
# 1. Clonar o descomprimir el proyecto
cd proyecto-final-sbc

# 2. Instalar dependencias
pip install -r requirements.txt
```

---

## Ejecución

```bash
cd src
streamlit run app.py
```

La aplicación abrirá automáticamente en el navegador en `http://localhost:8501`

---

## Descripción del sistema

El sistema contiene:
- **15 reglas de producción** organizadas en 6 grupos temáticos
- **16 predicados** de entrada (características del usuario)
- **9 herramientas** posibles como conclusión
- **Motor de encadenamiento hacia adelante** con detección de punto fijo
- **Sistema de explicación** con cadena de razonamiento y función `¿Por qué?`

### Herramientas que puede recomendar:
| Herramienta | Perfil ideal |
|---|---|
| Procreate | iPad, ilustración y concept art |
| Clip Studio Paint | Manga y cómic (PC o iPad) |
| Krita | PC, gratuito, principiantes |
| Adobe Photoshop | PC profesional con tableta gráfica |
| Adobe Illustrator | Vectorial profesional |
| Inkscape | Vectorial gratuito |
| Affinity Designer | Vectorial sin suscripción |
| Figma | UI/UX y colaboración |
| Autodesk Sketchbook | Principiantes en Android |
| Herramienta  | Uso recomendado                                      |
| Ibis Paint X | Android/iOS, ilustración digital y dibujo móvil      |
| Blender      | Modelado, animación y renderizado 3D gratuito        |
| Cinema 4D    | Animación y motion graphics profesionales            |
| ZBrush       | Escultura digital y modelado de personajes 3D        |
| Aseprite     | Pixel art y animación de videojuegos retro           |
| Spine        | Animación 2D para videojuegos mediante esqueletos    |
| FlipaClip    | Animación 2D cuadro por cuadro en móviles y tabletas |
| Align Motion | Motion graphics y animación para contenido digital   |

