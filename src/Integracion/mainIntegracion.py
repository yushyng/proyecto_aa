import pandas as pd
from Spotify import Spotify
from Wiki import Wiki
from YoutubeSubs import YoutubeSubs
from Integracion import Integracion
from VenueClass import venueClass
from LastFm import LastFm
import time

# Lee el archivo CSV despúes de Carga
df_total = pd.read_csv('dfCarga.csv')

#Categorizamos el lugar del evento
df_processed = venueClass(df_total)

#Credenciales para la api de Spotify
client_id = 'de2c627e722341b784a8bb67d1dda88e'
client_secret = 'ccc8b038637c4326999eec8bf12b6f1c'
spotify = Spotify(client_id, client_secret)

#print(df_total['links'].isnull().sum())


# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'spotify_url'
df_total['spotify_url'] = df_total['links'].apply(lambda x: x['spotify'][0]['url'] if x and 'spotify' in x and isinstance(x['spotify'], list) and len(x['spotify']) > 0 else None)

df_total['spotify_url'] = df_total['spotify_url'].astype(str)

# Aplicar la función obtener_seguidores_por_fila a cada fila de la columna 'spotify_url'
df_total['seguidores'] = df_total['spotify_url'].apply(spotify.obtener_seguidores_por_fila)
print(df_total['seguidores'])

# Aplicar la función obtener_popularidad_por_fila de spotify
df_total['popularidad'] = df_total['spotify_url'].apply(spotify.obtener_popularidad_por_fila)
# Aplicar la función obtener_generosArtistas_por_fila de spotify
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
df_total['premios'] = df_total['wiki_url'].apply(wiki.obtener_numero_premios)
df_total['Edad'] = df_total['wiki_url'].apply(wiki.obtener_edad_desde_wikipedia)
fin = time.time()

# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
# Calcular la diferencia de tiempo
tiempo_transcurrido = fin - inicio

print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")

###################################################################################################

#Tras conseguir las variables de las RRSS vamos integrar nuevas variables
integracion = Integracion()
df_total = integracion.calcular_dias_venta(df_total)

df = integracion.calcular_dias_desde_finVenta(df_total)

df_total = integracion.calcular_peso_promotor(df_total)

df_total['tiene_twitter'] = df_total['links'].apply(integracion.tiene_twitter)

df_total['tiene_instagram'] = df_total['links'].apply(integracion.tiene_instagram)

df_total['tiene_itunes'] = df_total['links'].apply(integracion.tiene_itunes)

df_total['tiene_homepage'] = df_total['links'].apply(integracion.tiene_homepage)

df['NumGeneros'] = df['GéneroArtista'].apply(lambda x: len(x))

df_total['Generos_combinados'] = df_total.apply(integracion.combinar_y_limpiar_generos, axis=1)
 
#Funcion que nos da información sobre la exclusividad del concierto que proporciona ese artista en esa ciudad

df_total['conciertos_del_artista_en_ciudad'] = df_total.groupby(['nameArtist', 'VenueCity'])['name'].transform('count')


#Descarga del dataframe tras el proceso de carga
df_total.to_csv('dfIntegracion.csv', index=False)