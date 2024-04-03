class LimpiezaFinal:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def convertir_string_a_lista(self, texto):
        """
        Convierte una cadena de texto que representa una lista en una lista de Python.
        """
        try:
            lista = eval(texto)
            if isinstance(lista, list):
                return lista
            else:
                return []
        except Exception as e:
            return []

    def aplicar_limpieza(self):
        # Aplicar la función a toda la columna 'GéneroArtista'
        self.dataframe['GéneroArtista'] = self.dataframe['GéneroArtista'].apply(self.convertir_string_a_lista)
        self.dataframe['NumGeneros'] = self.dataframe['GéneroArtista'].apply(lambda x: len(x))
        # Mostrar los primeros registros para verificar
        print(self.dataframe.head())
        self.dataframe.reset_index(drop=True)
        columnas_a_eliminar = ['lastfm_url', 'youtube_url', 'spotify_url', 'salaCiudad', 'wiki_url', 'links','GéneroArtista']
        df2 = self.dataframe.drop(columns=columnas_a_eliminar)
        columnas_a_convertir = ['seguidores', 'popularidad', 'seguidoresLast', 'subscriptores', 'premios']
        # Rellena los valores faltantes (NaN) con 0
        df2[columnas_a_convertir] = df2[columnas_a_convertir].fillna(0)

        # Convierte las columnas a enteros
        df2[columnas_a_convertir] = df2[columnas_a_convertir].astype(int)
        df2 = df2.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        df2.duplicated().sum()
        df2 = df2.drop_duplicates()
        df2.reset_index(drop=True)


