import logging

from telegram.ext import CommandHandler

from bot.user import StateId

logger = logging.getLogger(__name__)

def help_cmd(bot, update):
    logger.info("Start command, id: " + str(update.message.chat_id))

    bot.state[update.message.chat_id].state_id = StateId.Start

    text = "Telegram bot for PAI 486 course \n" \
           "\n" \
           "Select bot mode by using one of cmd: \n" \
           "/start   - return to start menu \n" \
           "/talk    - talk mode (can solve simple math) \n" \
           "/matches - 21 matches game \n" \
           "/xo3     - classic 3x3 TicTacToe game \n" \
           "/xo5     - TicTackToe on 10x10 filed, 5 in row \n" \
           "\n" \
           "Game state saved (until bot restart) \n" \
           "After game over use command again to start new game \n" \
           "You can switch between modes on the fly \n" \
           "Use /start to return in menu"

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )

Help_handler = CommandHandler('help', help_cmd)