import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

from bot.user import StateId

logger = logging.getLogger(__name__)

def start(bot, update):
    logger.info("Start command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Start

    custom_keyboard = [['/xo'],
                       ["/math"],
                       ['/matches'],
                       ['/xo_5row']]

    reply_markup = ReplyKeyboardMarkup (custom_keyboard)

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Start bot message",
        reply_markup=reply_markup
    )

Start_handler = CommandHandler('start', start)