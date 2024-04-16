import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

class Wiki:
   # Función para obtener el número de premios desde la página de Wikipedia
    def obtener_numero_premios(url):
        try:
        # Obtener el contenido HTML de la página
         response = requests.get(url)
         if response.status_code == 200:
            # Analizar el HTML con BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar la sección que contiene la información de premios (puedes ajustar esto según la estructura de la página)
            premios_section = soup.find('span', {'id': 'Premios_y_reconocimientos'})
            if premios_section:
                # Extraer el texto de la sección de premios
                premios_text = premios_section.find_next('ul').get_text()
                # Utilizar expresiones regulares para encontrar el número de premios
                match = re.search(r'(\d+) premios', premios_text)
                if match:
                    return int(match.group(1))
         return None
        except Exception as e:
            print("Error al obtener número de premios:", e)
            return None
    


    def obtener_edad_desde_wikipedia(url_wikipedia):
    # Realizar la solicitud HTTP
        response = requests.get(url_wikipedia)

    # Comprobar si la solicitud fue exitosa
        if response.status_code == 200:
        # Analizar el HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar la sección que contiene la fecha de nacimiento
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                fecha_nacimiento_tag = infobox.find(text=re.compile(r'\b\d+\s+años\b'))
                if fecha_nacimiento_tag:
                # Obtener el texto que contiene el número de años
                    texto = fecha_nacimiento_tag.strip()

                # Extraer el número de años utilizando expresiones regulares
                    patron = r'\b(\d+)\s+años\b'
                    resultado = re.search(patron, texto)

                # Si se encuentra el número de años, calcular la edad
                    if resultado:
                        numero_anios = int(resultado.group(1))

                    # Obtener la fecha actual
                        fecha_actual = datetime.now()

                    # Calcular el año de nacimiento
                        ano_nacimiento = fecha_actual.year - numero_anios

                    # Devolver la edad
                        return fecha_actual.year - ano_nacimiento
                    else:
                     return None
                else:
                 return None
            else:
                return None
        else:
         return None
