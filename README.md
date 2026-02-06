# Formula 1 Analytics: Analisis de Factores de Victoria

Este proyecto analiza datos históricos de la Fórmula 1 para determinar estadísticamente qué factores influyen en el éxito de un piloto.


* **Fuentes de Datos:**
    * **Archivos CSV:** `results`, `races`, `drivers`, `constructors`, `status`, `circuits`. (https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
    * **API Externa:** `jolpi.ca/ergast/f1/circuits` (base de datos geográfica).


## Hipótesis de Investigación

### 1. El peso de la 'Pole Position'
> **Pregunta:** ¿En qué medida determina la posición de salida (grid) la probabilidad de victoria en una carrera?
* **Objetivo:** Cuantificar la correlación entre la clasificación  y la posición final 

### 2. El efecto ventaja de ser local
> **Pregunta:** ¿Existe una mejora estadísticamente significativa en el rendimiento medio de los pilotos cuando compiten en una carrera celebrada en su país de origen?
* **Objetivo:** Comparar el rendimiento medio (puntos/posición) en circuitos locales vs. circuitos extranjeros.




## Metodología 

- El proyecto lo he realizado utilizando íntegramente Python y diferentes librerías como Pandas, Matplotlib y Seaborn.
- **Fuentes** :
     Utilicé 6 csv históricos extraídos de la base de datos Formula 1 World Championship (1950 - 2024) y un csv con la información geográfica de los circuitos extraído de la API Externa: `jolpi.ca/ergast/f1/circuits`.
- **Proceso exploratorio y limpieza** :
     Construí la función **limpieza_tablas** para comprobar automáticamente nulos y duplicados en todos los dataframes. Las tablas de los csv estaban generalmente limpias, con muy pocos duplicados en la tabla `results`, debido a que había pilotos que habían participado en una misma carrera más de 1 vez. Por ello apliqué un filtro para conservar la mayor puntuación/posición final.
- **Proceso de estandarización** :
     Construí un diccionario para cruzar nacionalidades de pilotos con sus países de origen (ej: Belgian -> Belgium,Britihs -> UK), creando así una columna nueva llamada pais_piloto para poder comparar con el país del circuito.
- **Formación del df_analisis_final**:
    Desarrollé un dataset (`df_analisis_final.csv`) uniendo los CSVs ya formateados mediante `lefts joins`
        `Results.csv` para obtener los años, posiciones y puntos
        `Races.csv` para obtener el nombre del circuito
        `Drivers.csv` para obtener el nombre del piloto y su nacionalidad
        `Circuits.csv` para obtener el país del circuito
        `api_circuits.csv` para comparar lat y lng con circuits.csv y comprobar que el circuito es el mismo en ambas fuentes de datos.
- **Creación de tablas para el análisis** :
    - Para responder a ambas hipótesis creé dos tablas:
        - `gano_desde_pole` (booleano) comparando la posición de salida y posición al final de carrera
        - `es_local` (booleano) comparando el país del piloto con el país del circuito




## CONCLUSIONES

### Hipótesis 1:
    * Respecto a la pregunta, ¿En qué medida determina la posición de salida (grid) la probabilidad de victoria en una carrera?
    - Los datos demuestran  que el promedio de victoria saliendo desde la pole es de un **41,8%**, determinando que salir desde primera posición es un factor clave  , con un histórico  demostrado  de **481** victorias saliendo desde la primera posición.
 
### Hipótesis 2:
    * Respecto a la pregunta, ¿Existe una mejora estadísticamente significativa en el rendimiento medio de los pilotos cuando compiten en un carrera celebrada en su país de origen?
    - Los datos nos indican históricamente que el efecto de ser local no es determinante, con un porcentaje histórico de victorias del **8,2%** en circuitos locales( 93 victorias locales en total) y un porcentaje histórico de victorias del **91,8%** de victorias de pilotos en circuitos no locales ( 1035 victorias no locales en total). El análisis también nos indica que el piloto local tiene una media de puntos de **5.47** y el piloto no local tiene una media de puntos de **6.59**, Una diferencia de puntos media de **1.12** puntos a favor del piloto no local. Esto puede ser debido a que los pilotos locales no siempre son los mejores.


## Errores a tener en cuenta

    - En la columna pais_circuito hay filas que aparecen con el valor UAE. Como próximo  paso se podría tener una limpieza más profunda desde otras bases de datos

## Futuros pasos

    - Análisis por escuderías: Comparar el % de victorias de compañeros de equipo con el mismo coche 
    - Análisis por décadas: Analizar como ha evolucionado el porcentaje de victorias de los pilotos en función de la década
    - Análisis por clima: Analizar como ha evolucionado el porcentaje de victorias de los pilotos en función del clima


 - Presentacion: https://docs.google.com/presentation/d/187wp5J4cNm-4ogfHbtCjXx7JMiBMB20RDB8oUOl8uxs/edit?slide=id.g3c400963539_2_66#slide=id.g3c400963539_2_66