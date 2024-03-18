import requests
import pandas as pd

class LastFm:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_artist_listeners(self, artist_names, date):
        artist_list = []
        listeners_list = []
        for artist_name in artist_names:
            url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={self.api_key}&format=json"
            response = requests.get(url)
            data = response.json()
            if "artist" in data and "stats" in data["artist"]:
                listeners = data["artist"]["stats"]["listeners"]
                artist_list.append(artist_name)
                listeners_list.append(listeners)
            else:
                print(f"No se encontró información para {artist_name}.")
        df = pd.DataFrame({"Artist": artist_list, "Listeners": listeners_list})
        return df

'''# Ejemplo de uso:
LASTFM_API_KEY = "your_lastfm_api_key"
ARTIST_NAMES = ['artist_name_1', 'artist_name_2', 'artist_name_3']  # Inserta los nombres de los artistas aquí
DATE = "03-03-2024"  # Ajusta según sea necesario

# Crear una instancia de la clase LastFm
lastfm_client = LastFm(LASTFM_API_KEY)

# Obtener el número de oyentes de cada artista en una fecha específica
df_artist_listeners = lastfm_client.get_artist_listeners(ARTIST_NAMES, DATE)

# Mostrar el DataFrame resultante
print(df_artist_listeners)'''
