import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import logging
from pyrogram import Client, filters
from subprocess import getstatusoutput
import re
from pyrogram.types import User, Message
import os

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

logger = logging.getLogger()
thumb = os.environ.get("THUMB")
if thumb.startswith("http://") or thumb.startswith("https://"):
    getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
    thumb = "thumb.jpg"


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **physics Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/login** to continue..\n\n")

@bot.on_message(filters.command(["login"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Number or email** in this manner otherwise bot will not respond.\n\nSend like this:-  **mobile no.**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    

headers = {
    'Host': 'api.penpencil.xyz',
    'authorization': 'Bearer',
    'client-id': '5eb393ee95fab7468a79d189',
    'client-version': '12.84',
    'user-agent': 'Android',
    'randomid': 'e4307177362e86f1',
    'client-type': 'MOBILE',
    'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '89',
    # 'accept-encoding': 'gzip',
}

params = {
    'smsType': '0',
}

json_data = {
    'username': f'{raw_text1}',
    'countryCode': '+91',
    'organizationId': '5eb393ee95fab7468a79d189',
}

response = requests.post('https://api.penpencil.xyz/v1/users/get-otp', params=params, headers=headers, json=json_data)
bot.run()
