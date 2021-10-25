from pyrogram import Client
from config import Config

if __name__ == "__main__" :

    mt_botz = Client(
        "MT Google Translator Bot ",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=dict(
        root="Google_Translator_Bot"
        ),
        workers=100
    )
    mt_botz.run()
