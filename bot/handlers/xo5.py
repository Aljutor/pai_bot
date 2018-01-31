import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.modes.xo5 import TicTac5X5

logger = logging.getLogger(__name__)

from bot.user import StateId

def xo_5(bot, update):
    logger.info("XO_5row command, id: " + str(update.message.chat_id))

    user_state = bot.state[update.message.chat_id]
    user_state.state_id = StateId.XO_5

    reply_markup = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Switched to XO 5 in row  game mode",
        reply_markup=reply_markup
    )

    if (user_state.xo5_game is None):
        user_state.xo5_game = TicTac5X5(10, 5)

        bot.send_message (
            chat_id=update.message.chat_id,
            text="New XO 5 in row game started",
        )

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.xo5_game.getGameState(),
    )

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Awaiting your move  (A1 style)",
    )


XO5_handler = CommandHandler('xo5', xo_5)