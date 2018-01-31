import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId

logger = logging.getLogger(__name__)

def math(bot, update):
    logger.info("Math command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Math

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Starting Math mode",
        reply_markup=reply_markup
    )

Math_handler = CommandHandler('math', math)