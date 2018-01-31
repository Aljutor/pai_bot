# search

from bot.modes.talk.services import duckduckgo

def search(query):
    return duckduckgo.query(query)

def query(query):
    return search(query)
