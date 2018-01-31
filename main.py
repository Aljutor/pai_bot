import logging
from bot.bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

token = "468336611:AAERPcwsq4iWifxpdqCJdU2v66fG7ftzDjA"

def main():
    bot = Bot(token)
    bot.start()


if __name__ == '__main__':
    main()