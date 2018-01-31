import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

from bot.user import StateId

logger = logging.getLogger(__name__)

def start(bot, update):
    logger.info("Start command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Start

    start_keyboard = [['/xo3'],
                       ['/xo5'],
                       ["/talk"],
                       ['/matches']]


    reply_markup = ReplyKeyboardMarkup (start_keyboard)

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Start bot message",
        reply_markup=reply_markup
    )

Start_handler = CommandHandler('start', start)