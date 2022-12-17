import requests
import json
api_key = "6a4ba2a0"

def scraping_from_omdb_api(): # returns dict
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey={api_key}"
    response = requests.get(url)
    response_json=json.loads(response.text)
    print(response_json)
    return response_json
