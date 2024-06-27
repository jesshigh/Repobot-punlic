from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userbot.config import LOGS_MAKER_UBOT, OWNER_ID
from userbot import bot, ubot
from userbot.core.database import get_expired_date

class MSG:
    def DEAK(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ telah berhasil di hapus dari telegram</b>
"""
            
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ masa aktif telah habis</b>
"""

    
    def START(message):
        return f"""
<b> ❏ 𝙷𝚊𝚕𝚕𝚘 <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>
   
 💬 @Dev_GhostBo ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜ𝚜ᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ  
 ⚠️ 𝙽𝚘𝚝𝚎 : 𝚍𝚎𝚗𝚐𝚊𝚗 𝚜𝚢𝚊𝚛𝚊𝚝 𝚔𝚊𝚖𝚞 𝚜𝚞𝚍𝚊𝚑 𝚖𝚎𝚕𝚊𝚔𝚞𝚔𝚊𝚗 𝚙𝚎𝚖𝚋𝚊𝚢𝚊𝚛𝚊𝚗 𝚊𝚐𝚊𝚛 𝚋𝚒𝚜𝚊 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚞𝚜𝚎𝚛𝚋𝚘𝚝 𝚒𝚗𝚒.  
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
ꜱɪʟᴀᴋᴀɴ ʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ

ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000

💳 ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:
 ├──• ʜᴜʙᴜɴɢɪ:
 ├─• @AnakManis5

🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ:  Rp {total}.000
🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}

✅ ꜱɪʟᴀʜᴋᴀɴ ꜱᴄᴀɴ ǫʀɪꜱ <a href=https://telegra.ph/file/d3819574afbe4fe2712e8.jpg> ᴅɪꜱɪɴɪ </a>

✅ ᴊɪᴋᴀ ꜱᴜᴅᴀʜ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ʙᴜᴋᴛɪ ᴛꜰ ᴘᴇᴍʙᴀʏᴀʀᴀɴ, 
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ userbot ke</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ akun:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ id:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ expired</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""

    def POLICY():
        return """
Kebijakan Pengembalian:
Note :
Setelah melakukan pembayaran, jika anda belum menerima manfaat dari pembelian, 
anda berhak untuk mengajukan pengembalian dalam waktu 1 Jam setelah pembelian. 
Namun, jika anda telah menggunakan atau menerima salah satu manfaat dari pembelian, 
termasuk akses ke fitur pembuatan userbot, maka anda tidak lagi memenuhi syarat untuk pengembalian dana.

Dukungan:

Untuk mendapatkan bantuan atau dukungan, 
anda dapat menghubungi admin di bawah ini atau mengirim pesan ke @AnakManis5 di Telegram. 
Perlu diingat, jangan menghubungi Dukungan Telegram atau 
Dukungan Bot untuk masalah terkait pembayaran yang dilakukan di bot ini.

Tombol Lanjutkan:

Klik tombol "Lanjutkan" untuk mengkonfirmasi 
bahwa anda telah membaca dan menerima ketentuan ini dan 
melanjutkan proses pembelian. Jika tidak, klik tombol "Kembali".
"""


async def sending_user(user_id):
    try:
        if bot and bot.me and bot.me.username:
            await bot.send_message(
                user_id,
                "💬 silahkan buat ulang userbot anda",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "buat userbot",
                                callback_data="bahan",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                f"""
➡️ yang merasa memiliki id: {user_id}

✅ silahkan buat ulang userbot nya di: @{bot.me.username}
        """,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📁 cek masa aktif 📁",
                                callback_data=f"cek_masa_aktif {user_id}",
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )
        else:
            print("Bot belum diinisialisasi dengan benar atau atribut 'me' tidak tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        # Lakukan penanganan kesalahan sesuai kebutuhan anda
