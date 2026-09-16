# Datos

## Fuente

**Motor vehicle insurance data**
Segura-Gisbert, J., Lledó, J., & Pavía, J. M. (2024). *Dataset of an actual motor vehicle insurance portfolio*. European Actuarial Journal. https://doi.org/10.1007/s13385-024-00398-0

Publicado en Mendeley Data: https://doi.org/10.17632/5cxyb5fp4f.2
Licencia: Creative Commons CC BY 4.0

## Descripción

105.555 pólizas de una cartera real (anonimizada) de seguros de vehículos de motor en España, correspondientes al periodo noviembre 2015 - diciembre 2018. Incluye variables del vehículo (potencia, cilindrada, peso, valor), del asegurado (antigüedad, historial de siniestros) y de la póliza (prima, fecha de contrato, renovaciones).

El diccionario completo de variables está documentado en el notebook `01_data_preparation.Rmd`.

## Por qué no está el CSV en este repositorio

El archivo original pesa varios MB y no aporta valor mantenerlo versionado en Git — además de que el flujo natural es descargarlo directamente desde la fuente original. En su lugar, este repositorio incluye únicamente el código que lo procesa.

## Cómo reproducir el análisis

1. Descargar el CSV desde el enlace de Mendeley Data indicado arriba.
2. Colocarlo en esta carpeta (`data/`) sin cambiar el nombre del archivo (`Motor vehicle insurance data.csv`).
3. Ejecutar `01_data_preparation.Rmd` — genera una muestra de 10.000 registros (semilla aleatoria fija para reproducibilidad) y guarda el resultado preparado en `data/processed/prepared_model.rds`, que carga el segundo notebook.

## Estructura de esta carpeta

```
data/
├── README.md                          
├── Motor vehicle insurance data.csv   
└── prepared_model.rds
```