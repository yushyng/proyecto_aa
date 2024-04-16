import pandas as pd

class Carga:
    def __init__(self, archivos):
        self.archivos = archivos
        self.df_total = None

    def cargar_archivos(self):
        """Carga los archivos CSV especificados en la lista self.archivos y los concatena
        en un solo DataFrame llamado self.df_total."""
        dataframes = []
        for archivo in self.archivos:
            df = pd.read_csv(archivo)
            dataframes.append(df)
        self.df_total = pd.concat(dataframes, ignore_index=True)

    
