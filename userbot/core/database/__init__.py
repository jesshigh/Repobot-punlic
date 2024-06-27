from motor.motor_asyncio import AsyncIOMotorClient

from userbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.ilauserbot

from userbot.core.database.expired import *
from userbot.core.database.notes import *
from userbot.core.database.premium import *
from userbot.core.database.reseller import *
from userbot.core.database.saved import *
from userbot.core.database.userbot import *
from userbot.core.database.pref import *
from userbot.core.database.otp import *
from userbot.core.database.gbans import *
from userbot.core.database.setvar import *
from userbot.core.database.logger import *
from userbot.core.database.bcast import *
from userbot.core.database.permit import *

