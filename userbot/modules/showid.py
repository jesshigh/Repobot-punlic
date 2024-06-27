from userbot import *

__MODULE__ = "ᴄᴇᴋɪᴅ"
__HELP__ = f"""
<b>『 bantuan untuk showid 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}id</code>
  <b>• penjelasan:</b> untuk mengetahui id dari user/grup/channel

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [reply to user/media]
  <b>• penjelasan:</b> untuk mengetahui id dari user/media

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [username user/grup/channel]
  <b>• penjelasan:</b> untuk mengetahui id user/grup/channel melalui username
"""

@CB.UBOT("id", sudo=True)
async def _(client, message):
    await id_cmd(client, message)
