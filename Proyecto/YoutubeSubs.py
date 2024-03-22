from googleapiclient.discovery import build

class YoutubeSubs:
    def __init__(self, api_key):
        """Toma un api_key como parámetro, que se utiliza para inicializar la conexión a la API de YouTube."""
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def get_channel_subscribers(self, channel_id):
        """Recibe un ID como parámetro y lo utiliza para hacer una solicitud a la API de YouTube
         para obtener estadísticas del canal (el número de suscriptores)."""
        request = self.youtube.channels().list(part="statistics", id=channel_id)
        response = request.execute()

        # Verificar si la respuesta contiene elementos
        if "items" in response and response["items"]:
            return int(response["items"][0]["statistics"]["subscriberCount"])
        else:
            return None

    def get_subscribers(self, channel_url):
        """Recibe la URL completa del canal de Youtube como parámetro y la utiliza para extraer
        el ID del canal y llamar a get_channel_subscribers() para obtener el número de suscriptores del canal."""
        if channel_url is not None:
            channel_id = channel_url.split("/")[-1]
            return self.get_channel_subscribers(channel_id)
        else:
            return None