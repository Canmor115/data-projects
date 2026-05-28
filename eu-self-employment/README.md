# 🇪🇺 Trabajo Autónomo en la Unión Europea (2010–2024)

Análisis exploratorio y visual del trabajo autónomo en la UE utilizando datos abiertos de **Eurostat**. El proyecto examina la evolución temporal, la distribución geográfica y las diferencias por género y nivel educativo, con el objetivo de responder a una pregunta central: **¿se emprende por necesidad o por oportunidad?**

---

## 📋 Descripción del problema

El trabajo autónomo en Europa lleva más de una década en descenso. Pero este dato agregado esconde diferencias notables entre países, géneros y niveles educativos. Este análisis busca entender qué hay detrás de esa tendencia y si el desempleo actúa como factor impulsor del emprendimiento, especialmente en mujeres con formación superior.

---

## 📂 Estructura del repositorio

```
eu-self-employment/
├── Trabajo_autonomo_UE_2010_2024.ipynb   # Notebook completo
└── README.md
```

> Los datos se descargan directamente desde la API de Eurostat al ejecutar el notebook — no se incluyen CSVs estáticos.

---

## 📊 Fuente de datos

**Eurostat — Empleo por situación en el mercado laboral**
- Dataset `lfst_r_lfe2estat` — Empleo y trabajo autónomo por región NUTS
- Dataset `lfsa_esgaed` — Autónomos por nivel educativo (ISCED) y sexo
- Dataset `une_educ_a` — Tasa de desempleo por nivel educativo y sexo

Cobertura: **UE-27 + países candidatos**, 2010–2024, población de 20–64 años.

---

## 🔧 Metodología

### 1. Evolución temporal del trabajo autónomo (UE-27)
- Proporción de autónomos totales y autónomos sin empleados sobre el total de ocupados
- Visualización de la tendencia 2010–2024

### 2. Distribución geográfica por regiones NUTS 2 (2024)
- Mapa interactivo con Folium del % de autónomos por región europea
- Escala de color por intensidad, con tooltip por región

### 3. Análisis por género
- Evolución de la tasa de emprendimiento para hombres y mujeres por separado
- Distribución del género dentro de la población autónoma (2010–2024)
- Mapas comparativos por países (2010 vs 2024) del % de mujeres autónomas

### 4. Nivel educativo y desempleo
- Evolución del emprendimiento por género y nivel ISCED (ED0-2, ED3-4, ED5-8)
- Evolución de la tasa de desempleo por género y nivel educativo
- **Correlación de Spearman** entre desempleo y emprendimiento

### 5. Ranking de países
- Top 10 países por tasa de desempleo femenino con formación superior (2010 vs 2024)
- Relación con la proporción de mujeres autónomas por país

---

## 📈 Hallazgos clave

- La proporción de autónomos en la UE-27 ha bajado del **15.9% en 2010 al 13.8% en 2024**.
- Los hombres representan ~70% de los autónomos, pero su tendencia es **descendente**. Las mujeres, minoritarias (~30%), muestran una tendencia **al alza**.
- Las mujeres con **formación superior** son las que más emprenden, al contrario que los hombres, donde son las menos cualificadas las que más emprenden.
- Existe una **correlación positiva fuerte (Spearman ~0.99)** entre la tasa de desempleo femenino con educación superior y el % de mujeres autónomas — apuntando a un patrón de **emprendimiento por necesidad**.
- El norte y oeste de Europa (Noruega, Francia, Irlanda) lideran el aumento del emprendimiento femenino. El este de Europa apenas ha cambiado en 14 años.

---

## 🛠️ Tecnologías y librerías

**Lenguaje:** Python  
**Entorno:** Jupyter Notebook

| Librería | Uso |
|----------|-----|
| `pandas` | Carga, limpieza y transformación de datos |
| `matplotlib` | Visualizaciones estáticas |
| `seaborn` | Heatmap de correlaciones |
| `folium` | Mapas interactivos coropletas |
| `branca` | Escalas de color para mapas |
| `requests` | Descarga del GeoJSON NUTS desde GISCO |

---

## 🚀 Reproducibilidad

```python
# Clonar el repositorio
# Abrir Trabajo_autonomo_UE_2010_2024.ipynb en Jupyter o VS Code
# Ejecutar todas las celdas en orden
# Los datos se descargan automáticamente desde la API de Eurostat
```

> **Nota**: el notebook usa `!wget` para descargar los CSV — compatible con Linux/Mac. En Windows puede requerir sustituir por `urllib.request` o ejecutar desde WSL.

---

## 👩‍💻 Autora

**Camila Moreno Ortiz**   

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Camila%20Moreno-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/camila-andrea-moreno-ortiz/)
