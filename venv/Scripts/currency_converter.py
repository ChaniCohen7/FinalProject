# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen

url = "https://api.exchangerate-api.com/v4/latest/USD"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response

print(data_json["rates"][data_json["base"]])

def convert_to_usd(num,kind):
    return float(num/float(data_json["rates"][kind]))
def convert_from_usd(num,kind):
    return float(num*float(data_json["rates"][kind]))
print(convert_from_usd(23,"AED"))

