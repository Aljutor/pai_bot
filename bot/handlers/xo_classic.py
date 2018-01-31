import logging
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId

logger = logging.getLogger(__name__)

def xo_classic(bot, update):
    logger.info("XO_classic command, id: " + str(update.message.chat_id))

    user_state = bot.state[update.message.chat_id]
    user_state.state_id = StateId.XO

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Switched to XO game mode",
        reply_markup=reply_markup
    )

    if (user_state.xo_game is None):
        user_state.xo_game = "XO GAME STATE MOCK"

        bot.send_message (
            chat_id=update.message.chat_id,
            text="New XO game started",
        )

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.xo_game,
    )

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Awaiting your move",
    )

XO_classic_handler = CommandHandler('xo', xo_classic)