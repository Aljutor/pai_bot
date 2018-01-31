CMD_LIST = {
    "priority" : ["calc", "search", "question", "tell", "action", "know", "hello", "joke"],
    "commands" : {
        "action" : ["do", "сделай"],
        "question" : ["?",
                      "how", "как",
                      "where", "где",
                      "who", "кто",
                      "when", "когда",
                      "will", "be", "будет"],
        "calc" : ["calc", "посчитай",
                  "much", "сколько",
                  "solve", "реши"],
        "tell" : ["tell", "скажи"],
        "joke" : ["joke", "шутка", "пошути"],
        "hello" : ["hello", "привет",
                   "hi", "прив"],
        "know" : ["wiki", "вики",
                  "wikipedia", "википедия"],
        "search" : ["find", "найди",
                    "search", "ищи", "искать"]
    },
    "command_service": {
        "action" : "action",
        "question" : "search",
        "calc" : "wolframalpha",
        "tell" : "search",
        "joke" : "jokes",
        "hello" : "hello",
        "know" : "wikipedia",
        "search" : "duckduckgo"
    },
    "helpers" : ["is", "are"]
}