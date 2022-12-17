import requests
import json
api_key = "6a4ba2a0"
# movie_id = '3896198'

def scraping_from_omdb_api(): # returns dict
    url = f"http://www.omdbapi.com/?i=tt{movie_id}&apikey={api_key}"
    response = requests.get(url)
    response_json=json.loads(response.text)
    print(response_json)
    return response_json
