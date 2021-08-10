
from urllib.request import urlopen
import json

class server():
    def __init__(self):
        self.url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.response = urlopen(self.url)
        self.data_json = json.loads(self.response.read())