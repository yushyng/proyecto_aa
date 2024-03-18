import pandas as pd
import requests

class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.get_access_token()

    def get_access_token(self):
        token_url = 'https://accounts.spotify.com/api/token'
        token_params = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        token_response = requests.post(token_url, data=token_params)
        token_data = token_response.json()
        if 'access_token' in token_data:
            return token_data['access_token']
        else:
            print('Error al obtener el token de acceso')
            return None

    def get_artist_ids(self, artist_names):
        search_url = 'https://api.spotify.com/v1/search'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }
        artist_ids = {}
        for artist_name in artist_names:
            search_params = {
                'q': artist_name,
                'type': 'artist',
            }
            search_response = requests.get(search_url, params=search_params, headers=headers)
            search_data = search_response.json()
            if 'artists' in search_data and 'items' in search_data['artists']:
                for artist in search_data['artists']['items']:
                    if 'name' in artist and artist['name'] == artist_name:
                        artist_ids[artist_name] = artist['id']
                        break
                else:
                    print(f"No se encontraron resultados para {artist_name} en 2022")
            else:
                print(f'No se encontró al artista {artist_name}')
        return artist_ids

    def get_followers_counts(self, artist_ids):
        artists_url = 'https://api.spotify.com/v1/artists'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }
        followers_counts = {}
        for artist_name, artist_id in artist_ids.items():
            artist_url = f'{artists_url}/{artist_id}'
            artist_response = requests.get(artist_url, headers=headers)
            artist_data = artist_response.json()
            if 'followers' in artist_data:
                followers_count = artist_data['followers']['total']
                followers_counts[artist_name] = followers_count
            else:
                followers_counts[artist_name] = None
        return followers_counts

'''# Ejemplo de uso:
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Crear una instancia de la clase Spotify
spotify_client = Spotify(client_id, client_secret)

# Lista de nombres de artistas
artist_names = ['artist_name_1', 'artist_name_2', 'artist_name_3']  # Inserta los nombres de los artistas aquí

# Obtener los IDs de los artistas
artist_ids = spotify_client.get_artist_ids(artist_names)

# Obtener el número de seguidores de cada artista
followers_counts = spotify_client.get_followers_counts(artist_ids)

# Crear un DataFrame con los IDs de los artistas y el número de seguidores
df_artist_followers = pd.DataFrame({'Artist': list(followers_counts.keys()), 'Followers': list(followers_counts.values())})

# Mostrar el DataFrame resultante
print(df_artist_followers)'''
