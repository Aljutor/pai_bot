import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId

logger = logging.getLogger(__name__)

def talk(bot, update):
    logger.info("Math command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Talk

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Starting talk mode",
        reply_markup=reply_markup
    )

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Send your question",
        reply_markup=reply_markup
    )

Talk_handler = CommandHandler('talk', talk)