from Carga import Carga
import pandas as pd
import json
from LimpiezaInicial import LimpiezaInicial
# Lista de archivos a cargar
archivos = [
'/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/d_17_02.csv',
 '/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/d_1_03.csv',
 '/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/d_21_02.csv',
 '/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/d_26_02.csv',
 '/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/d_28_02.csv',
 '/Users/yushanyang/Desktop/ProyectoDatos/Proyecto/csvs/adquisicion/datos_5_03.csv'
]

# Instanciar la clase y cargar los archivos
cargador = Carga(archivos)
cargador.cargar_archivos()

# Limpiar los datos
cargador.limpiar_datos()

# Obtener el DataFrame total
df_total = cargador.df_total
print("Longitud del DataFrame total:", len(df_total))
limpieza = LimpiezaInicial()

# Filtrar strings
strings_filtrar = ['film', 'servicio de autobús', 'festival', 'vip', 'meet', 'meet & greet', 'ticket', 'package',
                   'musical']
df_total = limpieza.limpiar_strings(df_total, strings_filtrar)

# Lista de columnas a corregir
columnas_a_corregir = ['sales', 'dates', 'classifications', 'promoter', 'priceRanges']

# Aplicar la función de corrección a las columnas_a_corregir
df_total = limpieza.corregir_columnas(df_total, columnas_a_corregir)

# Aplicar los métodos para obtener las variables que queremos
df_total['startDateTime'] = df_total.apply(limpieza.obtener_start_datetime, axis=1)
df_total['end_datetime'] = df_total.apply(limpieza.obtener_end_datetime, axis=1)
df_total['min_price'] = df_total.apply(limpieza.obtener_min_price, axis=1)
df_total['max_price'] = df_total.apply(limpieza.obtener_max_price, axis=1)
df_total['genero'] = df_total.apply(limpieza.obtener_genero, axis=1)
df_total['subgnero'] = df_total.apply(limpieza.obtener_subgenero, axis=1)
df_total['promoter'] = df_total.apply(limpieza.obtener_promotor, axis=1)

df_total = df_total.reset_index(drop=True)
df_total = df_total.drop(columns=['sales','dates','classifications','priceRanges'])
#Es probable que no encontremos información de los oyenetes de los géneros: Classical,
# Theatre, Fairs & Festivals. Esta será una de nuestras variables principales por lo que
# al no tenerla no podremos usar estos datos como prueba.
print(df_total)
generos = ['Classical', 'Theatre', 'Fairs & Festivals']
df_total = df_total[~df_total['genero'].isin(generos)]
print(len(df_total))
df_total['columna_json'] = df_total['_embedded'].apply(load_json)

