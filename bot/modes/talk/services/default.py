# default

import re

import bot.modes.talk.services.search as search
import bot.modes.talk.services.wolframalpha as wa

NUMERIC_EXPRESSION = '(\(|\))*(\d|\w)*[!=+\-*\/^()](\d|\w)*(\(|\))*'

def query(query):
    if re.findall(NUMERIC_EXPRESSION, query): # if starts is equation
        answer = wa.query(query)
    else: answer = search.query(query)
    return "..." if not answer else answer
