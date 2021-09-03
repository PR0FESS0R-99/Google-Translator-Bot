import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client
from config import Config

logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(
        root="Google_Translator_Bot"
    )
    mt_botz = Client(
        "MT Google Translator Bot ",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )
    mt_botz.run()
