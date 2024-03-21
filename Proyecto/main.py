from Carga import Carga
from LimpiezaInicial import LimpiezaInicial
from YoutubeSubs import YoutubeSubs
from Spotify import Spotify
import time
from LastFm import LastFm
import requests

archivos = ['csvs/adquisicion/d_1_03.csv', 'csvs/adquisicion/d_17_02.csv',
            'csvs/adquisicion/d_21_02.csv', 'csvs/adquisicion/d_26_02.csv',
            'csvs/adquisicion/d_28_02.csv', 'csvs/adquisicion/datos_5_03.csv']

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
df_total = df_total.drop(columns=['sales', 'dates', 'classifications', 'priceRanges'])
#Es probable que no encontremos información de los oyenetes de los géneros: Classical,
# Theatre, Fairs & Festivals. Esta será una de nuestras variables principales por lo que
# al no tenerla no podremos usar estos datos como prueba.
print(df_total)
generos = ['Classical', 'Theatre', 'Fairs & Festivals']
df_total = df_total[~df_total['genero'].isin(generos)]
print(len(df_total))
generos = ['Classical', 'Theatre', 'Fairs & Festivals']
df_total = df_total[~df_total['genero'].isin(generos)]


df_total = LimpiezaInicial.arreglo_embeded(df_total)
df_total['columna_json'] = df_total['_embedded'].apply(limpieza.load_json)

print(df_total['columna_json'])
print(len(df_total))

print("Nulos en la columna embdededd cambiada", df_total['columna_json'].isnull().sum())

df_total = df_total.dropna(subset=['columna_json'])

#df_total['nameArtist'] = df_total.apply(LimpiezaInicial.name, axis=1).copy()
df_total['nameArtist'] = df_total.apply(lambda fila: LimpiezaInicial().name(fila), axis=1).copy()
print(df_total['nameArtist'].isnull().sum())

df_total['genre'] = df_total.apply(lambda fila: limpieza.genre_event(fila), axis=1).copy()
df_total['subgenre'] = df_total.apply(lambda fila: limpieza.subgenre_event(fila), axis=1).copy()
df_total['type'] = df_total.apply(lambda fila: limpieza.type_event(fila), axis=1).copy()
df_total['subtype'] = df_total.apply(lambda fila: limpieza.subtype_event(fila), axis=1).copy()
df_total['VenueName'] = df_total.apply(lambda fila: limpieza.venue_name(fila), axis=1).copy()
df_total['VenueCity'] = df_total.apply(lambda fila: limpieza.venue_city(fila), axis=1).copy()
df_total['VenueState'] = df_total.apply(lambda fila: limpieza.venue_state(fila), axis=1).copy()
df_total['VenueCountry'] = df_total.apply(lambda fila: limpieza.venue_country(fila), axis=1).copy()


df_total['links'] = df_total.apply(lambda fila: limpieza.links(fila), axis=1)
df_total['num_links'] = df_total.apply(lambda fila: limpieza.num_links(fila), axis=1)
#print(df_total.iloc[0]['links']['spotify'][0]['url'])

'''client_id = '3e082f0f2dd240c1beb66c9705a663a5'
client_secret = 'd3dd1f7886eb4ba4aa5a76c9095120d7'
spotify = Spotify(client_id, client_secret)

#print(df_total['links'].isnull().sum())


# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'links'
inicio = time.time()
df_total['spotify_url'] = df_total['links'].apply(lambda x: x['spotify'][0]['url'] if x and 'spotify' in x and isinstance(x['spotify'], list) and len(x['spotify']) > 0 else None)

# Registrar el tiempo de finalización
fin = time.time()

# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
# Mostrar el DataFrame df_total con la nueva columna 'spotify_url'
print(df_total['spotify_url'])

df_total['spotify_url'] = df_total['spotify_url'].astype(str)

# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'spotify_url'
df_total['seguidores'] = df_total['spotify_url'].apply(spotify.obtener_seguidores_por_fila)'''



'''lastfm_client = LastFm("d3668e7b9ace955aaefafa6e262386ba")
df_total['lastfm_url'] = df_total['links'].apply(lambda x: x['lastfm'][0]['url'] if x and 'lastfm' in x and isinstance(x['lastfm'], list) and len(x['lastfm']) > 0 else None)
df_total['seguidoresLast'] = df_total['lastfm_url'].apply(lastfm_client.obtener_seguidores_lastf