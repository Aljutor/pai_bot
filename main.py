import os
import logging

from bot.bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    token = os.environ['BOT_TOKEN']
    bot = Bot(token)
    bot.start()


if __name__ == '__main__':
    main()
