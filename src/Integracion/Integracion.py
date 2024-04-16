import pandas as pd

class Integracion:
    def __init__(self):
        self.df_total = None

    def calcular_dias_desde_finVenta(df):
    # Convertir las columnas EventStartTime y SalesEndTime a objetos datetime
        df['EventStartTime'] = pd.to_datetime(df['EventStartTime'], format='ISO8601')
        df['SalesEndTime'] = pd.to_datetime(df['SalesEndTime'])

        # Calcular la diferencia en días entre EventStartTime y SalesEndTime para cada fila
        diferencias = []
        for index, row in df.iterrows():
            # Calcular la diferencia entre las fechas de EventStartTime y SalesEndTime en la fila actual
            diferencia = row['EventStartTime'] - row['SalesEndTime']
            # Agregar la diferencia en días a la lista de diferencias
            diferencias.append(diferencia.days)

            # Agregar la lista de diferencias como una nueva columna al DataFrame
        df['dias_desdeFinVenta'] = diferencias

        return df

  
    #Funcion para obtener el numero de dias que han estado en venta las entradas
    def calcular_dias_venta(df):
        # Convertir las columnas SalesStartTime y SalesEndTime en formato datetime
        df['SalesStartTIme'] = pd.to_datetime(df['SalesStartTIme'])
        df['SalesEndTime'] = pd.to_datetime(df['SalesEndTime'])

        diferencias = []
        for index, row in df.iterrows():
            # Calcular la diferencia entre las fechas de SalesStartTIme y SalesEndTime en la fila actual
            diferencia = row['SalesEndTime'] - row['SalesStartTIme']
            # Agregar la diferencia en días a la lista de diferencias
            diferencias.append(diferencia.days)

            # Agregar la lista de diferencias como una nueva columna al DataFrame
        df['dias_Venta'] = diferencias

    
        return df
    #Funcion para obtener las veces que aparece un promotor
    def calcular_peso_promotor(df):
         # Calcular la frecuencia de cada promotor en la columna 'promotor'
        frecuencia_promotores = df['promoter'].value_counts()

         # Mapear los recuentos de frecuencia a cada fila correspondiente
        df['peso_promotor'] = df['promoter'].map(frecuencia_promotores)
    
        return df
    #Funcion que devuelve 1 si tiene Wikipedia, 0 en otro caso
    def tiene_wiki(links):
        if isinstance(links, dict) and 'wiki'in links:
            return 1
        else:
            return 0
        
    #Funcion que devuelve 1 si tiene youtube, 0 en otro caso
    def tiene_youtube(links):
        if isinstance(links, dict) and 'youtube'in links:
         return 1
        else:
         return 0
        
    # Función para verificar si la URL de Twitter está presente
    def tiene_instagram(links):
        if isinstance(links, dict) and 'instagram'in links:
             return 1
        else:
            return 0

    # Función para verificar si la URL de Twitter está presente
    def tiene_twitter(links):
        if isinstance(links, dict) and 'twitter' in links:
         return 1
        else:
         return 0
        
    # Función para verificar si la URL de Twitter está presente
    def tiene_itunes(links):
        if isinstance(links, dict) and 'itunes'in links:
            return 1
        else:
            return 0
    # Función para verificar si el artista tiene homepage
    def tiene_homepage(links):
        if isinstance(links, dict) and 'homepage'in links:
          return 1
        else:
          return 0
        
    #Combinacion de generos del genre y subgenre
    def combinar_y_limpiar_generos(row):
        # Obtener los valores de las columnas y convertirlos a string
        genero = str(row['genre']) if row['genre'] not in ['Undefined', 'Music'] else ''
        subgenero = str(row['subgenre']) if pd.notnull(row['subgenre']) and row['subgenre'] not in ['Undefined', 'Music'] else ''
        genero_principal = str(row['genero']) if row['genero'] not in ['Undefined', 'Music'] else ''
        subgenero_principal = str(row['subgnero']) if pd.notnull(row['subgnero']) and row['subgnero'] not in ['Undefined', 'Music'] else ''

        # Combinar los géneros sin los valores "Undefined", "Music" y NaN
        generos_combinados = ','.join(set(filter(None, [genero, subgenero, genero_principal, subgenero_principal])))

        return generos_combinados
    

    
  