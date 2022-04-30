import os
import sys
import asyncio
import telethon.utils
from telethon import TelegramClient
from RiZoeLXSpam import BOT_TOKEN, API_ID, API_HASH

RiZoeL = TelegramClient('RiZoeL', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
