import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import MessageHandler, Filters

from bot.user import StateId
from bot.modes.talk.command import query


logger = logging.getLogger(__name__)

def text(bot, update):
    logger.info("Text command, id: " + str(update.message.chat_id) + " text: " + update.message.text)

    user_state = bot.state[update.message.chat_id]

    if (user_state.state_id == StateId.Talk) :
        talk_handler(bot, update)

    if (user_state.state_id == StateId.XO_5) :
        xo5_game_handler(bot, update)

    if (user_state.state_id == StateId.XO_3):
        xo3_game_handler(bot, update)

    if (user_state.state_id == StateId.Matches):
        matches_game_handler(bot, update)

Text_handler = MessageHandler(Filters.text, text)


def xo5_game_handler(bot, update):
    reply_markup = ReplyKeyboardRemove ()

    user_state = bot.state[update.message.chat_id]

    if (user_state.xo5_game is None):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="No game found, use /xo5 to start new game",
            reply_markup=reply_markup
        )

        return

    ok = user_state.xo5_game.sendUserMove(update.message.text)

    if (not ok):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="Invalid Move",
            reply_markup=reply_markup
        )

        return


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
            text="Game Over, Winner: " + winner,
            reply_markup=reply_markup
    )

def xo3_game_handler(bot, update):
    reply_markup = ReplyKeyboardRemove ()

    user_state = bot.state[update.message.chat_id]

    if (user_state.xo3_game is None):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="No game found, use /xo3 to start new game",
            reply_markup=reply_markup
        )

        return

    ok = user_state.xo3_game.sendUserMove(update.message.text)

    if (not ok):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="Invalid Move",
            reply_markup=reply_markup
        )

        return

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.xo3_game.getGameState(),
        reply_markup=reply_markup
    )

    winner = user_state.xo3_game.getWin()

    if (winner is not None):
        user_state.xo3_game = None
        user_state.state_id = StateId.Start

        bot.send_message (
            chat_id=update.message.chat_id,
            text="Game Over, Winner: " + winner,
            reply_markup=reply_markup
    )

def matches_game_handler(bot, update):
    pass

def talk_handler(bot, update):
    reply_markup = ReplyKeyboardRemove ()

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Thinking...",
        reply_markup=reply_markup
    )

    result = query(update.message.text)
    print(result)

    if (result is None or result == ""):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="Woops, sorry I am not smart enough",
            reply_markup=reply_markup
        )

        return

    bot.send_message (
        chat_id=update.message.chat_id,
        text=result,
        reply_markup=reply_markup
    )