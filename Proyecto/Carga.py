import pandas as pd

class Carga:
    def __init__(self, archivos):
        self.archivos = archivos
        self.df_total = None

    def cargar_archivos(self):
        dataframes = []
        for archivo in self.archivos:
            df = pd.read_csv(archivo)
            dataframes.append(df)
        self.df_total = pd.concat(dataframes, ignore_index=True)

    def limpiar_datos(self):
        if self.df_total is not None:
            num_duplicados = self.df_total.duplicated().sum()
            print("Filas duplicadas:", num_duplicados)
            self.df_total.drop_duplicates(inplace=True)
            print("Num filas sin duplicados:", len(self.df_total))
            self.df_total.drop(columns=['id', 'test','url', 'images', 'promoters', 'type', 'locale', '_links', 'seatmap'], inplace=True)
        else:
            print("Error: No se han cargado los archivos todavía.")
