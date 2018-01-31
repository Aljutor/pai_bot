import logging
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardRemove


from bot.user import StateId

logger = logging.getLogger(__name__)

def text(bot, update):
    logger.info("Text command, id: " + str(update.message.chat_id) + " text: " + update.message.text)

    user_state = bot.state[update.message.chat_id]

    reply_markup = ReplyKeyboardRemove()

    if (user_state.state_id == StateId.XO_5) :

        user_state.xo5_game.sendUserMove(update.message.text)

        bot.send_message (
            chat_id=update.message.chat_id,
            text=user_state.xo5_game.getGameState(),
            reply_markup=reply_markup
        )

        winner = user_state.xo5_game.getWin()

        if (winner is not None):
            user_state.xo5_game = None
            user_state.state_id = StateId.Start

            bot.send_message (
                chat_id=update.message.chat_id,
                text="Game Ended, Winner: " + winner,
                reply_markup=reply_markup
        )


Text_handler = MessageHandler(Filters.text, text)