# Proyecto 2: EDA de los Ingresos Públicos de Brasil en el período comprendido entre 2013 y 2021.

![imagen](imagenes/header.jpeg)

En Data Science, EDA significa Exploratory Data Analysis (Análisis Exploratorio de Datos). Es una técnica utilizada para analizar y comprender conjuntos de datos, que permitan sacar conclusiones ellos o, aplicar modelos más complejos a posteriori.

Sus objetivos principales son:
- Revelar estructuras subyacentes en los datos.
- Identificar patrones o anomalías.
- Entender las relaciones entre variables.

A menudo, se emplean métodos de visualización de datos para resumir las características principales y obtener una mejor comprensión de los datos.

Lo anterior, es lo que aplicaremos para este proyecto.


## Planteamiento: **Análisis de la Ejecución de Ingresos Públicos en Brasil**

El gobierno de Brasil, a través de sus distintos órganos, gestiona la recaudación de ingresos públicos para financiar los servicios y proyectos que benefician a la sociedad. Cada año, se realiza una planificación detallada para prever cuánto se espera recaudar, pero a menudo la recaudación real difiere de lo previsto debido a diversos factores como la evasión fiscal, fluctuaciones económicas, ineficiencias administrativas, entre otros.

Has sido contratado por la Secretaría de Hacienda para analizar los datos históricos de la ejecución de ingresos entre 2013 y 2021. La misión es identificar patrones, detectar áreas problemáticas donde la recaudación ha sido consistentemente menor a lo previsto, y proponer recomendaciones basadas en los datos que ayuden a mejorar la precisión de las previsiones y la eficiencia de la recaudación.

Los problemas concretos que nos han pedido resolver son:

1.	**Desviaciones entre lo previsto y lo recaudado**: Determinar en qué categorías económicas o tipos de ingresos las diferencias son más pronunciadas.

2.	**Evolución temporal de la recaudación**: Identificar cómo han cambiado las previsiones y recaudaciones año a año, y si existen patrones temporales, como meses específicos donde hay mayores discrepancias.

3.	**Rendimiento por órgano y unidad gestora**: Evaluar qué órganos o unidades gestoras son más eficientes en términos de alcanzar las metas de recaudación y cuáles presentan consistentemente una baja ejecución.


## Objetivos del Proyecto

- **Limpieza de datos:** Resolver problemas comunes como valores nulos, formatos inconsistentes y duplicados.

- **Unión de conjuntos de datos:** Combinar todos los archivos en un solo dataframe para análisis global. Si es necesario, deberéis crear una columna extra para no perder información. 

- **Análisis Exploratorio de Datos (EDA):** Examinar la relación entre diferentes variables clave y explorar categorías relevantes para identificar patrones o discrepancias significativas.

- **Visualización:** Generar gráficos que permitan identificar tendencias y patrones relevantes en los datos analizados.


## Estructura del repositorio:

### Notebooks
Las distintas fases del proyecto se han dividido en tres cuadernos de Jupyter (.ipynb).

1. Exploración: entender la estructura y relaciones de los datos para unificarlos en un sólo dataframe.

2. Limpieza: ejecutar tareas de normalización de los datos, incluyendo nombres de columnas, nulos, duplicados y tipos de datos.

3. Análisis y Visualización: identificar relaciones, tendencias y usar herramientas de visualización para explicarlas.

4. Soporte_Diccionarios: creación de diccionarios ubicados en "soporte_variables.py"


### Src:
Archivos de soporte:

1. soporte_limpieza: archivo .py con funciones utilizadas en el tratamiento de los datos.

2. soporte_variables: archivo .py que almacena diccionarios usados para el tratamiento de los datos.


### Datos
Aquí pueden consultarse los datos sin tratar del proyecto. Los CSVs resultantes de la unión y limpieza no pueden ser consultados por la limitación de 100MB en el tamaño de archivo de GitHub.


### Imágenes
Archivos de imagen de soporte para el proyecto.


## Conclusiones
Las principales conclusiones del EDA pueden consultarse en cada cuaderno, pero mencionamos algunas:


## Próximos Pasos