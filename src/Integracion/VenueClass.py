import pandas as pd
def venueClass(df):
    df_simple = df[['name', 'VenueName', 'VenueCity', 'VenueState']]
    df_simple = df_simple.reset_index(drop=True)

    listaSalas = ['sala', 'andén 56', 'moby dick club', 'razzmatazz',
                  'disfrutona', 'apolo', 'café berlín', 'escenario santander',
                  'gremi', 'sospechosa', 'auditorio la alameda', 'zentral',
                  'la chica de ayer', 'mamba', 'gran café', 'wolf', 'kafe antzokia',
                  'náutico', 'palacio de', 'antiguo mercado', 'playa club',
                  'bataplan', 'auditorio', 'recinto', 'fútbol', 'independance',
                  'atletismo', 'club', 'hotel', 'jamboree', 'marina norte', 'duquessa',
                  'can reon', 'urban', 'siroco', 'gas', 'guarida', 'volander', 'nau',
                  'jazz', 'heliogàbal', 'espacio', 'tizón', 'disco', 'pecera', 'noir', 'aliatar',
                 'marina', 'raqueta', 'ferial', 'espai' ]

    # teatros con más capacidad de 1000 y menos de 5000
    listaTeatros = ['teatro', 'auditorio starlite', 'sant jordi club', 'riviera',
                    'palau sant jordi', 'castillo', 'poble espanyol', 'damm',
                    'pabellón magdalena', 'enjoy! multiusos', 'golf', 'ifema', 'trips'
                    , 'palau', 'farga', 'marbella arena', 'brilla', 'alcazaba',
                    'coruña sounds', 'artillería', 'jardines', 'pandora', 'paral·lel',
                    'ushuaïa', 'hï ibiza', 'camping', 'carmen', 'fusteret', 'arena', 'bilbao', 'pabellón', 
                    'oasisss', 'stage', 'pisuerga', 'centro hípico', 'pal.', 'aretoa']

    listaEstadios = ['wizink center', 'palacio vistalegre', 'ventas',
                     'plaza de toros', 'coliseum', 'marenostrum',
                     'ciudad artes y ciencias', 'concert music festival',
                     'navarra arena', 'bizkaia arena', 'fundación unicaja']

    
    def asignar_clase(row):
        venueName = row['VenueName'].lower()
        if any(sala in venueName for sala in listaSalas):
            return 'SALA'
        elif any(teatro in venueName for teatro in listaTeatros):
            return 'TEATRO'
        elif any(estadio in venueName for estadio in listaEstadios):
            return 'ESTADIO S'
        elif 'estad' in venueName or 'iberdrola music' in venueName:
            return 'ESTADIO M'
        else:
            return None

    # Aplicar la función a cada fila de la columna 'VenueName'
    df_simple['VenueClass'] = df_simple.apply(asignar_clase, axis=1)
    df_merged = pd.merge(df_simple, df, on='name', how='inner')
    return df_merged

