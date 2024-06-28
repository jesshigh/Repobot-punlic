import random
import requests
import asyncio
import os

from pyrogram import *
from pyrogram.types import *
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from userbot.core.helpers.basic import edit_or_reply
from userbot import *

__MODULE__ = "ᴛᴏᴏʟꜱ"
__HELP__ = f"""
<b>『 ᴛᴏᴏʟꜱ 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ssweb</code>
  <b>• penjelasan:</b> Untuk mengambil screenshot dari web
  
  <b>• perintah:</b> <code>{PREFIX[0]}tinyurl</code>
  <b>• penjelasan:</b> Untuk memperpendek URL menggunakan TinyURL

  <b>• perintah:</b> <code>{PREFIX[0]}npm</code>
  <b>• penjelasan:</b> Untuk mencari paket NPM

  <b>• perintah:</b> <code>{PREFIX[0]}movie</code>
  <b>• penjelasan:</b> Untuk mencari informasi film
"""

@CB.UBOT("ssweb", sudo=False)
async def screenshot_web(client, message):
    url = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not url:
        await message.reply("`Mohon berikan URL yang valid.`")
        return

    loading_msg = await message.reply("Sedang mengambil screenshot...")

    screenshot_url = f"https://api.screenshotmachine.com/?key=49dcbd&dimension=1024x768&format=png&cacheLimit=0&url={url}"
    
    try:
        response = requests.get(screenshot_url)
        if response.status_code == 200:
            await client.send_photo(message.chat.id, screenshot_url, caption=f"**SS WEB DARI:** {url}")
        else:
            await message.reply("`Gagal mengambil screenshot. Mohon coba lagi.`")
    except Exception as e:
        print(e)
        await message.reply("`Terjadi kesalahan. Mohon coba lagi.`")
    finally:
        await loading_msg.delete()

@CB.UBOT("tinyurl", sudo=False)
async def tinyurl(client, message):
    url = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not url:
        await message.reply("`Mohon berikan URL yang valid.`")
        return

    loading_msg = await message.reply("Sedang memperpendek URL...")

    tinyurl_api = f"https://tinyurl.com/api-create.php?url={url}"
    
    try:
        response = requests.get(tinyurl_api)
        if response.status_code == 200:
            short_url = response.text
            await client.send_message(message.chat.id, f"Berikut URL Anda: {short_url}")
        else:
            await message.reply("`Gagal memperpendek URL. Mohon coba lagi.`")
    except Exception as e:
        print(e)
        await message.reply("`Terjadi kesalahan. Mohon coba lagi.`")
    finally:
        await loading_msg.delete()

@CB.UBOT("npm", sudo=False)
async def npm_search(client, message):
    query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply("`Mohon berikan nama paket NPM yang valid.`")
        return

    loading_msg = await message.reply("Sedang mencari paket NPM...")

    npm_api_url = f"https://registry.npmjs.com/-/v1/search?text={query}"
    
    try:
        response = requests.get(npm_api_url)
        if response.status_code == 200:
            data = response.json()
            objects = data.get('objects', [])
            if not objects:
                await message.reply(f"`Paket NPM dengan nama \"{query}\" tidak ditemukan.`")
                return

            result = "\n\n".join([
                f"*{pkg['name']}* (v{pkg['version']})\n[{pkg['links']['npm']}]({pkg['links']['npm']})\n_{pkg['description']}_"
                for pkg in (obj['package'] for obj in objects)
            ])

            await client.send_message(message.chat.id, result, parse_mode="Markdown")
        else:
            await message.reply("`Gagal mencari paket NPM. Mohon coba lagi.`")
    except Exception as e:
        print(e)
        await message.reply("`Terjadi kesalahan. Mohon coba lagi.`")
    finally:
        await loading_msg.delete()

@CB.UBOT("movie", sudo=False)
async def movie_search(client, message):
    movie_name = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not movie_name:
        await message.reply("`Mohon berikan nama film yang valid.`")
        return

    loading_msg = await message.reply("Sedang mencari informasi film...")

    movie_api_url = f"https://moviedetails.apinepdev.workers.dev/?moviename={requests.utils.quote(movie_name)}"
    
    try:
        response = requests.get(movie_api_url)
        if response.status_code == 200:
            movie_data = response.json()
            if not movie_data:
                await message.reply(f"`Film dengan nama \"{movie_name}\" tidak ditemukan.`")
                return

            poster_url = movie_data.get('Poster', 'https://via.placeholder.com/300x450?text=No+Image')
            caption = (
                f"🎬 *{movie_data.get('Title', 'N/A')}* ({movie_data.get('Year', 'N/A')})\n"
                f"⭐ *Rating:* {movie_data.get('Ratings', [{'Value': 'N/A'}])[0]['Value']}\n"
                f"🎭 *Genre:* {movie_data.get('Genre', 'N/A')}\n"
                f"🎥 *Director:* {movie_data.get('Director', 'N/A')}\n"
                f"👥 *Actors:* {movie_data.get('Actors', 'N/A')}\n"
                f"📝 *Plot:* {movie_data.get('Plot', 'N/A')}\n"
                f"🌍 *Country:* {movie_data.get('Country', 'N/A')}\n"
                f"🔊 *Language:* {movie_data.get('Language', 'N/A')}"
            )

            await client.send_photo(message.chat.id, poster_url, caption=caption, parse_mode="Markdown")
        else:
            await message.reply("`Gagal mencari informasi film. Mohon coba lagi.`")
    except Exception as e:
        print(e)
        await message.reply("`Terjadi kesalahan. Mohon coba lagi.`")
    finally:
        await loading_msg.delete()

# The usual way to run the bot
# if __name__ == "__main__":
#     app = Client("my_account")
#     app.run()
