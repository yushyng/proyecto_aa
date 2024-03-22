from extraccion.Carga import Carga
from LimpiezaInicial import LimpiezaInicial
from extraccion.YoutubeSubs import YoutubeSubs
from extraccion.Spotify import Spotify
from extraccion.Wiki import Wiki
import pandas as pd
import time
from extraccion.LastFm import LastFm
from exploracion import Exploracion
import requests

archivos = ['csvs/adquisicion/d_1_03.csv', 'csvs/adquisicion/d_17_02.csv',
            'csvs/adquisicion/d_21_02.csv', 'csvs/adquisicion/d_26_02.csv',
            'csvs/adquisicion/d_28_02.csv', 'csvs/adquisicion/datos_5_03.csv']

print("\nCARGA DEL CONJUNTO DE DATOS EN BRUTO")
# Instanciar la clase y cargar los archivos
cargador = Carga(archivos)
cargador.cargar_archivos()

# Limpiar los datos
cargador.limpiar_datos()

# Obtener el DataFrame total
df_total = cargador.df_total
print("Longitud del DataFrame total:", len(df_total))

print("\nLIMPIEZA DEL CONJUNTO DE DATOS")
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
# Es probable que no encontremos información de los oyenetes de los géneros: Classical,
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
#print(len(df_total))

print("Nulos en la columna embdededd cambiada", df_total['columna_json'].isnull().sum())

df_total = df_total.dropna(subset=['columna_json'])

#df_total['nameArtist'] = df_total.apply(LimpiezaInicial.name, axis=1).copy()
df_total['nameArtist'] = df_total.apply(lambda fila: LimpiezaInicial().name(fila), axis=1).copy()
print("Nulos en la columna nameArtist: ", df_total['nameArtist'].isnull().sum())

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

client_id = 'de2c627e722341b784a8bb67d1dda88e'
client_secret = 'ccc8b038637c4326999eec8bf12b6f1c'
spotify = Spotify(client_id, client_secret)

#print(df_total['links'].isnull().sum())


# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'spotify_url'
df_total['spotify_url'] = df_total['links'].apply(lambda x: x['spotify'][0]['url'] if x and 'spotify' in x and isinstance(x['spotify'], list) and len(x['spotify']) > 0 else None)

df_total['spotify_url'] = df_total['spotify_url'].astype(str)
# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'spotify_url'
df_total['seguidores'] = df_total['spotify_url'].apply(spotify.obtener_seguidores_por_fila)
df_total['popularidad'] = df_total['spotify_url'].apply(spotify.obtener_popularidad_por_fila)
df_total['GéneroArtista'] = df_total['spotify_url'].apply(spotify.obtener_generosArtistas_por_fila)

lastfm_client = LastFm("d3668e7b9ace955aaefafa6e262386ba")
inicio = time.time()
df_total['lastfm_url'] = df_total['links'].apply(lambda x: x['lastfm'][0]['url'] if x and 'lastfm' in x and isinstance(x['lastfm'], list) and len(x['lastfm']) > 0 else None)
df_total['seguidoresLast'] = df_total['lastfm_url'].apply(lastfm_client.obtener_seguidores_lastfm)
fin = time.time()

api_key = "AIzaSyBnd9DxGl04Adp7VgtDrgKYbB57HqsAUvM"
inicio = time.time()
df_total['youtube_url'] = df_total['links'].apply(lambda x: x['youtube'][0]['url'] if x and 'youtube' in x and isinstance(x['youtube'], list) and len(x['youtube']) > 0 else None)

youtube_subs = YoutubeSubs(api_key)
df_total['subscriptores'] = df_total['youtube_url'].apply(youtube_subs.get_subscribers)
fin = time.time()

# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")

inicio = time.time()
df_total['wiki_url'] = df_total['links'].apply(lambda x: x['wiki'][0]['url'] if x and 'wiki' in x and isinstance(x['wiki'], list) and len(x['wiki']) > 0 else None)

wiki = Wiki()
df_total['premios'] = df_total['wiki_url'].apply(wiki.count_won_awards_with_wiki)
fin = time.time()

# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
print("\nCONJUNTO DE DATOS FINAL")
print(df_total)
df_total.to_csv('df_total.csv', index=False)

# IMPORTANTE: una vez ejecutado el código hasta aquí, comentarlo y
# comenzar trabajando con "df_final" a partir la siguiente instrucción:
df_final = pd.read_csv('df_final.csv')


print("\nEXPLORACIÓN DE LOS DATOS")

# Crear una instancia de la clase Exploracion y explorar el DataFrame
explorador = Exploracion(df_final)
explorador.visualizar_columnas()
explorador.resumen()
explorador.mostrar_muestra()
