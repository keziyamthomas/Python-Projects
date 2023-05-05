import requests

def get_json(url):
    result = requests.get(url)
    return result.json()