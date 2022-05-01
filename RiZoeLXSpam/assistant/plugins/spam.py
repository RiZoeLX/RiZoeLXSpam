import os 
import asyncio
import re
from telethon import events
from resources.data import *
from telethon.tl import functions
from RiZoeLXSpam import OWNER_ID, hl

SEND_COUNT ="**Send Counts**"
SEND_SPAM = "**Send spam message to spam**"
ABORT = "**All process Cancelled !**"

@RiZoeL.on(events.NewMessage(pattern="[!/]spam"))
async def spam(event):
     if event.sender_id in DEV or event.sender_id in SUDO_USERS:
            await event.reply("**We'll Add This Cmd Soon.**")

@RiZoeL.on(events.NewMessage(pattern="[!/]dmspam"))
async def dm_spam(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
         return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Username or ID of user to Start DM Spam**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        username = res.message.message
        if username.startswith("@"):
            try:
               k = await Riz.get_entity(username)
               id = k.id
               if int(id) in RiZoeLX:
                   return await rizx.send_message("I can't raid on @RiZoeLX's Owner")
               elif int(id) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(id) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(id) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                   fname = k.first_name
                   fukname = f"[{fname}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        elif username.isnumeric():
            try:
               if int(username) in RiZoeLX:
                   return await rizx.send_message("I can't raid on @RiZoeLX's Owner")
               elif int(username) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(username) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(username) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                  id = int(username)
                  fukname = f"[{id}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        else:
            await rizx.send_message("Error! Send User ID or Username")
            return
        await rizx.send_message(SEND_COUNT)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        Num = res.message.message
        if Num.isnumeric():
             count = int(Num)
        else:
            await rizx.send_message("Error! Send Count in Numbers")
            return
        await rizx.send_message(SEND_SPAM)
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        message = res.message.message
        Fukoff = await rizx.send_message(f"__Starting Dm Spam On User {fukname}__")
        await asyncio.sleep(2)
        await Fukoff.edit(f"**▪️ Started DM Spam ▪️** \n\n__User__ : {fukname}\n__Spam Count__ : `{count}` \n__Spam Message__ : `{message}`")
        try:
           if Riz: 
                 for _ in range(count):
                        await Riz.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz2: 
                 for _ in range(count):
                        await Riz2.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz3: 
                 for _ in range(count):
                        await Riz3.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz4: 
                 for _ in range(count):
                        await Riz4.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz5: 
                 for _ in range(count):
                        await Riz5.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz6: 
                 for _ in range(count):
                        await Riz6.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz7: 
                 for _ in range(count):
                        await Riz7.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz8: 
                 for _ in range(count):
                        await Riz8.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz9: 
                 for _ in range(count):
                        await Riz9.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz10: 
                 for _ in range(count):
                        await Riz10.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz11: 
                 for _ in range(count):
                        await Riz11.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz12: 
                 for _ in range(count):
                        await Riz12.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz13: 
                 for _ in range(count):
                        await Riz13.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz14: 
                 for _ in range(count):
                        await Riz14.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz15: 
                 for _ in range(count):
                        await Riz15.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz16: 
                 for _ in range(count):
                        await Riz16.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz17: 
                 for _ in range(count):
                        await Riz17.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz18: 
                 for _ in range(count):
                        await Riz18.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz19: 
                 for _ in range(count):
                        await Riz19.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz20: 
                 for _ in range(count):
                        await Riz20.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz21: 
                 for _ in range(count):
                        await Riz21.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz22: 
                 for _ in range(count):
                        await Riz22.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz23: 
                 for _ in range(count):
                        await Riz23.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz24: 
                 for _ in range(count):
                        await Riz24.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz25: 
                 for _ in range(count):
                        await Riz25.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz26: 
                 for _ in range(count):
                        await Riz26.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz27: 
                 for _ in range(count):
                        await Riz27.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz28: 
                 for _ in range(count):
                        await Riz28.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz29: 
                 for _ in range(count):
                        await Riz29.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz30: 
                 for _ in range(count):
                        await Riz30.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz31: 
                 for _ in range(count):
                        await Riz31.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz32: 
                 for _ in range(count):
                        await Riz32.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz33: 
                 for _ in range(count):
                        await Riz33.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz34: 
                 for _ in range(count):
                        await Riz34.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz35: 
                 for _ in range(count):
                        await Riz35.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz36: 
                 for _ in range(count):
                        await Riz36.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz37: 
                 for _ in range(count):
                        await Riz37.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz38: 
                 for _ in range(count):
                        await Riz38.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz39: 
                 for _ in range(count):
                        await Riz39.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz40: 
                 for _ in range(count):
                        await Riz40.send_message(id, message)
                        await asyncio.sleep(0.3)
           
        except Exception as ex:
                print(ex)

@RiZoeL.on(events.NewMessage(pattern="[!/]dm"))
async def dm(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
          return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Username or ID of user to Start DM Spam**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        username = res.message.message
        if username.startswith("@"):
            try:
               k = await Riz.get_entity(username)
               id = k.id
               if int(id) in RiZoeLX:
                   return await rizx.send_message("I can't raid on @RiZoeLX's Owner")
               elif int(id) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(id) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(id) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                   fname = k.first_name
                   fukname = f"[{fname}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        elif username.isnumeric():
            try:
               if int(username) in RiZoeLX:
                   return await rizx.send_message("I can't raid on @RiZoeLX's Owner")
               elif int(username) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(username) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(username) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                  id = int(username)
                  fukname = f"[{id}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        else:
            await rizx.send_message("Error! Send User ID or Username")
            return
        await rizx.send_message("**Send Message For DM**")
        response = rizx.wait_event(events.NewMessage(chats=event.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await rizx.send_message(ABORT)
        message = res.message.message
        Fukoff = await rizx.send_message(f"__Sending Your Message To {fukname}__")
        await asyncio.sleep(2)
        await Fukoff.edit(f"**🔸 Message Delevered 🔸** \n\n__User__ : {fukname}\n__Message__ : `{message}`")
        try:
           if Riz: 
                    await Riz.send_message(id, message) 
           if Riz2: 
                    await Riz2.send_message(id, message) 
           if Riz3: 
                    await Riz3.send_message(id, message) 
           if Riz4: 
                    await Riz4.send_message(id, message) 
           if Riz5: 
                    await Riz5.send_message(id, message) 
           if Riz6: 
                    await Riz6.send_message(id, message) 
           if Riz7: 
                    await Riz7.send_message(id, message) 
           if Riz8: 
                    await Riz8.send_message(id, message) 
           if Riz9: 
                    await Riz9.send_message(id, message) 
           if Riz10: 
                    await Riz10.send_message(id, message) 
           if Riz11: 
                    await Riz11.send_message(id, message) 
           if Riz12: 
                    await Riz12.send_message(id, message) 
           if Riz13: 
                    await Riz13.send_message(id, message) 
           if Riz14: 
                    await Riz14.send_message(id, message) 
           if Riz15: 
                    await Riz15.send_message(id, message) 
           if Riz16: 
                    await Riz16.send_message(id, message) 
           if Riz17: 
                    await Riz17.send_message(id, message) 
           if Riz18: 
                    await Riz18.send_message(id, message) 
           if Riz19: 
                    await Riz19.send_message(id, message) 
           if Riz20: 
                    await Riz20.send_message(id, message) 
           if Riz21: 
                    await Riz21.send_message(id, message) 
           if Riz22: 
                    await Riz22.send_message(id, message) 
           if Riz23: 
                    await Riz23.send_message(id, message) 
           if Riz24: 
                    await Riz24.send_message(id, message) 
           if Riz25: 
                    await Riz25.send_message(id, message) 
           if Riz26: 
                    await Riz26.send_message(id, message) 
           if Riz27: 
                    await Riz27.send_message(id, message) 
           if Riz28: 
                    await Riz28.send_message(id, message) 
           if Riz29: 
                    await Riz29.send_message(id, message) 
           if Riz30: 
                    await Riz30.send_message(id, message) 
           if Riz31: 
                    await Riz31.send_message(id, message) 
           if Riz32: 
                    await Riz32.send_message(id, message) 
           if Riz33: 
                    await Riz33.send_message(id, message) 
           if Riz34: 
                    await Riz34.send_message(id, message) 
           if Riz35: 
                    await Riz35.send_message(id, message) 
           if Riz36: 
                    await Riz36.send_message(id, message) 
           if Riz37: 
                    await Riz37.send_message(id, message) 
           if Riz38: 
                    await Riz38.send_message(id, message) 
           if Riz39: 
                    await Riz39.send_message(id, message) 
           if Riz40: 
                    await Riz40.send_message(id, message) 
           
        except Exception as ex:
                print(ex)
