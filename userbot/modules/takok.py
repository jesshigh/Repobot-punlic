from userbot import *
from pyrogram.raw import functions
from pyrogram import filters
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup as IKM
from pyrogram.types import InlineKeyboardButton as IKB
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
import asyncio
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from userbot import OWNER_ID

@CB.CALLBACK("^takok")
async def takok_jing(c, callback_query: CallbackQuery):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    try:
        buttons = [
            [IKB("ᴄᴀɴᴄᴇʟʟ", callback_data=f"batal {user_id}")]
        ]
        pesan = await c.ask(
            user_id,
            "🗯 ᴋɪʀɪᴍ ᴘᴇsᴀɴ ᴀɴᴅᴀ, ᴀᴅᴍɪɴ ᴀᴋᴀɴ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴇsᴇɢᴇʀᴀ ᴍᴜɴɢᴋɪɴ.",
            # reply_markup=IKM(buttons),
            timeout=60,
        )
        await c.send_message(
            user_id, "✅ ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴜᴅᴀʜ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ ᴀᴅᴍɪɴ, ᴍᴏʜᴏɴ ᴅɪᴛᴜɴɢɢᴜ ʙᴀʟᴀsᴀɴɴʏᴀ"
        )
        await callback_query.message.delete()
    except asyncio.TimeoutError:
        return await c.send_message(user_id, "**Automatic cancellation**")
    button = [
        [
            IKB(full_name, user_id=user_id),
            IKB("ᴊᴀᴡᴀʙ", callback_data=f"gendeng {user_id}"),
        ],
    ]
    try:
        await pesan.copy(
            OWNER_ID,
            reply_markup=IKM(button),
        )
    except Exception as t:
        await c.send_message(user_id, f"{t}")

@CB.CALLBACK("^gendeng")
async def gendeng_jing(c, callback_query: CallbackQuery):
    user_id = int(callback_query.from_user.id)
    user_ids = int(callback_query.data.split()[1])
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    if user_ids == OWNER_ID:
        try:
            button = [
                [IKB("ʙᴀᴛᴀʟ", callback_data=f"batal {user_id}")]
            ]
            pesan = await c.ask(
                user_id,
                "sɪʟᴀᴋᴀɴ ᴋɪʀɪᴍ ʙᴀʟᴀsᴀɴ ᴀɴᴅᴀ.",
                # reply_markup=IKM(button),
                timeout=60,
            )
            await c.send_message(
                user_id,
                "✅ ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴜᴅᴀʜ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ ᴀᴅᴍɪɴ, ᴍᴏʜᴏɴ ᴅɪᴛᴜɴɢɢᴜ ʙᴀʟᴀsᴀɴɴʏᴀ",
            )
            await callback_query.message.delete()
        except asyncio.TimeoutError:
            return await c.send_message(user_id, "**Pembatalkan otomatis**")
        buttons = [
            [
                IKB(full_name, user_id=user_id),
                IKB("ᴊᴀᴡᴀʙ", callback_data=f"gendeng {user_id}"),
            ],
        ]
    else:
        try:
            button = [
                [IKB("ʙᴀᴛᴀʟ", callback_data=f"batal {OWNER_ID}")]
            ]
            pesan = await c.ask(
                OWNER_ID,
                "sɪʟᴀᴋᴀɴ ᴋɪʀɪᴍ ʙᴀʟᴀsᴀɴ ᴀɴᴅᴀ.",
                # reply_markup=IKM(button),
                timeout=60,
            )
            await c.send_message(
                OWNER_ID,
                "✅ ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴜᴅᴀʜ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ ᴀᴅᴍɪɴ, ᴍᴏʜᴏɴ ᴅɪᴛᴜɴɢɢᴜ ʙᴀʟᴀsᴀɴɴʏᴀ",
            )
            await callback_query.message.delete()
        except asyncio.TimeoutError:
            return await c.send_message(OWNER_ID, "**Pembatalkan otomatis**")
        buttons = [
            [
                IKB("ᴊᴀᴡᴀʙ", callback_data=f"gendeng {OWNER_ID}"),
            ],
        ]

    await pesan.copy(
        user_ids,
        reply_markup=IKM(buttons),
    )
