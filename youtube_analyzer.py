import requests as re
import json
from statistic import Statistic


class YouTubeAnalyzer:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id

    def get_statistic(self) -> Statistic:

        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        response = re.get(url)
        data = json.loads(response.text)["items"][0]["statistics"]
        return Statistic(**data)