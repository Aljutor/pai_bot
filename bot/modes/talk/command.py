# command

import importlib

from bot.modes.talk.cmd_list import CMD_LIST as data

COMMANDS = data["commands"]
HELPERS  = data["helpers"]
PRIORITY = data["priority"]
SERVICES = data["command_service"]

def prepare(query):
    return query.strip().lower()
    
def parse_commands(text):
    text = " " + text + " "
    commands = set()
    for command, words in COMMANDS.items():
        for word in words:
            if text.find(" " + word + " ") >= 0:
                commands.add(command)
    return commands
    
def clear_commands(text):
    text = " " + text + " "
    for command, words in COMMANDS.items():
        for word in words:
            if text.find(" " + word + " ") >= 0:
                text = text.replace(" " + word + " ", " ")
    return text.strip()
    
def top_command(commands):
    for command in PRIORITY:
        if command in commands:
            return command
    return ""
    
def get_service(command_name):
    for command, service in SERVICES.items():
        if command == command_name:
            return service
    return "default"
    
def service_query(command, query):
    service_name = get_service(command)
    service = importlib.import_module('.' + str(service_name), 'bot.modes.talk.services')
    return service.query(query)

def query(query):
    query = prepare(query)
    if(query != ""):
        commands = parse_commands(query)
        top = top_command(commands)
        value = clear_commands(query)
        return service_query(top, value)
    else: return ""
