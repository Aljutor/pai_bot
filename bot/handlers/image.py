import os
import io
import uuid
import logging

import requests

from telegram.ext import MessageHandler, Filters


logger = logging.getLogger(__name__)

def find_simular(image):
    return "Yeah"

def photo(bot, update):
    photo = update.message.photo[0]
    voice_file = bot.get_file(photo.file_id)

    with io.BytesIO() as file:
        voice_file.download(out=file)


        try:
            text = find_simular(file)

            bot.send_message(
                chat_id=update.message.chat_id,
                text='Image recognition: ' + text,
            )

        except Exception as e:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Photo recognition critical error',
            )

            logger.critical(e)

            return


Photo_handler = MessageHandler(Filters.photo, photo)

