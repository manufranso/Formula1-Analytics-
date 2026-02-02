# Formula 1 Analytics: Análisis de Factores de Victoria

Este proyecto analiza datos históricos de la Fórmula 1 para determinar estadísticamente qué factores influyen en el éxito de un piloto.

## Hipótesis de Investigación

### 1. El peso de la 'Pole Position'
> **Pregunta:** ¿En qué medida determina la posición de salida (grid) la probabilidad de victoria en una carrera?
* **Objetivo:** Cuantificar la correlación entre la clasificación (`grid`) y la posición final (`positionOrder`).

### 2. El efecto ventaja de ser local
> **Pregunta:** ¿Existe una mejora estadísticamente significativa en el rendimiento medio de los pilotos cuando compiten en un Gran Premio celebrado en su país de origen?
* **Objetivo:** Comparar el rendimiento medio (puntos/posición) en circuitos locales vs. circuitos extranjeros.

## Herramientas y Datos

* **Stack Tecnológico:** Python (Pandas, Requests).
* **Fuentes de Datos:**
    * **Archivos CSV:** `results`, `races`, `drivers`, `constructors`, `status`.
    * **API Externa:** `jolpi.ca/ergast/f1/circuits` (base de datos geográfica).

## Estructura del Repositorio

```text
├── data/          
├── notebooks/    
├── src/          
└── README.md   
```  