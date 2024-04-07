import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
class Integracion:
    def _init_(self, dataframe):
        self.dataframe = dataframe

    def calcular_nunoches(self):
        """
        Calcula las noches consecutivas para eventos con el mismo nombre y lugar.
        """
        from datetime import datetime, timedelta

        # Ordenar el DataFrame por nombre del evento y fecha
        self.dataframe = self.dataframe.sort_values(by=['name', 'startDateTime'])

        # Inicializar el contador de noches
        contador_nunoches = 1

        # Lista para almacenar los índices de las filas que se eliminarán
        filas_a_eliminar = []

        # Iterar sobre las filas del DataFrame
        for index, row in self.dataframe.iterrows():
            # Obtener el nombre del evento, la fecha y el nombre del lugar de la fila actual
            evento_actual = row['name']
            fecha_actual = datetime.strptime(row['startDateTime'], '%Y-%m-%dT%H:%M:%SZ')
            lugar_actual = row['VenueName']

            # Buscar en todo el DataFrame las filas que cumplan con las condiciones
            for i, r in self.dataframe.iloc[index+1:].iterrows():
                evento_siguiente = r['name']
                fecha_siguiente = datetime.strptime(r['startDateTime'], '%Y-%m-%dT%H:%M:%SZ')
                lugar_siguiente = r['VenueName']

                # Verificar si el evento es el mismo y la fecha es 1 día después y el mismo lugar
                if evento_actual == evento_siguiente and lugar_actual == lugar_siguiente and \
                        fecha_siguiente - fecha_actual == timedelta(days=1):
                    # Incrementar el contador de noches y agregar el índice de la fila siguiente para eliminarla
                    contador_nunoches += 1
                    filas_a_eliminar.append(i)

                    # Agregar el contador de noches a la fila actual del DataFrame
                    self.dataframe.at[index, 'Noches'] = contador_nunoches

        # Eliminar las filas marcadas para eliminar
        self.dataframe = self.dataframe.drop(filas_a_eliminar)

        # Resetear los índices para que estén ordenados
        self.dataframe = self.dataframe.reset_index(drop=True)

        return self.dataframe

    import pandas as pd

    '''Variable que nos dice cúantos dias entan en venta unas entradas'''
    def calcular_dias_venta(df):
        # Convertir las cadenas de fecha en objetos de fecha y hora
        df['SalesStart'] = pd.to_datetime(df['sales_datetime'])
        df['SalesEnd'] = pd.to_datetime(df['end_datetime'])

        # Calcular la diferencia entre las fechas y almacenarla en una nueva columna
        df['DiasVenta'] = (df['SalesEnd'] - df['SalesStart']).dt.days

        # Mostrar el DataFrame resultante
        return df

    import pandas as pd

    def agregar_total_promotor(df):
        # Calcular la frecuencia de cada promotor en la columna 'promotor'
        frecuencia_promotores = df['promoter'].value_counts()

        # Mapear los recuentos de frecuencia a cada fila correspondiente
        df['peso_promotor'] = df['promoter'].map(frecuencia_promotores)

        return df

    def agregar_columna_tiene_lastfm_url(df):
        """
        Agrega una nueva columna llamada 'tiene_lastfm_url' al DataFrame df.
        La columna tendrá valor 1 si lastfm_url no es NaN, 0 de lo contrario.

        Parámetros:
            df (DataFrame): El DataFrame al que se agregará la columna.

        Retorna:
            DataFrame: El DataFrame con la nueva columna agregada.
        """
        df['tiene_lastfm_url'] = df['lastfm_url'].notna().astype(int)
        return df

    def obtener_edad_desde_wikipedia(url_wikipedia):
        # Realizar la solicitud HTTP
        response = requests.get(url_wikipedia)

        # Comprobar si la solicitud fue exitosa
        if response.status_code == 200:
            # Analizar el HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar la sección que contiene la fecha de nacimiento
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                fecha_nacimiento_tag = infobox.find(text=re.compile(r'\b\d+\s+años\b'))
                if fecha_nacimiento_tag:
                    # Obtener el texto que contiene el número de años
                    texto = fecha_nacimiento_tag.strip()

                    # Extraer el número de años utilizando expresiones regulares
                    patron = r'\b(\d+)\s+años\b'
                    resultado = re.search(patron, texto)

                    # Si se encuentra el número de años, calcular la edad
                    if resultado:
                        numero_anios = int(resultado.group(1))

                        # Obtener la fecha actual
                        fecha_actual = datetime.now()

                        # Calcular el año de nacimiento
                        ano_nacimiento = fecha_actual.year - numero_anios

                        # Devolver la edad
                        return fecha_actual.year - ano_nacimiento
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None

    #Funcion para crear la variable dias_desde_finVenta
    def calcular_dias_desde_finVenta(df):
        df['startDateTime'] = pd.to_datetime(df['startDateTime'])
        df['dias_desde_finVenta'] = (df['startDateTime'] - df['end_datetime']).dt.days
        return df


