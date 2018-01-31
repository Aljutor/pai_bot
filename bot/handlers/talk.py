import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId

logger = logging.getLogger(__name__)

def talk(bot, update):
    logger.info("Talk command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Talk

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Starting talk mode",
        reply_markup=reply_markup
    )

    text = "Send your question, examples: \n" \
           "calc integral 10/x   \n" \
           "calc derivative 10/x \n" \
           "solve 2 * x = 4 \n" \
           "search pizza \n"

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        reply_markup=reply_markup
    )

Talk_handler = CommandHandler('talk', talk)