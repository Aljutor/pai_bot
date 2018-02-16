import logging

from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

from bot.user import StateId

logger = logging.getLogger(__name__)

help_text = "Telegram bot for PAI 486 course \n" \
            "\n" \
            "Select bot mode by using one of cmd: \n" \
            "/start   - return to start menu \n" \
            "/talk    - talk mode (can solve simple math) \n" \
            "/matches - 21 matches game \n" \
            "/xo3     - classic 3x3 TicTacToe game \n" \
            "/xo5     - TicTacToe on 10x10 filed, 5 in row \n" \
            "/translate - translate ENG -> RUS" \
            "\n" \
            "Game state saved (until bot restart) \n" \
            "After game over use command again to start new game \n" \
            "You can switch between modes on the fly \n" \
            "Use /start to return in menu \n" \
            "Additional you can you voice commands (analog of text) \n" \
            "'play tic-tac-toe' \n" \
            "'switch to translate' \n" \
            "'play 5 in row' \n" \
            "'switch to math' \n" \


def start(bot, update):
    logger.info("Start command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Start

    start_keyboard = [['/xo3'],
                       ['/xo5'],
                       ["/talk"],
                       ['/matches'],
                       ['/translate']
                      ]


    reply_markup = ReplyKeyboardMarkup (start_keyboard)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=help_text,
        reply_markup=reply_markup
    )

Start_handler = CommandHandler('start', start)


def help_cmd(bot, update):
    logger.info("Help command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Start


    bot.send_message(
        chat_id=update.message.chat_id,
        text=help_text,
    )

Help_handler = CommandHandler('help', help_cmd)