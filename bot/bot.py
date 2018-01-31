import logging

from collections import defaultdict

from telegram.ext import Updater
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

from bot.user import UserState

from bot.handlers.math import Math_handler
from bot.handlers.xo5 import XO5_handler
from bot.handlers.start import Start_handler
from bot.handlers.matches import Matches_handler
from bot.handlers.xo3 import XO3_handler

from bot.handlers.message import Text_handler

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token):
        logger.info("Creating bot")
        self.updater = Updater(token)

        self.updater.bot.state = defaultdict(UserState)

        self.dispatcher = self.updater.dispatcher

        self._set_handlers()

    def _set_handlers(self):
        logger.info("Setup handlers")
        self.dispatcher.add_handler(Start_handler)
        self.dispatcher.add_handler(Math_handler)
        self.dispatcher.add_handler(Matches_handler)
        self.dispatcher.add_handler(XO3_handler)
        self.dispatcher.add_handler(XO5_handler)

        self.dispatcher.add_handler(Text_handler)

        def error_callback(bot, update, error):
            try:
                raise error
            except Unauthorized:
                logger.error("Unauthorized")
                # remove update.message.chat_id from conversation list
            except BadRequest:
                logger.error ("BadRequest")
                # handle malformed requests - read more below!
            except TimedOut:
                logger.error ("TimedOut")
                # handle slow connection problems
            except NetworkError:
                logger.error ("NetworkError")
                # handle other connection problems
            except ChatMigrated as e:
                logger.error ("ChatMigrated")
                # the chat_id of a group has changed, use e.new_chat_id instead
            except TelegramError:
                logger.error ("TelegramError")
                # handle all other telegram related errors

        self.dispatcher.add_error_handler (error_callback)

    def start(self):
        logger.info("Bot started")
        self.updater.start_polling()
