
from urllib.request import urlopen
import json

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = urlopen(url)
data_json = json.loads(response.read())