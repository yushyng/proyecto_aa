import requests
from bs4 import BeautifulSoup
class LastFm:
    def __init__(self, api_key):
        self.api_key = api_key

    def parse_abbr_to_int(self, abbr):
        if 'K' in abbr:
            return int(float(abbr.replace('K', '')) * 1000)
        elif 'M' in abbr:
            return int(float(abbr.replace('M', '')) * 1000000)
        else:
            return int(abbr)

    def obtener_seguidores_lastfm(self, url):
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
