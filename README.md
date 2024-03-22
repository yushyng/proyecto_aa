 # Proyecto de Datos I.
 
__Integrantes__: Julia Arauzo, Carlota Salazar y Yushan Yang. \
__Grupo__: 4 \
__Curso__: 2º GIDIA

## Sobre el proyecto
EventPeak es un portal de venta de entradas para los conciertos realizados en España. 

Para acordar unos precios de venta justos y competitivos, nos basaremos en un sistema de Aprendizaje Automático desarrollado por el equipo de EventPeak que logre predecir el rango de precios entre los que oscila cada concierto que se publique en nuestro portal. Al tratarse de un rango de precio, realizaremos dos modelos: uno que prediga el precio mínimo y otro que prediga el precio máximo.

El plan es implementar y entrenar este sistema con los datos actualmente publicados y probar su funcionamiento con los datos nuevos que sean publicados a medio o largo plazo.
Todos estos datos están extraídos, principalmente, con la API de Ticketmaster.

## Sobre la instalación
En primer lugar, clona el repositorio de este proyecto en tu dispositivo utilizando el comando _git clone_ y pegando a continuación la URL del repositorio especificada [aquí](https://github.com/yushyng/proyecto_aa.git).

El proyecto se desarrollará con PyCharm. Por ello, recomendamos tener descargado este entorno de desarrollo. Asegúrate de tener instalado un intérpetre de Python 3.9 o una versión superior.

Antes de comenzar a trabajar, realiza un _pull_ para bajarte la última versión del proyecto. Recomendamos también la realización de _commits_ periódicos para mantener a salvo cualquier cambio elaborado (no esperes a tener el código terminado para hacer _commit_). Y después de un _commit_, hacer un _push_ (existe la opción de hacer ambas cosas juntas en un solo paso).

## Sobre las fuentes de datos
[TicketMaster](https://www.ticketmaster.es/?utm_source=TM-google&utm_medium=cpc&utm_campaign=co:ES+%7C+an:Pure+Brand+%7C+obj:Sales+%7C+chl:Gb+%7C+cat:Branded+%7C+bud:TM+%7C+a:B1+%7C+tp:TMES+%7C+pn:+%7C+p:+%7C+ag:+%7C+fc:Manual+%7C+lc:ES&utm_content=paid&awtrc=true&utm_source=TM-google&camefrom=%7B%7Bcampaign.name%7D%7D&awtrc=true&gad_source=1&gclid=CjwKCAjwzN-vBhAkEiwAYiO7oNkvHFfNBeLpD6kto_Xb09hfWnR9rEUHBd3_2zWZUXSMJfMmf59B8BoCDlwQAvD_BwE&gclsrc=aw.ds) será la fuente principal de donde obtendremos todos los datos "base" para realizar el proyecto (nombre y tipo del evento, artista, fechas de realización, fechas de venta, precios fijados por TicketMaster, género y subgénero del concierto, promotor y detalles del lugar). 

Además, complementaremos esta información con otras fuentes de datos secundarias como son:
- [Spotify](https://open.spotify.com/intl-es): número de seguidores actuales
- [Last.FM](https://www.last.fm/es/): número de oyentes mensuales
- [Wikipedia](https://es.wikipedia.org/wiki/Wikipedia:Portada): número de premios ganados
- [Youtube](https://www.youtube.com/): número de subscriptores


## Sobre el código
El código está estructurado de la siguiente manera:
- Una clase main.py que orquesta todo el código, donde se llama a los métodos implementados en el resto de clases.
   En el main se se importan las bibliotecas necesarias y nos descargamos los datos recopilados hasta el momento de la Api de ticketmaster, es decir los últimos eventos.
   Tras descargar los datos, concatenamos todos los dataframe en uno solo y hacemos una limpieza llamando a los métodos de la clase LimpiezaInicial ya que, al haber descargado los 
   datos se han guardado en un formato con el que no podemos trabajar o hay varios eventos duplicados (todas las variables iguales:nombres,fechas...).
   Posteriormente creamos las clases necesarias como por ejemplo Spotify,Youtube para complementar nuestros datos con datos secundarios (los mencionados anteriormente).
- La fase de extracción está dividida en varios módulos, uno por cada fuente utilizada: LastFM, Spotify, Wiki, YoutubeSubs
  La 1ª fase de extraccion es usar la Api de Ticketmaster que nos permite adquirir un conjunto de datos de los próximo eventos que se van a realizar en España.
  En la 2º fase de estracción complementamos con datos secundarios gracias a la varable _embedded,que nos proporciona links a las siguientes páginas:
  
  Last.Fm.py: en este módulo, usamos la librería requests de Python que permite enviar solicitudes HTTP fácilmente. De aquí conseguimos el número de oyentes mensuales de los artistas.
  
  Youtube.py: usando la Api de googleapiclient conseguimos el número de subscriptores de los artistas en youtube.
  
  Wiki.py : utilizando la librería de Beautiful Soup, hacemos web-scrapping para tener una variables que nos permita saber cuántos premios ha ganado cada artista.
  
  Spotify: con la librería requests conseguimos el número de seguidores en la plataforma de streaming de música de Spotify.
  
- El archivo LimpiezaInicial:
  Tenemos varios métodos:
  Método corregir_json: Reemplaza comillas simples por comillas dobles y convierte las palabras 'True' y 'False' en minúsculas. Luego, carga el string corregido como un objeto JSON.
  Método corregir_columnas: Aplica la función corregir_json() a las columnas especificadas del DataFrame df que contienen datos en formato JSON.
  Con estado dos funciones podemos obtener variables como obtener_start_datetime, obtener_end_datetime, obtener_min_price, etc., 
  Método arreglo_embeded: Similar a corregir_json, pero específicamente para la columna _embedded.
  Métodos para obtener información específica sobre eventos: Estos métodos, como genre_event, subgenre_event, etc., extraen información específica sobre eventos dentro de la variable     _embedded.
Recuerda comentar breve pero detalladamente cada método que implementes para ayudar a los compañeros de trabajo a comprenderlo.
Y si tu trabajo requiere de la instalación de un nuevo paquete, recuerda añadirlo al requirements.txt escribiéndolo manualmente o usando la instrucción _pip freeze > requirements.txt_
_En curso..._

## Lo último en el repositorio... (09/03/2024)
Organización del repositorio con la nueva carpeta "Proyecto". \
Esta carpeta contiene una subcarpeta para los csvs de antes y después del preprocesado, y las subcarpetas correspondientes a cada entrega.
Los elementos de cada entrega son, de manera general:
 - Enunciado del problema en PDF
 - Memoria en WORD
 - Presentación en PDF
 - Código pertinente en IPYNB
 - Archivo resultante del código en CSV o PARQUET
 - Resumen de la entrega y planes de mejoras en TXT
 - Subcarpeta de "reentrega" donde solventamos los puntos tratados en el TXT
