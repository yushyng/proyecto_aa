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

    def calcular_dias_venta(df):
        # Convertir las cadenas de fecha en objetos de fecha y hora
        df['SalesStart'] = pd.to_datetime(df['sales_datetime'])
        df['SalesEnd'] = pd.to_datetime(df['end_datetime'])

        # Calcular la diferencia entre las fechas y almacenarla en una nueva columna
        df['DiasVenta'] = (df['SalesEnd'] - df['SalesStart']).dt.days

        # Mostrar el DataFrame resultante
        return df


