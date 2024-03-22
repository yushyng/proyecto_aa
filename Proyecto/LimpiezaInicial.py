import json


class LimpiezaInicial:
    def __init__(self):
        self.df_total = None

    def limpiar_strings(self, df_total, strings_filtrar):
        """Filtra las filas del DataFrame df_total en las cuales la columna 'name' no
        contiene ninguna de las cadenas especificadas en la lista strings_filtrar."""
        # Filtrar
        for string in strings_filtrar:
            df_total = df_total[~df_total['name'].str.lower().str.contains(string)]
        return df_total

    def corregir_json(self, json_str):
        """Reemplaza comillas simples por comillas dobles y convirte las palabras 'True'
        y 'False' en minúsculas. Luego, carga el string corregido como un objeto JSON."""
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
        """Aplica la función corregir_json() a las columnas especificadas del
        DataFrame df que contienen datos en formato JSON."""
        for columna in columnas:
            df[columna] = df[columna].apply(self.corregir_json)
        return df

        # Nuevos métodos para obtener información específica

    def obtener_start_datetime(self, fila):
        """Devuelve la fecha y hora de inicio de un evento"""
        if 'access' in fila['dates'] and 'startDateTime' in fila['dates']['access']:
            return fila['dates']['access']['startDateTime']
        else:
            return None

    def obtener_end_datetime(self, fila):
        """Devuelve la fecha y hora final del evento"""
        return fila['sales']['public'].get('endDateTime')

    def obtener_min_price(self, fila):
        """Devuelve el precio mínimo del evento"""
        if 'priceRanges' in fila and isinstance(fila['priceRanges'], list) and fila['priceRanges']:
            for price_range in fila['priceRanges']:
                if price_range.get('type') == 'standard':
                    return price_range['min']
            return None

    def obtener_max_price(self, fila):
        """Devuelve el precio máximo del evento"""
        if 'priceRanges' in fila and isinstance(fila['priceRanges'], list) and fila['priceRanges']:
            for price_range in fila['priceRanges']:
                if price_range.get('type') == 'standard':
                    return price_range['max']
            return None

    def obtener_promotor(self, fila):
        """Devuelve el promotor del evento"""
        if 'promoter' in fila and isinstance(fila['promoter'], dict):
            return fila['promoter'].get('name')
        else:
            return None

    def obtener_genero(self, fila):
        """Devuelve el género del evento"""
        if isinstance(fila['classifications'], list) and fila['classifications']:
            for item in fila['classifications']:
                if 'genre' in item and isinstance(item['genre'], dict):
                    return item['genre'].get('name')
            return None

    def obtener_subgenero(self, fila):
        """Devuelve el subgénero del evento"""
        if isinstance(fila['classifications'], list) and fila['classifications']:
            for item in fila['classifications']:
                if 'subGenre' in item and isinstance(item['subGenre'], dict):
                    return item['subGenre'].get('name')
            return None

    def arreglo_embeded(df):
        """Hace lo mismo que corregir_json() pero específicamente para la columna _embedded
         porque tenía mucha información y no cogía los cambios indicados en ese otro método"""
        em = df['_embedded']
        col = em.str.replace("'", '"')
        col = col.str.replace("True", 'true')
        col = col.str.replace("False", 'false')
        df['_embedded'] = col
        return df

    def load_json(self, json_str):
        """Intenta cargar un string JSON en un objeto JSON."""
        try:
            json_object = json.loads(json_str)
            return json_object
        except json.JSONDecodeError as e:
            return None

    def genre_event(self, fila):
        """Devuelve el genre del evento"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['genre']['name']
        else:
            return None

    def subgenre_event(self, fila):
        """Devuelve el subgenre del evento"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['subGenre']['name']
        else:
            return None

    def type_event(self, fila):
        """Devuelve el type del evento"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['type']['name']
        else:
            return None

    def subtype_event(self, fila):
        """Devuelve el subtype del evento"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['classifications'][0]['subType']['name']
        else:
            return None

    def name(self, fila):
        """Devuelve el nombre del artista"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json'] and fila['columna_json']['attractions']:
            return fila['columna_json']['attractions'][0]['name']
        else:
            return None

    def venue_name(self, fila):
        """Devuelve el lugar del evento"""
        return fila['columna_json']['venues'][0]['name']

    def venue_city(self, fila):
        """Devuelve la ciudad del evento"""
        return fila['columna_json']['venues'][0]['city']['name']

    def venue_state(self, fila):
        """Devuelve el estado o comunidad autónoma del evento"""
        return fila['columna_json']['venues'][0]['state']['name']

    def venue_country(self, fila):
        """Devuelve el país del evento --> siempre es España"""
        return fila['columna_json']['venues'][0]['country']['name']

    def links(self, fila):
        """Devuelve los links asociados al artista"""
        if 'columna_json' in fila and 'attractions' in fila['columna_json']:
            attractions = fila['columna_json']['attractions']
            if attractions and 'externalLinks' in attractions[0]:
                return attractions[0]['externalLinks']
        return None

    def num_links(self, fila):
        """Devuelve el número de links que están asociados al artista"""
        if fila['links'] == None:
            return 0
        else:
            return len(fila['links'].keys())

