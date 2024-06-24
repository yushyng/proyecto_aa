import pandas as pd
import os
import sys

class Carga:
    def __init__(self, archivos):
        self.archivos = archivos
        self.df_total = None

    def cargar_archivos(self):
        """Carga los archivos CSV especificados en la lista self.archivos y los concatena
        en un solo DataFrame llamado self.df_total."""
        # paso 1: añadir la carpeta 'drive' al path
        ruta_carpeta_drive = os.path.abspath('../drive') #.. era para salirse de la carpeta actual y entrar en la de drive
        if ruta_carpeta_drive not in sys.path:
            sys.path.insert(0, ruta_carpeta_drive)

        import drive

        # paso 2: Descargamos los datos en formato csv de Google Drive y los guardamos localmente
        dataframes = []
        for archivo in self.archivos:
            drive.descargar_archivos_concretos(archivo, '../drive')
            df = pd.read_csv(f'datos/{archivo}')
            dataframes.append(df)
        self.df_total = pd.concat(dataframes, ignore_index=True)