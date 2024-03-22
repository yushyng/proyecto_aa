import requests
from bs4 import BeautifulSoup

class Wiki:
    @staticmethod
    def count_won_awards_with_wiki(url):
        """Función para contar los premios donde el resultado es 'Won', solo si hay una URL de Wikipedia disponible."""
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                cells = soup.find_all('td', class_='yes table-yes2 notheme')
                won_count = sum('Won' in cell.text for cell in cells)
                return won_count
        return None
