import requests

from mapper.base import BaseExtractor


class HTTPExtractor(BaseExtractor):

    def __init__(self, url):
        self.url = url

    def extract(self):
        response = requests.get(self.url)
        return response.text
