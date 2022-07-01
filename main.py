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
    emsg = await bot.ask(m.chat.id,
        "Send **Number or email** in this manner otherwise bot will not respond.\n\nSend like this:-  **mobile no.**"
    )  
    email = emsg.text
    
headers={
"Host": "api.penpencil.xyz",
"authorization": "Bearer",
"client-id": "5eb393ee95fab7468a79d189",
"client-version": "12.84",
"user-agent": "Android",
"randomid": "f81c3f69ed0646ed",
"client-type": "MOBILE",
"device-meta": '{"APP_VERSION":"12.84","DEVICE_MAKE":"apple","DEVICE_MODEL":"iphone 13x","OS_VERSION":"6","PACKAGE_NAME":"xyz.penpencil.physicswalb"}',
"content-type": "application/json; charset=UTF-8",
"content-length": "178",
"accept-encoding": "gzip"}
data='{"username":'+email+',"countryCode":"+91","organizationId":"5eb393ee95fab7468a79d189"}'
url="https://api.penpencil.xyz/v1/users/get-otp?smsType=0"
a=requests.post(url, headers=headers, data=data)

bot.run()
