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

Para clonar el proyecto, también puedes usar el siguiente comando en la terminal.
```
git clone https://github.com/yushyng/proyecto_aa.git
```


El proyecto se desarrollará con PyCharm. Por ello, recomendamos tener descargado este entorno de desarrollo. Asegúrate de tener instalado un intérpetre de Python 3.9 o una versión superior.

Para descargar los datos de Google Drive ejecutar el scrpit dentro de la carpeta data habiendo descargado también el fichero de texto.

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
- Una clase main.py que orquesta todo el código, donde se importan las bibliotecas necesarias y se pone en funcionamiento el programa (carga, extracción, concatenación, limpieza...) llamando a los métodos implementados en el resto de clases.

- La fase de extracción está dividida en varios módulos, uno por cada fuente utilizada: Ticketmaster, LastFM, Spotify, Wiki, YoutubeSubs

  La 1ª fase de extracción es usar la API de Ticketmaster, que nos permite adquirir un conjunto de datos de los próximo eventos que se van a realizar en España.
  En Ticketmaster.py hacemos la extracción de cada banco de datos, en Carga.py los juntamos y limpiamos las filas duplicadas.
  
  En la 2º fase de extracción, complementamos con datos secundarios gracias a la variable _embedded, que nos proporciona links a las siguientes páginas:
  
  LastFm.py: en este módulo, usamos la librería requests de Python para extraer el número de oyentes mensuales de los artistas.
  
  Youtube.py: usando la API de googleapiclient extraemos el número de subscriptores de los artistas en Youtube.
  
  Wiki.py : utilizando la librería de Beautiful Soup, hacemos web-scrapping para extraer cuántos premios ha ganado cada artista.
  
  Spotify: con la librería requests, conseguimos extraer el número de seguidores en la plataforma de streaming de música de Spotify.

  Además, tenemos VenueClass.py, donde obtenemos una nueva variable "VenueClass" que indica el tipo de recinto donde se realiza el evento: sala, teatro, estadio S o estadio M, en función del tamaño del mismo.
  
- El archivo LimpiezaInicial: Al haber descargado los datos de la API de Ticketmaster, vemos que se han guardado en un formato con el que no podemos trabajar o hay varios eventos duplicados, por lo que arreglamos estos problemas (eliminamos las que tienen todas las variables iguales: nombres,fechas...) y, además, extraemos más variables que estan embedidas en la variable "_embedded".

Recuerda comentar breve pero detalladamente cada método que implementes para ayudar a los compañeros de trabajo a comprenderlo.
Y si tu trabajo requiere de la instalación de un nuevo paquete, recuerda añadirlo al requirements.txt escribiéndolo manualmente o usando la instrucción _pip freeze > requirements.txt_ en la terminal del programa.
