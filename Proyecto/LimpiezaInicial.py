import json


class LimpiezaInicial:
    def __init__(self):
        self.df_total = None

    def limpiar_strings(self, df_total, strings_filtrar):
        # Filtrar
        for string in strings_filtrar:
            df_total = df_total[~df_total['name'].str.lower().str.contains(string)]
        return df_total

    def corregir_json(self, json_str):
        # Convertir a cadena de texto si no es una cadena
        if isinstance(json_str, str):
            # Reemplazar comillas simples por comillas dobles
            corregida = json_str.replace("'", '"')
            # Reemplazar "True" por "true" y "False" por "false"
            corregida = corregida.replace("True", "true")
            corregida = corregida.replace("False", "false")
            return json.loads(corregida)
        else:
            return json_str

    def corregir_columnas(self, df, columnas):
        for columna in columnas:
            df[columna] = df[columna].apply(self.corregir_json)
        return df

        # Nuevos métodos para obtener información específica

    def obtener_start_datetime(self, fila):
        if 'access' in fila['dates'] and 'startDateTime' in fila['dates']['access']:
            return fila['dates']['access']['startDateTime']
        else:
            return None

    def obtener_end_datetime(self, fila):
        return fila['sales']['public'].get('endDateTime')

    def obtener_min_price(self, fila):
        if 'priceRanges' in fila and isinstance(fila['priceRanges'], list) and fila['priceRanges']:
            for price_range in fila['priceRanges']:
                if price_range.get('type') == 'standard':
                    return price_range['min']
            return None

    def obtener_max_price(self, fila):
        if 'priceRanges' in fila and isinstance(fila['priceRanges'], list) and fila['priceRanges']:
            for price_range in fila['priceRanges']:
                if price_range.get('type') == 'standard':
                    return price_range['max']
            return None

    def obtener_promotor(self, fila):
        if 'promoter' in fila and isinstance(fila['promoter'], dict):
            return fila['promoter'].get('name')
        else:
            return None

    def obtener_genero(self, fila):
        if isinstance(fila['classifications'], list) and fila['classifications']:
            for item in fila['classifications']:
                if 'genre' in item and isinstance(item['genre'], dict):
                    return item['genre'].get('name')
            return None

    def obtener_subgenero(self, fila):
        if isinstance(fila['classifications'], list) and fila['classifications']:
            for item in fila['classifications']:
                if 'subGenre' in item and isinstance(item['subGenre'], dict):
                    return item['subGenre'].get('name')
            return None

    def arreglo_embeded(df):
        em = df['_embedded']
        col = em.str.replace("'", '"')
        col = col.str.replace("True", 'true')
        col = col.str.replace("False", 'false')
        df['_embedded'] = col
        return df

    def load_json(self, json_str):
        try:
            json_object = json.loads(json_str)
            return json_object
        except json.JSONDecodeError as e:
            return None

    def genre_event(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['genre']['name']
        else:
            return None

    def subgenre_event(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['subGenre']['name']
        else:
            return None

    def type_event(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['type']['name']
        else:
            return None

    def subtype_event(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['subType']['name']
        else:
            return None

    def name(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['name']
        else:
            return None

    def venue_name(self, fila):
        return fila['columna_json']['venues'][0]['name']

    def venue_city(self, fila):
        return fila['columna_json']['venues'][0]['city']['name']

    def venue_state(self, fila):
        return fila['columna_json']['venues'][0]['state']['name']

    def venue_country(self, fila):
        return fila['columna_json']['venues'][0]['country']['name']

    def links(self, fila):
        if 'columna_json' in fila and 'attractions' in fila['columna_json']:
            attractions = fila['columna_json']['attractions']
            if attractions and 'externalLinks' in attractions[0]:
                return attractions[0]['externalLinks']
        return None

    def num_links(self, fila):
        if fila['links'] == None:
            return 0
        else:
            return len(fila['links'].keys())

