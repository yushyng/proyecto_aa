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
