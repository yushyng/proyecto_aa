import requests
from bs4 import BeautifulSoup
class LastFm:
    def __init__(self, api_key):
        self.api_key = api_key

    def parse_abbr_to_int(self, abbr):
        """LastFm devuelve el número de seguidores como una abreviatura de números en
        formato 'K' (miles) o 'M' (millones) y con este método hacemos la conversirón
        a números enteros."""
        if 'K' in abbr:
            return int(float(abbr.replace('K', '')) * 1000)
        elif 'M' in abbr:
            return int(float(abbr.replace('M', '')) * 1000000)
        else:
            return int(abbr)

    def obtener_seguidores_lastfm(self, url):
        """Obtiene el número de seguidores de una cuenta de Last.fm dada su URL"""
        """Cuando la solicitud "get" es exitosa, analiza el contenido HTML utilizando 
        BeautifulSoup para encontrar la etiqueta <abbr> que contiene el número de seguidores."""
        if url is None:
            print("URL no proporcionada. No se pueden obtener seguidores.")
            return None

        print("Obteniendo seguidores para la URL:", url)  # Agregar impresión de diagnóstico

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            listeners_tag = soup.find('abbr', class_='intabbr js-abbreviated-counter')
            if listeners_tag:
                listeners_text = listeners_tag.text.strip()
                listeners = self.parse_abbr_to_int(listeners_text)
                return listeners
            else:
                print("No se pudo encontrar el número de oyentes en la página.")
                return None
        else:
            print("No se pudo acceder a la página:", response.status_code)
            return None
