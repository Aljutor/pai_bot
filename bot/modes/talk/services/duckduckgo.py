# duckduckgo

import requests

API_URL = "https://api.duckduckgo.com/?format=json&pretty=0&no_redirect=1&no_html=1&skip_disambig=1&q={}"

def query(query):
    url = API_URL.format(query)
    try:
        response = requests.get(url)
        json = response.json()
        answer = json["Abstract"]
    except: answer = "connection error"
    return "DuckDuckGo: " + answer if answer else ""
