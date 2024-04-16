import pandas as pd
from Exploracion import Exploracion
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

# Lee el archivo CSV despúes de Limpieza
df_total = pd.read_csv('dfLimpio.csv')
print("\nEXPLORACIÓN DE LOS DATOS")
exploracion=Exploracion()
#vemos la info del df
exploracion.resumen(df_total)

#las columnas que tiene
exploracion.visualizar_columnas(df_total)

#Estudiamos la correlacion de las variables numéricas

matriz_correlacion_resultante = exploracion.calcular_matriz_correlacion(df_total)

# Crear el heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(matriz_correlacion_resultante, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, vmin=-1, vmax=1)
plt.title('Matriz de Correlación')
plt.show()

#Estudiamos las correlaciones de las variables categoricas
resultado_tabla = exploracion.calcular_coeficiente_contingencia(df_total, 'nameArtist', 'VenueName')
print(resultado_tabla)

resultado_tabla = exploracion.calcular_coeficiente_contingencia(df_total, 'VenueCity', 'VenueName')
print(resultado_tabla)

resultado_tabla = exploracion.calcular_coeficiente_contingencia(df_total, 'VenueState', 'VenueName')
print(resultado_tabla)

resultado_tabla = exploracion.calcular_coeficiente_contingencia(df_total, 'VenueState', 'nameArtist')
print(resultado_tabla)

#Análisis exploratorio de los outliers

exploracion.plot_boxplots(df_total, 'min_price', 'max_price')
#Vemos que hay un caso atipico de un concierto donde el maximo precio de la entrada son 60000, esto 
#produciria un sesgo en nuestro modelo por lo que decidimos eliminarlo

df_total[df_total['name']=='Luis Miguel']
# Eliminar la fila número siete
df_total = df_total.drop(7)

# Reorganizar los índices
df_total = df_total.reset_index(drop=True)
df_total[df_total['name']=='Luis Miguel']

#Vemos que ya no tenemos valores nulos tras hacer KKN y la limpieza 
msno.matrix(df_total)

#Vamos a crear este nuevo dataframe, con las columnas finales ya ordenadas.
# Suponiendo que df es tu DataFrame y column_order es la lista de nombres de columnas en el orden deseado
column_order = ['name', 'EventStartTime', 'SalesStartTIme', 'SalesEndTime', 'min_price',
       'max_price', 'nameArtist', 'VenueName', 'VenueCity', 'VenueState',
       'num_links', 'seguidoresSpotify', 'popularidad', 'subsYT', 'VenueClass',
       'NumGeneros', 'peso_promotor', 'tiene_lastfm_url', 'Generos_combinados',
       'conciertos_del_artista_en_ciudad', 'tiene_twitter', 'tiene_instagram',
       'tiene_itunes', 'tiene_homepage', 'Adult Contemporary', 'Alternative',
       'Alternative Rock', 'Ballads/Romantic', 'Blues', 'Classical',
       'Classical/Vocal', 'Club Dance', 'Dance', 'Dance/Electronic',
       'Flamenco', 'Folk', 'Funky Breaks', 'Hard Rock', 'Heavy Metal',
       'Hip-Hop/Rap', 'Indie Pop', 'Jazz', 'Jazz Blues', 'K-Pop', 'Latin',
       'Latin Pop', 'Metal', 'New Wave', 'Other', 'Performance Art', 'Pop',
       'Pop Metal', 'Pop Rock', 'Pop Vocal', 'Psychedelic', 'R&B', 'Reggae',
       'Rock', 'Singer-Songwriter', 'Soul', 'Urban', 'World', 'tiene_wiki',
       'tiene_youtube', 'dias_Venta', 'dias_desdeFinVenta', 'num_noches']

df_Final = df_total.reindex(columns=column_order)
#Con esto nuestro conjunto de datos esta preparado para el entrenamiento.
#Descarga del dataframe tras el proceso de Exploracion
df_Final.to_csv('dfFinal.csv', index=False)