from userbot import *

__MODULE__ = "ꜱᴀɴɢᴍᴀᴛᴀ"
__HELP__ = f"""
<b>『 bantuan untuk sangmata 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}sg</code> [user_id/reply user]
  <b>• penjelasan:</b> untuk memeriksa histori nama/username
"""


@CB.UBOT("sg", sudo=False)
async def _(client, message):
    await sg_cmd(client, message)
