import requests
import re

class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.obtener_access_token()

    def obtener_access_token(self):
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

    def obtener_id_artista(self, url_spotify):
        pattern = r'/artist/(\w+)'
        match = re.search(pattern, url_spotify)
        if match:
            return match.group(1)
        else:
            return None

    def obtener_seguidores_por_fila(self, url_spotify):
        artist_id = self.obtener_id_artista(url_spotify)
        if artist_id:
            artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(artist_url, headers=headers)
            if response.status_code == 200:
                artist_data = response.json()
                seguidores = artist_data['followers']['total']
                return seguidores
        else:
            return None
    def obtener_popularidad_por_fila(self, url_spotify):
        artist_id = self.obtener_id_artista(url_spotify)
        if artist_id:
            artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(artist_url, headers=headers)
            if response.status_code == 200:
                artist_data = response.json()
                seguidores = artist_data['popularity']
                return seguidores
            else:
                return None
        else:
            return None
    def obtener_generosArtistas_por_fila(self, url_spotify):
        artist_id = self.obtener_id_artista(url_spotify)
        if artist_id:
            artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(artist_url, headers=headers)
            if response.status_code == 200:
                artist_data = response.json()
                seguidores = artist_data['genres']
                return seguidores
            else:
                return None
        else:
            return None
