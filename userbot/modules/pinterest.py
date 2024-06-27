import requests
from pyrogram import filters
from userbot import *
from pyrogram.errors.exceptions.bad_request_400 import MediaInvalid
from pyrogram.types import Message, InputMediaPhoto
import wget
import os
import glob

MODULE = "ᴘɪɴᴛᴇʀᴇꜱᴛ"
HELP = """
『 Pinterest 』

  • perintah: {0}pint jumlah kata_kunci
  • penjelasan: untuk mendownload media di pinterest.
"""

@CB.UBOT("pint")
async def pinterest(client, message):
    chat_id = message.chat.id

    if len(message.command) < 3:
        return await message.reply("Gunakan .pint jumlah kata_kunci")

    msg = await message.reply("🔍Sedang mencari...")

    try:
        jumlah = int(message.command[1])
        query = ' '.join(message.command[2:])
    except (IndexError, ValueError):
        return await msg.edit("❌ Salin url dari pinterest dan ketik .pint jumlah kata_kunci 🔍")

    try:
        response = requests.get(f"https://pinterest-api-one.vercel.app/?q={query}")
        response.raise_for_status()
    except requests.RequestException as e:
        return await msg.edit(f"Gagal mengambil data dari API: {e}")

    images = response.json().get("images", [])
    if not images:
        return await msg.edit("Tidak ada gambar yang ditemukan.")

    media_group = []
    for url in images[:jumlah]:
        try:
            image_response = requests.get(url, stream=True)
            if image_response.status_code == 200:
                potonya = wget.download(url)
                media_group.append(InputMediaPhoto(media=potonya))
            else:
                await message.reply(f"URL tidak dapat dijangkau: {url}")
        except requests.RequestException as e:
            await msg.edit(f"Gagal mengakses URL: {url} - Error: {e}")

    if media_group:
        try:
            await client.send_media_group(chat_id, media_group)
        except MediaInvalid:
            for meki in images[:jumlah]:
                try:
                    await client.send_photo(chat_id, meki)
                except:
                    pass
        except Exception as e:
            await msg.edit(f"Gagal mengirim media: {e}")
    else:
        await msg.edit("Tidak ada media yang valid untuk dikirim.")

    await msg.delete()
    try:
        os.system("rm -rf *.jpg")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")
