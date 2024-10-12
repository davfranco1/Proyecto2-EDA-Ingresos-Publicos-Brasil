import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# En este soporte se incluyen todas las funciones que utilizan los notebooks "1_Exploración",
# "2_Limpieza", "3_Visualización y Análisis" y "Soporte_Diccionarios".


def nombrecolumnas(dataframe, cambio_nombre_columnas):
    """
    Renombra las columnas de un DataFrame según un diccionario de cambios.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene las columnas a renombrar.
    cambio_nombre_columnas (dict): Diccionario con los nombres antiguos como llaves y los nuevos nombres como valores.

    Retorna:
    DataFrame: El DataFrame con las columnas renombradas.
    """
    dataframe = dataframe.rename(columns=cambio_nombre_columnas)
    return dataframe


def valores_numeros(dataframe, columna):
    """
    Convierte los valores de una columna de strings a números flotantes.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene la columna a convertir.
    columna (str): Nombre de la columna a convertir.

    Retorna:
    DataFrame: El DataFrame con los valores de la columna convertidos a números flotantes.
    """
    dataframe[columna] = dataframe[columna].str.replace(',', '.')
    dataframe[columna] = dataframe[columna].apply(float)
    dataframe[columna] = dataframe[columna].apply(lambda x: "{:.2f}".format(x))
    dataframe[columna] = dataframe[columna].apply(float) #repetida porque linea 3 reconvierte a object
    return dataframe


def nulos_categoricos(dataframe, columna):
    """
    Rellena los valores nulos de una columna categórica con 'Desconocido'.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene la columna a rellenar.
    columna (str): Nombre de la columna a rellenar.

    Retorna:
    DataFrame: El DataFrame con los valores nulos rellenados.
    """
    dataframe[columna] = dataframe[columna].fillna("Desconocido")
    return dataframe


def nulos_ceros(dataframe, columna):
    """
    Rellena los valores nulos de una columna numérica con 0.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene la columna a rellenar.
    columna (str): Nombre de la columna a rellenar.

    Retorna:
    DataFrame: El DataFrame con los valores nulos rellenados.
    """
    dataframe[columna] = dataframe[columna].fillna(0)
    return dataframe


def rellenar_anos(dataframe):
    """
    Rellena la columna 'ano_ejercicio' con los años proporcionados.

    Parámetros:
    dataframe (list of DataFrames): Lista de DataFrames que contienen la columna 'ano_ejercicio'.

    Retorna:
    list of DataFrames: La lista de DataFrames con la columna 'ano_ejercicio' rellenada.
    """
    indice = 0
    años = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    for df in dataframe:
        df["ano_ejercicio"] = años[indice]
        indice += 1
    return dataframe


def conversion_fecha(dataframe, fecha):
    """
    Convierte una columna de strings a fechas, manejando errores.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene la columna a convertir.
    fecha (str): Nombre de la columna a convertir.

    Retorna:
    DataFrame: El DataFrame con los valores de la columna convertidos a fechas.
    """
    dataframe[fecha] = pd.to_datetime(dataframe[fecha], errors="coerce")
    return dataframe


def rellenar_codigos_nombres(dataframe, codigo, nombre, diccionario):
    """
    Rellena los códigos de los nombres utilizando un diccionario dado y elimina la columna de nombres.

    Parámetros:
    dataframe (DataFrame): DataFrame que contiene las columnas de código y nombre.
    codigo (str): Nombre de la columna que contiene los códigos.
    nombre (str): Nombre de la columna que contiene los nombres.
    diccionario (dict): Diccionario usado para reemplazar los valores en la columna de códigos.

    Retorna:
    DataFrame: El DataFrame con los códigos rellenos y la columna de nombres eliminada.
    """
    dataframe[codigo] = dataframe[codigo].replace(diccionario)
    # Reemplaza los valores de la columna 'codigo' usando el diccionario proporcionado
     
    dataframe[dataframe[codigo].isna() & dataframe[nombre].notna()][[codigo, nombre]].head()
    # Selecciona y muestra las primeras filas donde la columna 'codigo' es NaN (faltante) y la columna 'nombre' no es NaN

    dataframe.loc[dataframe[codigo].isna() & dataframe[nombre].notna(), codigo] = dataframe[nombre]
    # Asigna los valores de la columna 'nombre' a la columna 'codigo' donde 'codigo' es NaN y 'nombre' no es NaN

    dataframe.drop(columns=[nombre], inplace=True)
    # Elimina la columna 'nombre' del DataFrame

    return dataframe


def traducir_dicc(dataframe, columna, diccionario):
    """
    Traduce los valores de una columna de un DataFrame usando un diccionario dado.

    Parámetros:
    dataframe (DataFrame): El DataFrame que contiene la columna a traducir.
    columna (str): Nombre de la columna cuyos valores serán traducidos.
    diccionario (dict): Diccionario usado para reemplazar los valores en la columna.

    Retorna:
    DataFrame: El DataFrame con los valores de la columna traducidos.
    """
    dataframe[columna] = dataframe[columna].replace(diccionario)
    return dataframe

