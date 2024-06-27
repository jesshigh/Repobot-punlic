import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *
from userbot.core.function.emoji import emoji

from userbot import *

BANNED_USERS = filters.user()            


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await eor(message, emoji("proses") + "<code>Proses Ban Sedang Diproses....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>gban</code> [user_id/username/reply to uꜱer]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit(emoji("gagal") + f"tidak dapat menemukan user tersebut.")
        return
    iso = 0
    gagal = 0
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            
            if prik in DEVS:
                return await Tm.edit(
                    emoji("gagal") + f"anda tidak bisa gban dia karena dia adalah owner saya."
                )
            elif prik in prok:
                return await Tm.edit(
                    emoji("gagal") + f"anda tidak bisa gban dia, karna dia adalah admin userbot anda."
                )
            elif udah:
                return await Tm.edit(
                    f"pengguna ini ꜱudah di gban." + emoji("done")
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await Tm.edit(
        f"""
<b>global banned</b>

<b>ʙᴇʀʜᴀsɪʟ ʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜsᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )

async def cung_ban(client, message):
    user_id = await extract_user(message)
    if message.from_user.id != client.me.id:
        Tm = await eor(message, emoji("proses") + "<code>ᴍᴇᴍᴘʀᴏsᴇs.....</code>")
    else:
        Tm = await eor(message, emoji("proses") + "<code>ᴍᴇᴍᴘʀᴏsᴇs....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>ungban</code> [user_id/username/reply to user]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit(emoji("gagal") + "<b>tidak menemukan user tersebut.</b>")
        return
    iso = 0
    gagal = 0
    prik = user.id
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in BANNED_USERS:
                BANNED_USERS.remove(prik) 
            try:
                await remove_banned_user(gua, prik)
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
                await asyncio.sleep(0.1)
            except BaseException:
                gagal = gagal + 1
                await asyncio.sleep(0.1)

    return await Tm.edit(
        f"""
<b>global unbanned</b>

<b>ʙᴇʀʜᴀsɪʟ ᴜɴʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ᴜɴʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜsᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )


async def gbanlist(client, message):
    gua = client.me.id
    total = await get_banned_count(gua)
    if total == 0:
        return await message.edit(emoji("gagal") + "<b>belum ada pengguna yang digban.</b>")
    nyet = await message.edit(emoji("proses") + "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    msg = "total gbanned:\n\n"
    tl = 0
    org = await get_banned_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await nyet.edit(emoji("gagal") + "<b>belum ada pengguna yang digban.</b>")
    else:
        return await nyet.edit(msg)
