import os 
import asyncio
import random
from telethon import events
from datetime import datetime
from telethon.tl import functions
from resources.data import RAID, REPLYRAID, RiZoeLX, GRP
from RiZoeLXSpam import OWNER_ID

SEND_GRP = "**Send Group Link Where You want to start raid**"
SEND_COUNT ="**Send Counts**"
ABORT = "**All process Cancelled !**"      
        
@RiZoeL.on(events.NewMessage(pattern="[!/]raid"))
async def raid(event):
   if event.sender_id in DEV or event.sender_id in SUDO_USERS:
          await event.reply("**We'll Add This Cmd Soon.**")
          
#======== Dm Raid =========#

@RiZoeL.on(events.NewMessage(pattern="[!/]dmraid"))
async def dm_raid(event):
  if event.sender_id in DEV or event.sender_id in SUDO_USERS:
     if event.is_group:
          return await event.reply("**Use this Cmd in PM !!**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        await rizx.send_message("**Send Username or ID of user to activate raid**")
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
                   raidname = f"[{fname}](tg://user?id={id})"
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
                  raidname = f"[{id}](tg://user?id={id})"
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
        text = f"**☣️ Dm Raid Started ☣️** \n\n\n__Riad Count__ : `{count}` \n__Dm Raid User__ : {raidname}"
        hehe = await rizx.send_message("__Starting Dm Raid__")
        await asyncio.sleep(3)
        await hehe.edit(text)
        try:
           if Riz:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz2:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz2.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz3:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz3.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz4:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz4.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz5:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz5.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz6:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz6.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz7:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz7.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz8:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz8.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz9:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz9.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz10:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz10.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz11:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz11.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz12:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz12.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz13:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz13.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz14:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz14.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz15:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz15.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz16:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz16.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz17:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz17.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz18:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz18.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz19:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz19.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz20:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz20.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz21:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz21.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz22:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz22.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz23:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz23.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz24:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz24.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz25:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz25.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz26:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz26.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz27:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz27.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz28:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz28.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz29:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz29.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz30:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz30.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz31:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz31.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz32:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz32.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz33:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz33.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz34:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz34.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz35:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz35.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz36:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz36.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz37:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz37.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz38:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz38.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz39:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz39.send_message(id, message)
                        await asyncio.sleep(0.3)
           if Riz40:
                 message = random.choice(RAID)
                 for _ in range(count):
                        await Riz40.send_message(id, message)
                        await asyncio.sleep(0.3)
           
        except Exception as ex:
                print(ex)
