import os
import io
import uuid
import logging

import requests

from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters

from bot.handlers.message import text as process_text

logger = logging.getLogger(__name__)

api_token  = os.environ['YA_TOKEN']

# this is unique identifier of user
# API assumes that APPLICATION makes requests and we can mark them

UUID = str(uuid.uuid4()).replace("-", "")

def ask_yandex(file, uid, lang="en-US"):
    # API doc
    # https://tech.yandex.ru/speechkit/cloud/doc/guide/concepts/asr-http-request-docpage/
    url = "https://asr.yandex.net/asr_xml?uuid={}&key={}&topic={}&lang={}&disableAntimat={}"
    url = url.format (uid, api_token, "queries", lang, "true")

    # just read raw information of the container
    data = file.getbuffer()

    headers = {'Content-Type': 'audio/ogg;codecs=opus', 'Content-Length': str (len (data))}

    # do post request of data
    resp = requests.post(url, data=data, headers=headers)

    # parse answers
    dom = BeautifulSoup(resp.text, "lxml")

    if (dom.html.body.recognitionresults['success'] == '0'):
        return []

    result = [var.string for var in dom.html.body.recognitionresults.findAll ("variant")]
    return result


def voice(bot, update):

    voice = update.message.voice
    voice_file  = bot.get_file(voice.file_id)

    with io.BytesIO() as file:
        voice_file.download(out=file)

        text = ''

        try:
            text = ask_yandex (file, UUID)
        except Exception as e:
            bot.send_message (
                chat_id=update.message.chat_id,
                text='Voice recognition critical error',
            )

            logger.critical(e)
        
            return

        if len(text) < 1:
            logger.info ("Voice command, id: " + str (update.message.chat_id) + " empty voice")

            bot.send_message (
                chat_id=update.message.chat_id,
                text='Voice recognition error',
            )

            return

        text = text[0]

        logger.info ("Voice command, id: " + str (update.message.chat_id) + " voice: " + text)

        bot.send_message (
            chat_id=update.message.chat_id,
            text='Voice recognition: ' + text,
        )

        update.message.text = text
        process_text(bot, update)


Voice_handler = MessageHandler(Filters.voice, voice)

