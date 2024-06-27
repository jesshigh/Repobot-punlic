import asyncio
from userbot.core.function.emoji import emoji
from userbot.core.helpers.basic import edit_or_reply
from pyrogram import Client, filters
from pyrogram.types import Message

async def del_cmd(client, message):
    rep = message.reply_to_message
    await message.delete()
    try:
        await rep.delete()
    except AttributeError:
        pass


async def purge_cmd(client, message):
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text(emoji("bintang") + "membalas pesan untuk dibersihkan.")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )

async def purgeme_cmd(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await edit_or_reply(message, "Harap masukan angka")
    n = int(n)
    if n < 1:
        return await edit_or_reply(message, "Masukan jumlah pesan yang ingin dihapus!")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await edit_or_reply(message, "Tidak dapat menemukan pesan.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()
