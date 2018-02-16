import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId


logger = logging.getLogger(__name__)

def translate(bot, update):
    logger.info("Translate command, id: " + str(update.message.chat_id))

    user_state = bot.state[update.message.chat_id]
    user_state.state_id = StateId.Translate

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Switched to translate mode ENG -> RUS",
        reply_markup=reply_markup
    )

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Awaiting your English phrase to Translate",
    )

Translate_handler = CommandHandler('translate', translate)
