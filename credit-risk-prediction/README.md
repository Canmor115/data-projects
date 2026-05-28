# 🏦 Credit Risk Prediction with Decision Trees

Análisis completo de predicción de riesgo crediticio aplicando árboles de decisión, Random Forest y XGBoost sobre el dataset **German Credit**. El proyecto incluye exploración de datos, modelado, evaluación con matriz de costes asimétrica y explicabilidad con técnicas SHAP, ALE y Feature Importance.

------------------------------------------------------------------------

## 📋 Descripción del problema

Un banco alemán necesita predecir qué solicitantes de crédito tienen mayor probabilidad de **no devolver el préstamo** (default). El desafío clave es que el coste de los errores es asimétrico: **clasificar un cliente moroso como solvente cuesta 5 veces más** que el error inverso.

Esto convierte el problema en un ejercicio de optimización bajo restricciones de negocio, donde el Recall de la clase Default es la métrica prioritaria, no el accuracy global.

------------------------------------------------------------------------

## 📂 Estructura del repositorio

```         
credit-risk-prediction/
├── credit_risk_analysis.Rmd   # Análisis completo en R Markdown
├── credit_risk_analysis.html   # Versión renderizada (GitHub Pages)
├── data/
│   └── credit.csv             # Dataset German Credit
└── README.md
```

------------------------------------------------------------------------

## 📊 Dataset

**German Credit Dataset**\
Fuente: [Kaggle — shravan3273/credit-approval](https://www.kaggle.com/shravan3273/credit-approval)

-   **1.000 observaciones** — solicitudes de crédito de un banco alemán
-   **20 variables** — perfil financiero y sociodemográfico del cliente
-   **Variable objetivo** — `default`: 1 = buen pagador / 2 = impago
-   **Desbalance de clases** — 70% No default / 30% Default

------------------------------------------------------------------------

## 🔧 Metodología

### 1. Análisis exploratorio (EDA)

-   Diccionario de variables y tipos de datos
-   Distribución de la variable objetivo
-   Análisis de correlaciones y relaciones con el target
-   Detección y tratamiento de variables pseudonuméricas

### 2. Modelos de clasificación

| Modelo               | Descripción                                     |
|----------------------|-------------------------------------------------|
| **C5.0 básico**      | Árbol de decisión base con todas las variables  |
| **C5.0 con pruning** | Árbol podado (CF=0.10) para reducir sobreajuste |
| **Random Forest**    | Ensemble de 500 árboles con bagging             |
| **XGBoost**          | Gradient boosting con regularización            |

### 3. Evaluación

-   Matriz de confusión y métricas por clase (Precision, Recall, F1)
-   Curva ROC y AUC
-   **Matriz de costes asimétrica** (FN=5, FP=1) como criterio de selección

### 4. Explicabilidad

-   Feature Importance global (permutación)
-   Partial Dependence Plots (PDP) vs Accumulated Local Effects (ALE)
-   Valores SHAP para explicación individual de predicciones

------------------------------------------------------------------------

## 📈 Resultados

| Modelo                 | Accuracy | Recall (Default) | AUC       | Coste   |
|------------------------|----------|------------------|-----------|---------|
| C5.0 básico            | 69.8%    | 47.1%            | 0.689     | 320     |
| C5.0 pruning (CF=0.10) | 70.4%    | 47.1%            | 0.720     | **315** |
| Random Forest          | 73.7%    | 38.2%            | **0.770** | 370     |
| XGBoost                | 72.2%    | 45.1%            | 0.759     | 335     |

**Modelo recomendado según criterio:**

-   💰 **Menor coste económico** → C5.0 con pruning (315 unidades)
-   📊 **Mayor capacidad discriminante** → Random Forest (AUC = 0.770)
-   ⚖️ **Mejor equilibrio de métricas** → XGBoost (F1 = 49.7%)

------------------------------------------------------------------------

## 🔍 Hallazgos clave

-   **`checking_balance`** es la variable más predictiva, tanto a nivel global como en explicaciones individuales SHAP.
-   **Perfil de alto riesgo identificado**: cliente con saldo negativo en cuenta corriente que solicita un préstamo de más de 30 meses para educación o coche nuevo.
-   **Hallazgo contraintuitivo**: clientes con historial `fully repaid` presentan tasas de default elevadas — el banco les concede créditos nuevos sin historial activo reciente.
-   Variables como `dependents`, `telephone` o `residence_history` son prácticamente irrelevantes para predecir el impago.

------------------------------------------------------------------------

## 🛠️ Tecnologías y librerías

**Lenguaje:** R\
**Entorno:** R Markdown

| Librería                | Uso                                            |
|-------------------------|------------------------------------------------|
| `C50`                   | Árbol de decisión C5.0                         |
| `randomForest`          | Random Forest                                  |
| `xgboost`               | Gradient Boosting                              |
| `caret`                 | Evaluación y validación de modelos             |
| `iml`                   | Explicabilidad (Feature Importance, ALE, SHAP) |
| `ROCR`                  | Curvas ROC                                     |
| `ggplot2` + `patchwork` | Visualizaciones                                |

------------------------------------------------------------------------

## 🚀 Reproducibilidad

``` r
# Clonar el repositorio
# Abrir credit_risk_analysis.Rmd en RStudio
# Las librerías se instalan automáticamente al ejecutar el primer chunk
# Hacer knit a HTML

# El dataset debe estar en data/credit.csv (incluido en el repo)
```

> **Nota**: Se fijó semilla aleatoria en todos los modelos y en el cálculo de Feature Importance por permutación para garantizar resultados idénticos en cada compilación.

------------------------------------------------------------------------

## 👩‍💻 Autora

**Camila Moreno Ortiz**\
[LinkedIn](https://www.linkedin.com/in/camila-andrea-moreno-ortiz) · [GitHub](https://github.com/Canmor115)

------------------------------------------------------------------------

## 📄 Licencia

Dataset original bajo licencia de Kaggle. El código de análisis es de libre uso con atribución.
