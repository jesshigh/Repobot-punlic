import uvloop
uvloop.install()
import logging
import os
import asyncio
import re

from pyrogram import Client, filters
from pyrogram.enums import ParseMode 
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pyromod import listen
from pytgcalls import GroupCallFactory
from aiohttp import ClientSession
from userbot.config import *

from motor.motor_asyncio import AsyncIOMotorClient
conn = AsyncIOMotorClient(MONGO_URL)

class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for error_type in ["OSError", "TimeoutError"]:
            if error_type in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m userbot")

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

import asyncio
from aiohttp import ClientSession

# Assuming 'aiosession' is used later in the code, you'll need to create it within an async function.
async def create_aiosession():
    async with ClientSession() as session:
        return session  # You can return or use 'session' here based on your bot's logic

# Main function that runs the event loop
async def main():
    global aiosession
    aiosession = await create_aiosession()  # Await the session creation
    # Continue with the rest of your bot logic here

if __name__ == "__main__":
    asyncio.run(main())  # This ensures the event loop is running

LOOP = asyncio.get_event_loop_policy()
event_loop = LOOP.get_event_loop()
asyncio.set_event_loop(event_loop)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="Ghostxmods UBot")

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="Ghostxmods UBot")
        self.group_call = GroupCallFactory(self).get_group_call()
        self.device_model = "Ghostxmods UBot"

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix
    
    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, ["."])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            if message.text:
                text = message.text.strip().encode("utf-8").decode("utf-8")
                username = client.me.username or ""
                prefixes = await self.get_prefix(client.me.id)

                if not text:
                    return False

                for prefix in prefixes:
                    if not text.startswith(prefix):
                        continue

                    without_prefix = text[len(prefix) :]

                    for command in cmd.split("|"):
                        if not re.match(
                            rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                            without_prefix,
                            flags=re.IGNORECASE | re.UNICODE,
                        ):
                            continue

                        without_command = re.sub(
                            rf"{command}(?:@?{username})?\s?",
                            "",
                            without_prefix,
                            count=1,
                            flags=re.IGNORECASE | re.UNICODE,
                        )
                        message.command = [command] + [
                            re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                            for m in command_re.finditer(without_command)
                        ]

                        return True

                return False

        return filters.create(func)

    async def start(self):
        await super().start()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = ["."]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")

bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)

ubot = Ubot(name="ubot")

from userbot.core.database import *
from userbot.core.function import *
from userbot.core.helpers import *
from userbot.core.plugins import *
