import os

DEVS = [
    6934282635
]

API_ID = int(os.getenv("API_ID", "27934485"))

API_HASH = os.getenv("API_HASH", "922751167fa262b2fb1f6f23b595ed7b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6536595465:AAG28m_S0eaopeU-dgxIgJE2S_NXZXcQnFM")

OWNER_ID = int(os.getenv("OWNER_ID", "6934282635"))

USER_ID = list(map(int,os.getenv("USER_ID", "6934282635",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002170796011"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002170796011").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ayuniarisati:dante4636@cluster0.ds9fhwc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
