from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from userbot import *

class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="tutup",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}"
                ),
                InlineKeyboardButton(
                    text="stats",
                    callback_data="sys_stats"
                ),
            ]
        ]
        return button
        
        
    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} bulan",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "👤 dapatkan profil 👤", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ tolak pembayaran ❌", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if message.from_user.id not in USER_ID:
            button = [
                [
                InlineKeyboardButton("🔥ʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ🔥", callback_data="bahan")
                ],
                [
                InlineKeyboardButton(text="💬 ꜱᴜᴘᴘᴏʀᴛ", callback_data="takok"),
                InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ ᴀᴋᴜɴ ✨", callback_data="pler")
                ],
                [
                InlineKeyboardButton("⚙️ʜᴇʟᴘ ᴍᴇɴᴜ ⚙️", callback_data="help_back")
                ],
            ]
        else:
            button = [
                [InlineKeyboardButton("🔥ʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ🔥", callback_data="bahan")],
                [
                    InlineKeyboardButton("🛠 updates", callback_data="cb_gitpull"),
                    InlineKeyboardButton("ʀᴇꜱᴛᴀʀᴛ 🔄", callback_data="cb_restart"),
                ],
                [
                    InlineKeyboardButton("ɢᴇᴛᴜʙᴏᴛ 📋", callback_data="cek_ubot"),
                    InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ ᴠᴘꜱ 💾", callback_data="host"),
                ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [
                InlineKeyboardButton("konfirmasi", callback_data="confirm"),
                InlineKeyboardButton("kembali", callback_data="bahan"),
            ]
        ]
        return button

    
    def ambil_akun(user_id, count):
        button = [
             [
                 InlineKeyboardButton(
                     "📁 ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ 📁",
                     callback_data=f"del_ubot {int(user_id)}",
                 )
            ],
            [
                 InlineKeyboardButton(
                    "📲 ᴄᴇᴋ ɴᴏᴍᴏʀ 📲",
                     callback_data=f"get_phone {int(count)}",
                 )
             ],
            [
                InlineKeyboardButton(
                    "⏳ ᴄᴇᴋ ᴋᴀᴅᴀʟᴜᴡᴀʀꜱᴀ ⏳",
                     callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                     "🔑 ᴄᴇᴋ ᴏᴛᴘ 🔑",
                     callback_data=f"get_otp {int(count)}",
                 )
            ],
            [
                InlineKeyboardButton(
                     "🔐 ᴄᴇᴋ ᴠᴇʀɪꜰɪᴋᴀꜱɪ 2ʟ 🔐",
                     callback_data=f"get_faktor {int(count)}",
                 )
             ],
             [
                 InlineKeyboardButton(
                     "☠ ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ☠", callback_data=f"ub_deak {int(count)}",
                 )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"next_ub {int(count)}"),
            ],  
        ]
        return button

    def deak(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "kembali",
                    callback_data=f"prev_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "setuJui ✅", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button
        
def absen_hadir(get_id):
        buttons =[
            [InlineKeyboardButton("Hadir", callback_data="hadir")],
        ]
        return button
      
                
       
class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"anda belum order @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"silahkan order di @{bot.me.username} dulu biar bisa menggunakan inline ini"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"gak usah klik-klik mending Langsung order di @{bot.me.username}",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper


async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = m.text.split("~>", 1)
    for X in split_text[1].split():
        button_data = X.split(":", 1)
        button_label = button_data[0].replace("_", " ")
        button_url = button_data[1]
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0].split(None, 1)[1]
    return buttons, text_button


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("~>", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button
    
   
async def pmpermit_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("~>", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button
