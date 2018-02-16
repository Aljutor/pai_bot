import os
import logging

from telegram import ReplyKeyboardRemove
from telegram.ext import MessageHandler, Filters

from yandex_translate import YandexTranslate

from bot.user import StateId
from bot.modes.talk.command import query

from bot.handlers.matches import matches
from bot.handlers.talk import talk
from bot.handlers.xo3 import xo_3
from bot.handlers.xo5 import xo_5


logger = logging.getLogger(__name__)

translate = YandexTranslate(os.environ['TR_TOKEN'])

def text(bot, update):
    logger.info ("Text command, id: " + str (update.message.chat_id) + " text: " + update.message.text)

    user_state = bot.state[update.message.chat_id]
    text = update.message.text.lower()

    switch_mode_words = [
        'switch',
        'select'
        'change',
        'exchange',
        'play',
        'show',
        'start',
        'open'

    ]
    tic_tac_words = ['tic-tac', 'tic tac', 'in a row', 'tictac']
    matches_words = ['matches']
    talk_words = ['talk', 'math', 'dialog']

    for x in switch_mode_words:
        if x in text:
            for y in tic_tac_words:
                if y in text:
                    if '5' in text or 'five' in text:
                        xo_5(bot, update)
                        return
                    else:
                        xo_3(bot, update)
                        return

            for y in matches_words:
                if y in text:
                    matches(bot, update)
                    return

            for y in talk_words:
                if y in text:
                    talk(bot, update)
                    return

    if (user_state.state_id == StateId.Talk):
        talk_handler(bot, update)

    if (user_state.state_id == StateId.XO_5):
        xo5_game_handler(bot, update)

    if (user_state.state_id == StateId.XO_3):
        xo3_game_handler(bot, update)

    if (user_state.state_id == StateId.Matches):
        matches_game_handler(bot, update)

    if (user_state.state_id == StateId.Translate):
        translate_handler(bot, update)


Text_handler = MessageHandler (Filters.text, text)


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
            reply_markup=reply_markup,
        )

        return


    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.xo5_game.getGameState(),
        reply_markup=reply_markup,
        parse_mode = "MARKDOWN"
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

    ok = user_state.xo3_game.xo_bot(update.message.text)

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
    reply_markup = ReplyKeyboardRemove ()

    user_state = bot.state[update.message.chat_id]

    if (user_state.matches_game is None):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="No game found, use /matches to start new game",
            reply_markup=reply_markup
        )

        return

    ok = user_state.matches_game.sendUserMove(update.message.text)

    if (not ok):
        bot.send_message (
            chat_id=update.message.chat_id,
            text="Invalid Move",
            reply_markup=reply_markup
        )

        return

    bot.send_message (
        chat_id=update.message.chat_id,
        text=user_state.matches_game.getGameState(),
        reply_markup=reply_markup
    )

    winner = user_state.matches_game.getWin()

    if (winner is not None):
        user_state.matches_game = None
        user_state.state_id = StateId.Start

        bot.send_message (
            chat_id=update.message.chat_id,
            text="Game Over, Winner: " + winner,
            reply_markup=reply_markup
    )

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

def translate_handler(bot, update):
    reply_markup = ReplyKeyboardRemove ()

    text = translate.translate(update.message.text, 'ru').get('text')

    if len(text) < 1:
        bot.send_message (
            chat_id=update.message.chat_id,
            text="Translation error",
            reply_markup=reply_markup
        )

        return

    bot.send_message (
        chat_id=update.message.chat_id,
        text="Translation: " + text[0],
        reply_markup=reply_markup
    )