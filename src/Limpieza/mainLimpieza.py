import pandas as pd
from sklearn.impute import KNNImputer
from LimpiezFinal import LimpiezaFinal

# Lee el archivo CSV despúes de Extraccion
df_total = pd.read_csv('dfExtraccion.csv')

print("\nLIMPIEZA DE LOS DATOS")
# Elegimos el parámetro predeterminado (5) y después aplicamos a la columna dataframe
imputer = KNNImputer()
df_total['seguidores'] = imputer.fit_transform(df_total[['seguidores']])
df_total['popularidad'] = imputer.fit_transform(df_total[['popularidad']])
df_total['subscriptores'] = imputer.fit_transform(df_total[['subscriptores']])
#Para la imputación de numGnéneros en vez de usar la biblioteca de sklearn
# podemos sustituir simplemente los valores 0 por 1. Suponemos que todos los artistas pertenecen como mínimo a un género.
df_total['NumGeneros'] = df_total['NumGeneros'].replace(0, 1)

#Usamos el método One-Hot enconding para tratar con la variable ordinal venue_class.
size_mapping = {'SALA': 0,
                'TEATRO': 1,
                'ESTADIO S': 2,
                'ESTADIO M': 3}

df_total['VenueClass'] = df_total['VenueClass'].map(size_mapping)
limpieza=LimpiezaFinal()
df_total=limpieza.aplicar_limpieza(df_total)

#Vamos a eliminar las filas que tienen type o subtype = Festival (puede que queden algunas):

filas_festival = df_total[(df_total['type'] == 'Festival') | (df_total['subtype'] == 'Festival')]
filas_festival

# Índices de las filas a eliminar
indices_a_eliminar = [102, 432, 494, 495, 523]

# Eliminar las filas del DataFrame original
df2 = df_total.drop(indices_a_eliminar)

# Restablecer los índices del DataFrame resultante
df2.reset_index(drop=True, inplace=True)

#Vamos a visualizar los nulos de la variable startDateTime
num_nulos = df2['startDateTime'].isnull().sum()
print("Número de valores nulos en startDateTime:", num_nulos)


# Contar los valores NaN y 0 en la columna 'seguidoresLast'
total_nan_zero = df2['seguidoresLast'].isna().sum() + (df2['seguidoresLast'] == 0).sum()

print("Total de valores NaN y 0 en la columna 'seguidoresLast':", total_nan_zero)

#Eliminamos las variables lasFm_url y seguidoresLast ya que no nos sirven ya para nada, entre otras que ya hemos explotado lo suficiente.
columnas_a_eliminar = [ 'seguidoresLast', 'lastfm_url','promoter','genero','subgnero', 'genre', 'subgenre']
df2 = df2.drop(columns=columnas_a_eliminar)
df2

#La variable "premios" podría ser ahora completada (quizás) gracias a los nuevos links de wikipedia, así que usaremos Expresiones Regulares para intentar encontrar el número de premios (igual que hicimos con la Edad)
# Contar el número de NaNs en la columna 'premios'
num_nans_premios = df2['premios'].isna().sum()

print("Número de NaNs en la variable 'premios':", num_nans_premios)

#Decidimos eliminar la variable premios ya que tiene muchos nulos ya que no podemos usar KNN
df2 = df2.drop(columns='premios')

# Contar el número de NaNs en la columna 'Edad'
num_nans_premios = df2['Edad'].isna().sum()

print("Número de NaNs en la variable 'premios':", num_nans_premios)

#Vemos que tiene muchos nulos ya que la mayoria son bandas y no podemos sacar la edad de varios integrantes del grupo
#por lo que decidimos eliminar dicha variable
df2 = df2.drop(columns='Edad')

# Filtrar las filas con NaN en la columna "Generos_combinados"
filas_con_nan = df2.loc[df2['Generos_combinados'].isnull()]

filas_con_nan
# Rellenar la columna Generos_combinados con "Pop" en las filas con índices 21 y 515
df2.at[21, 'Generos_combinados'] = "Pop"
df2.at[515, 'Generos_combinados'] = "Pop"

# Reorganizar los índices
df2 = df2.reset_index(drop=True)


#Descarga del dataframe tras el proceso de limpieza
df2.to_csv('dfLimpio.csv', index=False)