from userbot import *

__MODULE__ = "ꜱᴇᴄʀᴇᴛ"
__HELP__ = f"""
<b>『 bantuan untuk secret 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}msg</code> [reply to user - text]
  <b>• penjelasan:</b> untuk mengirim pesan secara rahasia
"""


@CB.UBOT("msg", sudo=False)
async def _(client, message):
    await msg_cmd(client, message)


@CB.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
