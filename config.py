import os
class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    DATABASE = os.environ.get("DATABASE", "")

    DEV_NAME = os.environ.get("DEV_NAME", "Muhammed")

    DEV_ID = set(int(x) for x in os.environ.get("DEV_ID", "1855070892").split())
