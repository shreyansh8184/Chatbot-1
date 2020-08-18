import os
import sys
import logging

from pyrogram import Client

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# If python version < 3.6, quit
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You need at least python v3.6.x\nBot quitting.")
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    STRING_SESSION = os.environ.get("STRING_SESSION")
    CF_API_KEY = os.environ.get("CF_API_KEY")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    NAME = os.environ.get("NAME")
    TOKEN = os.environ.get("TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = int(os.environ.get("API_HASH"))
else:
    from configparser import ConfigParser
    
    parser = ConfigParser()
    parser.read("config.ini")
    
    STRING_SESSION = parser.get("config", "STRING_SESSION")
    CF_API_KEY = parser.get("config", "CF_API_KEY")
    DATABASE_URL = parser.get("config", "DATABASE_URL")
    NAME = parser.get("config", "NAME")
    
token = TOKEN
app_id = API_ID
app_hash = API_HASH
app = Client(
    "chatbot,
    bot_token=token,
    api_id=app_id,
    api_hash=app_hash
)
