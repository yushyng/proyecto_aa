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

El proyecto se desarrollará con PyCharm. Por ello, recomendamos tener descargado este entorno de desarrollo. Asegúrate tener instalado un intérpetre de Python 3.9 o una versión superior.

Antes de comenzar a trabajar, realiza un _pull_ para bajarte la última versión del proyecto. Recomendamos también la realización de _commits_ periódicos para mantener a salvo cualquier cambio elaborado (no esperes a tener el código terminado para hacer _commit_). Y después de un _commit_, hacer un _push_ (existe la opción de hacer ambas cosas juntas en un solo paso).

## Sobre las fuentes de datos
[TicketMaster](https://www.ticketmaster.es/?utm_source=TM-google&utm_medium=cpc&utm_campaign=co:ES+%7C+an:Pure+Brand+%7C+obj:Sales+%7C+chl:Gb+%7C+cat:Branded+%7C+bud:TM+%7C+a:B1+%7C+tp:TMES+%7C+pn:+%7C+p:+%7C+ag:+%7C+fc:Manual+%7C+lc:ES&utm_content=paid&awtrc=true&utm_source=TM-google&camefrom=%7B%7Bcampaign.name%7D%7D&awtrc=true&gad_source=1&gclid=CjwKCAjwzN-vBhAkEiwAYiO7oNkvHFfNBeLpD6kto_Xb09hfWnR9rEUHBd3_2zWZUXSMJfMmf59B8BoCDlwQAvD_BwE&gclsrc=aw.ds) será la fuente principal de donde obtendremos todos los datos "base" para realizar el proyecto (nombre y tipo del evento, artista, fechas de realización, fechas de venta, precios fijados por TicketMaster, género y subgénero del concierto, promotor y detalles del lugar). 

Además, complementaremos esta información con otras fuentes de datos secundarias como son:
- [Spotify](https://open.spotify.com/intl-es): número de oyentes mensuales actuales
- [Last.FM](https://www.last.fm/es/): número de oyentes mensuales

Se probó con la extracción de información de Google Trends, pero sin éxito. Por ello, lo próximo será probar con nuevas fuentes de datos secundarias como Instagram para obtener el número de seguidores (esto dará una idea sobre la popularidad del artista).

## Sobre el código
_Próximamente..._

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
