from googleapiclient.discovery import build

class YoutubeSubs:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def get_channel_subscribers(self, channel_id):
        request = self.youtube.channels().list(part="statistics", id=channel_id)
        response = request.execute()

        # Verificar si la respuesta contiene elementos
        if "items" in response and response["items"]:
            return int(response["items"][0]["statistics"]["subscriberCount"])
        else:
            return None

    def get_subscribers(self, channel_url):
        if channel_url is not None:
            channel_id = channel_url.split("/")[-1]
            return self.get_channel_subscribers(channel_id)
        else:
            return None