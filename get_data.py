# get_data.py
import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

#----- part 1 --------

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"

response = requests.get(request_url)
response_data = json.loads(response.text)

print(response_data['department'],":",response_data['name'],",$",response_data['price'])

#------- part 2 -------

request2_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

response = requests.get(request_url)
response_data = json.loads(response.text)

for x in response_data2:
        print(x["id"], x["name"]

# ---------
