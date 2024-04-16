class LimpiezaFinal:
  def __init__(self):
    self.df_total = None

  def aplicar_limpieza(self, df):
    # Aplicar la función a toda la columna 'GéneroArtista'
    df['GéneroArtista'] = df['GéneroArtista'].apply(self.convertir_string_a_lista)
    df['NumGeneros'] = df['GéneroArtista'].apply(lambda x: len(x))
    
     # Mostrar los primeros registros para verificar
    print(df.head())

    df.reset_index(drop=True)
    #las urls ya no nos siven ya que no podemos sacar mas informacion de ellos
    #Eliminamos las columnas de GeneroArtista porque adquiere el valor de lista y no podemos trabajar en ese formato 
    #y tampoco podemos cambiarlo (ya lo hemos probado), pero supliremos esta parte más adelante.
    columnas_a_eliminar = ['lastfm_url', 'youtube_url', 'spotify_url', 'salaCiudad', 'wiki_url', 'links','GéneroArtista']
    df2 = df.drop(columns=columnas_a_eliminar)
    columnas_a_convertir = ['seguidores', 'popularidad', 'seguidoresLast', 'subscriptores', 'premios']
    
    # Rellena los valores faltantes (NaN) con 0
    df2[columnas_a_convertir] = df2[columnas_a_convertir].fillna(0)

    # Convierte las columnas a enteros
    df2[columnas_a_convertir] = df2[columnas_a_convertir].astype(int)
    df2 = df2.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df2.duplicated().sum()
    #eliminamos las filas duplicadas
    df2 = df2.drop_duplicates()
    df2.reset_index(drop=True)
    
    return df2



