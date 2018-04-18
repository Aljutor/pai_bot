import os
import logging
import telegram
from bot.bot import Bot


SOCKS_URL = 'socks5://<your_sock5_proxy_host>:1080/'
SOCKS_USER = '<your_sock5_proxy_user>'
SOCKS_PASS = '<your_sock5_proxy_password>'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

from telegram.vendor.ptb_urllib3.urllib3.contrib.socks import SOCKSProxyManager

def main():
    token = os.environ['BOT_TOKEN']
    bot = Bot(token)
    bot.start()


if __name__ == '__main__':
    main()
