import os
import io
import uuid
import logging
import cv2
import requests
import numpy as np
from telegram.ext import MessageHandler, Filters

from bot.modes.image import gen_model, predict

logger = logging.getLogger(__name__)

clf = gen_model()

def find_simular(file):
    data = np.frombuffer(file.getvalue(), dtype=np.uint8)
    color_image_flag = 1
    bgrImg = cv2.imdecode(data, color_image_flag)
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    result = predict(rgbImg, clf)

    text = ""
    for name, prob in result:
        text += "* {}: Prob {}\n".format(name, round(prob, 3))

    return text

def photo(bot, update):
    photo = update.message.photo[0]
    voice_file = bot.get_file(photo.file_id)

    with io.BytesIO() as file:
        voice_file.download(out=file)


        try:
            text = find_simular(file)

            bot.send_message(
                chat_id=update.message.chat_id,
                text='Image recognition:\n' + text,
                parse_mode="MARKDOWN"
            )

        except Exception as e:
            bot.send_message(
                chat_id=update.message.chat_id,
                text='Photo recognition critical error',
            )

            logger.critical(e)

            return


Photo_handler = MessageHandler(Filters.photo, photo)

