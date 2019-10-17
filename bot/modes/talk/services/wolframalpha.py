# wolfram alpha
import os
import requests
from bs4 import BeautifulSoup

api_url = 'http://api.wolframalpha.com/v2/query?input={}&appid={}'
api_token = token = os.environ['WA_TOKEN']

def ask(query):
    resp = requests.get(api_url.format(query, api_token))

    if resp.status_code != 200:
        answer = "http error"
    else:

        dom = BeautifulSoup(resp.text, "lxml")
        result = dom.queryresult.findAll("pod", id="Solution")

        if not result:
            result = dom.queryresult.findAll("pod", id="Result")

        if not result:
            result = dom.queryresult.findAll("pod", id="Root")

        if not result:
            result = dom.queryresult.findAll("pod", title="Derivative")

        if not result:
            result = dom.queryresult.findAll ("pod", title="Definite integral")

        if not result:
            result = dom.queryresult.findAll ("pod", title="Indefinite integral")

        if result:
            subpods = result[0].findAll("subpod")
            answers = list(pod.plaintext.string for pod in subpods)
            answer = "; ".join(answers) + "."
        else:
            answer = None # "nothing found"
    return "WolframAlpha: " + answer if answer else ""
    
def query(query):
    return ask(query)
