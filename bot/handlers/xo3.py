import logging
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId
from bot.modes.xo3 import TicTac3X3

logger = logging.getLogger(__name__)

def xo_3(bot, update):
    logger.info("XO_classic command, id: " + str(update.message.chat_id))

    user_state = bot.state[update.message.chat_id]
    user_state.state_id = StateId.XO_3

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Switched to XO game mode",
        reply_markup=reply_markup
    )

    if (user_state.xo3_game is None):
        user_state.xo3_game = TicTac3X3()

        bot.send_message (
            chat_id=update.message.chat_id,
            text="New XO 3x3 game started",
        )

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.xo3_game.getGameState(),
    )

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Awaiting your move",
    )

XO3_handler = CommandHandler('xo3', xo_3)