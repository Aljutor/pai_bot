import logging
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove

from bot.user import StateId
from bot.modes.matches import Matches


logger = logging.getLogger(__name__)

def matches(bot, update):
    logger.info("Matches command, id: " + str(update.message.chat_id))

    reply_markup = ReplyKeyboardRemove ()

    user_state = bot.state[update.message.chat_id]
    user_state.state_id = StateId.Matches

    bot.send_message(
        chat_id=update.message.chat_id,
        text="Switched to matches game mode",
        reply_markup=reply_markup
    )

    if (user_state.matches_game is None):
        user_state.matches_game = Matches(21, 3)

        bot.send_message (
            chat_id=update.message.chat_id,
            text="New matches game started",
        )

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.matches_game.getGameState(),
    )

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Awaiting your move (1 - 3)",
    )


Matches_handler = CommandHandler('matches', matches)