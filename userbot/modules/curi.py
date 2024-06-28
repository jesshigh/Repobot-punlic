import asyncio
import os

from pyrogram import *
from pyrogram.types import *
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from userbot.core.helpers.basic import edit_or_reply
from userbot import *

__MODULE__ = "ᴄᴜʀɪ"
__HELP__ = f"""
<b>『 Curi 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}curi</code>
  <b>• penjelasan:</b> .curi untuk mengambil pap timer

"""

@CB.UBOT("curi", sudo=False)
async def pencuri(client, message):
    dia = message.reply_to_message
    me = client.me.id
    if not dia:
        await edit_or_reply(message, "`Mohon balas ke media.`")
    anjing = dia.caption or None
    await edit_or_reply(message, "`Processing...`")
    if dia.text:
        await dia.copy("me")
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    try:
        await client.send_message("me", "**Pap timernya tuh.**")
    except Exception as e:
        print(e)


@CB.UBOT("qris", sudo=False)
async def send_qris(client, message):
    if len(message.command) < 2:
        await message.reply("Mohon sertakan nominalnya. Contoh: .qris 50000")
        return
    
    nominal = message.command[1]
    loading_msg = await message.reply("Loading.......")
    qris_image_url = "https://telegra.ph/file/d3819574afbe4fe2712e8.jpg"
    caption = f"Silahkan TF Dengan Nominal {nominal} Ke Ghostxmods"

    try:
        await asyncio.sleep(2)  # Simulate some loading time
        await client.send_photo(message.chat.id, qris_image_url, caption=caption)
    except Exception as e:
        print(e)
    finally:
        await loading_msg.delete()
