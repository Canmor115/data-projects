# 🚗 Segmentación de riesgo y predicción de siniestralidad en seguros de vehículos

Análisis completo sobre una cartera real (anonimizada) de seguros de vehículos de motor en España, combinando clustering no supervisado (K-means, K-medians, PAM, DBSCAN) con un árbol de decisión y un random forest para predecir siniestros. 

La intención es responder a dos preguntas muy sencillas: 
- ¿Hay clientes que se comportan muy distinto aunque parezcan iguales?
- ¿Se puede ver venir qué tipo de cliente va a tener un siniestro?

---

## 📋 Descripción del problema

Los datos abiertos al público de compañías aseguradoras son poco comunes, ya que la información sobre siniestralidad constituye el núcleo del negocio. El dataset utilizado en este proyecto proviene del estudio de Segura-Gisbert et al. (2024), publicado en el *European Actuarial Journal*, con datos reales de una cartera de vehículos entre 2015 y 2018.

Su estructura permite combinar dos enfoques en un mismo problema: segmentación no supervisada a partir de las características del vehículo, y predicción supervisada de siniestros a partir del historial de cada póliza.

---

## 📂 Estructura del repositorio

```         
insurance-risk-segmentation/
├── 01_data_preparation.Rmd   
├── 01_data_preparation.html
├── 02_clustering_classification.Rmd
├── 02_clustering_classification.html   
├── data/
│   ├── README.md
│   └── prepared_model.RData              
├── .gitignore
└── README.md
```

Son dos notebooks que van en orden: el primero (`01_data_preparation.Rmd`) limpia y prepara los datos; el segundo (`02_clustering_classification.Rmd`) carga ese resultado y hace el clustering y la clasificación. Se dejan también los HTML ya renderizados por si alguien quiere leer sin ejecutar nada.

---

## 📊 Dataset

**Motor vehicle insurance data**
Fuente: [Mendeley Data — Segura-Gisbert, Lledó & Pavía (2024)](https://data.mendeley.com/datasets/5cxyb5fp4f/2) · CC BY 4.0

- **105.555 pólizas originales**, muestra de trabajo de 10.000 (semilla fija para reproducibilidad)
- **Variables de vehículo, cliente e historial** — potencia, cilindrada, peso, valor, antigüedad, ratio de siniestros históricos
- **Variable objetivo** — `Claim`: si hubo o no siniestro en el periodo
- **Desbalance de clases** — 81.5% sin siniestro / 18.5% con siniestro

---

## 🔧 Metodología

### 1. Limpieza y preparación

No todos los datos anómalos se trataron de la misma manera. 153 pólizas con potencia de 0 CV se cruzaron con cilindrada y valor del vehículo antes de modificarlas, confirmando que eran motos y tractores con datos mal registrados; la solución fue imputar por la mediana de su categoría. Por otro lado, aquellos registros imposibles como por ejemplo un turismo con 310 CV, 599 cc y 680 kg, se eliminaron directamente.

### 2. Reducción de dimensionalidad

Aquellas variables numéricas correlacionadas fueron reducidas a 6 componentes que capturaron el 80% de la información mediante PCA. Adicionalmente se comparó con SVD para comprobar la calidad de los resultados, ya que el objetivo también era entender las matemáticas detrás de cada técnica. 

### 3. Modelos

| Modelo                               | Descripción                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------ |
| **K-means / K-medians / PAM**        | Clustering sobre los 6 componentes del PCA                                           |
| **DBSCAN**                           | Clustering basado en densidad, para detectar outliers que no encajan en ningún grupo |
| **Árbol de decisión (CART, podado)** | Predicción de siniestro, priorizando recall sobre accuracy                           |
| **Random Forest**                    | Ensemble de árboles, como contraste del modelo simple                                |

Con 81.5% de pólizas sin siniestro, un modelo vago podría acertar el 81% del tiempo prediciendo siempre "no habrá siniestro", algo totalmente inútil en la práctica. Por eso el criterio de evaluación prioriza el recall (detectar siniestros reales) sobre el accuracy bruto.

---

## 📈 Resultados

| Modelo              | Recall    | Variables usadas                     | Notas                                                              |
| ------------------- | --------- | ------------------------------------ | ------------------------------------------------------------------ |
| Árbol podado (CART) | **0.928** | 2 (`R_Claims_history`, `Policy_age`) | Simple, interpretable, el modelo más recomendado                   |
| Random Forest       | 0.477     | Todas                                | Mejor accuracy, pero los pesos de clase se diluyen en el bootstrap |

---

## 🔍 Hallazgos

Salieron tres clusters sin forzar ningún resultado: motos con siniestralidad baja (7.8%), un grupo estándar que es la mayoría de la cartera (19.2%), y clientes "veteranos" con más historial y más siniestralidad (20.7%).

DBSCAN marcó 287 pólizas como "ruido", casos que no encajan en ningún grupo, que además agrupan la siniestralidad más alta de toda la cartera, 32.4% y un ratio histórico de 0.85, muy por encima de los demás clusters.

El árbol de decisión, entrenado por separado, eligió por su cuenta las mismas dos variables que definen al grupo de más riesgo: antiguedad de la póliza y el ratio de siniestros por año.  

Lo que queda menos resuelto es el random forest: los pesos usados para compensar el desbalance se diluyen porque cada árbol del ensemble solo ve una muestra aleatoria, mientras que en un árbol único ese peso afecta directamente cada decisión. Se recomienda revisar con SMOTE o ajustar el umbral.

---

## 🛠️ Tecnologías y librerías

**Lenguaje:** R · **Entorno:** R Markdown

| Librería                                       | Uso                                  |
| ---------------------------------------------- | ------------------------------------ |
| `factoextra`, `cluster`, `dbscan`, `flexclust` | Clustering y evaluación (silhouette) |
| `rpart`, `rpart.plot`                          | Árbol de decisión                    |
| `randomForest`                                 | Random Forest                        |
| `caret`, `gmodels`                             | Evaluación y validación              |
| `ggplot2`, `patchwork`, `ggcorrplot`, `GGally` | Visualizaciones                      |
| `dplyr`, `lubridate`                           | Preparación de datos                 |

---

## 🚀 Reproducibilidad

```r
# Clonar el repositorio
# Abrir notebooks/01_preparacion_datos.Rmd en RStudio y hacer knit
# (genera el dataset preparado que carga el segundo notebook)
# Abrir notebooks/02_modelado_clustering_clasificacion.Rmd y hacer knit
```

> El dataset no se incluye completo en el repo (ver `data/README.md` para la fuente). Semilla aleatoria fija en el muestreo y en todos los modelos para reproducibilidad.

---

## 👩‍💻 Autora

**Camila Moreno Ortiz**
[LinkedIn](https://www.linkedin.com/in/camila-andrea-moreno-ortiz) · [GitHub](https://github.com/Canmor115)

---

## 📄 Licencia

Dataset bajo licencia CC BY 4.0 (Mendeley Data). El código de análisis es de libre uso con atribución.