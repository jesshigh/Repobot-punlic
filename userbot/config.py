import os

DEVS = [
    6934282635
]

API_ID = int(os.getenv("API_ID" ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", ""))

USER_ID = list(map(int,os.getenv("USER_ID", "",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", ""))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL")
