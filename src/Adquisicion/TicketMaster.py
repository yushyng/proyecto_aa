import requests
import pandas as pd
#Funcion que hemos usado para extraer la información de la API de Ticketmaster
def TicketMasterAdquisicion():
    pag = 0
    url = ('https://app.ticketmaster.com/discovery/v2/events?apikey=4uZ7cKblFpFckdrfHMGrT2coHBKCiAjs&countryCode=ES'
           '&classificationName=music&locale=*&page=') + str(
        pag)
    r = requests.get(url)

    if r.status_code == 200:
        respuesta = r.json()
        total_pages = respuesta['page']['totalPages']
        print(total_pages)
        df_datos = pd.DataFrame(respuesta['_embedded']['events'])
        pag += 1
        while pag < total_pages:
            url = ('https://app.ticketmaster.com/discovery/v2/events?apikey=4uZ7cKblFpFckdrfHMGrT2coHBKCiAjs'
                   '&countryCode=ES&classificationName=music&locale=*&page=') + str(
                pag)
            r = requests.get(url)
            res = r.json()
            df_datos_mas = pd.DataFrame(res['_embedded']['events'])
            df_datos = pd.concat([df_datos, df_datos_mas], ignore_index=True)
            pag += 1
    else:
        print('Error: ' + r.status_code)
        print(r.text)

    print(len(df_datos))
    return df_datos



