# Funcion descargar API
import pandas as pd
import requests
import numpy as np



# Funcion descargar API
def descargar_api():


    """
    Descarga la lista de circuitos de F1 desde la API de Ergast y la guarda en CSV.
    Realiza una petición GET a la API, procesa el JSON anidado ('MRData' > 'CircuitTable' > 'Circuits')
    y convierte los resultados en un DataFrame de Pandas.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de los circuitos o un DataFrame vacío en caso de error.
    """


    
    url_api = "https://api.jolpi.ca/ergast/f1/circuits.json?limit=100"
    ruta_guardado = "../data/api_circuits.csv"

    print(f"Descargando API desde {url_api}")

    try:
        # Peticion con gestion de limites de tiempo
        response = requests.get(url_api, timeout=10)
        response.raise_for_status()
    
        # Procesamiento
        data = response.json()
        df_circuitos = pd.DataFrame(data['MRData']['CircuitTable']['Circuits'])  #"La API devuelve una estructura JSON anidada. Para extraer la lista de circuitos y convertirlos en un DataFrame 

        # Guardar en local
        df_circuitos.to_csv(ruta_guardado, index=False)
        print(f" Guardado en: {ruta_guardado}")

        return df_circuitos
    
    except Exception as e:
        print(f" Error en API: {e}")
        return pd.DataFrame()



# Funcion de limpieza de tablas 

def limpieza_tablas(dicc_dfs):
    """
    Realiza un análisis de calidad de datos sobre un diccionario de DataFrames.
    Itera sobre cada DataFrame para detectar:
    Valores nulos.
    Duplicados (filas completas y por IDs específicos).
    Espacios en blanco en columnas de texto.
    Estadísticas básicas (min/max) de columnas numéricas.
    """



    for nombre,tabla, in dicc_dfs.items():
        # Comporbacion de nulos
        nulos = tabla.isnull().sum().sum()
        if nulos > 0:
            print(f"Tabla {nombre} tiene {nulos} nulos")
            print(tabla.isnull().sum()[tabla.isnull().sum() > 0])

        else: 
            print(f"Tabla {nombre} no tiene nulos")

        # Comprobacion de duplicados
        try: 
            duplicados = tabla.duplicated().sum()
        except TypeError:
            duplicados = tabla.astype(str).duplicated().sum()
            if duplicados > 0:
                print(f"Tabla {nombre} tiene {duplicados} duplicados")
        else:
            print(f"Tabla {nombre} no tiene duplicados")

        # Comprobacion de IDs Duplicados
        cols_id = [c for c in ['driverId', 'constructorId', 'raceId', 'circuitId'] if c in tabla.columns]
        
        if cols_id:
            ids_duplicados = tabla.duplicated(subset=cols_id).sum()
            if ids_duplicados > 0:
                print(f"Tabla {nombre} tiene {ids_duplicados} IDs duplicados")
            else:
                print(f"Tabla {nombre} no tiene IDs duplicados")
        
        # Comprobacion de strings 
        objeto_cols = tabla.select_dtypes(include=[object]).columns.tolist()
        if objeto_cols:
            espacios = 0
            for col in objeto_cols:
                espacios += (tabla[col].astype(str).str.strip() == "").sum()
                print(f"Tabla {nombre} tiene {espacios} espacios en blanco en la columna {col}")
            if espacios > 0:
                print(f"Tabla {nombre} tiene {espacios} espacios en blanco")

        # Estadisticas
        num_cols = tabla.select_dtypes(include=[np.number]).columns.tolist()
        if num_cols:
            print(tabla.describe().loc[['min','max']])


# Funcion para seleccionar y cambiar nombre de columnas 
        
def columnas_analisis(df):
    """
    Selecciona y renombra las columnas relevantes del DataFrame para el análisis.
    Filtra el DataFrame original manteniendo solo las columnas definidas en el mapeo
    y las renombra al español para facilitar su interpretación (ej. 'year' -> 'año').
    """

    renombrar_columnas = {
        'year': 'año',
        'surname': 'apellido_piloto',
        'nationality': 'nacionalidad_piloto',
        'circuitName': 'nombre_circuito',
        'country': 'pais_circuito',
        'grid': 'posicion_salida',
        'positionOrder': 'posicion_final',
        'points': 'puntos',
        'raceId': 'id_carrera',
        'driverId': 'id_piloto'
    }

    
    
    # Comprobacion de columnas existenetes para evitar errores
    columnas_validas = [col for col in renombrar_columnas.keys() if col in df.columns]
    print(f"Columnas originales: {df.shape[1]}.")
    print(f"COlumnas para el analisis: {len(columnas_validas)}")

    df_resultado = df[columnas_validas].copy()
    return df_resultado.rename(columns=renombrar_columnas)


# Funcion para obtener el pais del piloto, para saber si es local o no

#  Diccionario de nacionalidades a paises
nacionalidad_a_pais = {
    'American': 'USA',
    'American-Italian': 'USA',
    'Argentine': 'Argentina',
    'Argentinian': 'Argentina',
    'Australian': 'Australia',
    'Austrian': 'Austria',
    'Belgian': 'Belgium',
    'Brazilian': 'Brazil',
    'British': 'UK',
    'Canadian': 'Canada',
    'Chinese': 'China',
    'Dutch': 'Netherlands',
    'French': 'France',
    'German': 'Germany',
    'Hungarian': 'Hungary',
    'Indian': 'India',
    'Italian': 'Italy',
    'Japanese': 'Japan',
    'Malaysian': 'Malaysia',
    'Mexican': 'Mexico',
    'Monegasque': 'Monaco',
    'Portuguese': 'Portugal',
    'Russian': 'Russia',
    'South African': 'South Africa',
    'Spanish': 'Spain',
    'Swedish': 'Sweden',
    'Swiss': 'Switzerland'
}

def pais_piloto(nacionalidad):
    """
    Mapea la nacionalidad de un piloto a su país correspondiente.
    Utiliza el diccionario `nacionalidad_a_pais` para la conversión. 
    Útil para comparar la nacionalidad del piloto con el país del circuito.
    (Ej. Nacionalidad del piloto (ej. 'British', 'Spanish').
    Nombre del país (ej. 'UK', 'Spain') o el valor original si no está en el diccionario).
    """


    if not isinstance(nacionalidad, str):
        return nacionalidad

    return nacionalidad_a_pais.get(nacionalidad.strip(), nacionalidad)



