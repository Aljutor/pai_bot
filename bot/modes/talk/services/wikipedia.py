# wikipedia

import re
import requests

API_URL = 'https://{}.wikipedia.org/w/api.php?action=opensearch&format=json&namespace=0&limit=1&search={}'

def lang(query):
    lang = 'en'
    if re.match(r'\w', query):
        lang = 'ru'
    return lang

def query(query):
    url = API_URL.format(lang(query), query)
    response = requests.get(url)
    json = response.json()
    if not json[1]:
        return ""
    answer = json[1][0] + ": " + json[3][0]
    print(answer)
    return answer
