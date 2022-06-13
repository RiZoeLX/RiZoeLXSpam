import os
from RiZoeLXSpam import OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY
from telethon import events
import heroku3

heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)
fullsudo = os.environ.get("FULLSUDO", None)
ABORT = "**All Process Cancelled ❌**"

@RiZoeL.on(events.NewMessage(pattern="[!/]addsudo"))
async def add_sudo(event):
  if event.sender_id in DEV:
     if event.is_group:
          return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        if HEROKU_API_KEY:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
        else:
            rizx.send_message("**Error !!** \n\n Please Setup Your `HEROKU_API_KEY` than try again")
        rizoel = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await rizx.send_message("**Error !!** \n\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        await rizx.send_message("**Send Username or User id Of user To add in Sudo user**")
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
                   return await rizx.send_message("I Can't Add @RiZoeLX's Owner As a Sudo")
               elif int(id) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(id) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(id) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                   fname = k.first_name
                   nname = f"[{fname}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        elif username.isnumeric():
            try:
               if int(username) in RiZoeLX:
                   return await rizx.send_message("I Can't Add @RiZoeLX's Owner As a Sudo")
               elif int(username) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(username) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(username) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                  id = int(username)
                  nname = f"[{id}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        else:
            await rizx.send_message("Error! Send User ID or Username")
            return
        ok = await rizx.send_message(f"__Adding {id} As A Sudo Users__")
        if sudousers:
            newsudo = f"{sudousers} {id}"
        else:
            newsudo = f"{id}"
        await ok.edit(f"**⚜️ New Sudo Added** \n\n User: {nname} \n User ID: {id} \n\n Wait until Restart !! ")
        heroku_var[rizoel] = newsudo
  elif event.sender_id in SUDO_USERS:
         await event.reply("**Kid !! Only Owner and Full Sudo Users Can Add Sudos**")

@RiZoeL.on(events.NewMessage(pattern="[!/]fullsudo"))
async def full_sudo(event):
  if event.sender_id == OWNER_ID or event.sender_id == 1517994352:
     if event.is_group:
          return await event.reply("**Use This Cmd In PM**")
     async with RiZoeL.conversation(event.chat_id) as rizx:
        if HEROKU_API_KEY:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
        else:
            rizx.send_message("**Error !!** \n\n Please Setup Your `HEROKU_API_KEY` than try again")
        rizoel = "FULLSUDO"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await rizx.send_message("**Error !!** \n\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        await rizx.send_message("**Send Username or User id Of user To add in Full Sudo user**")
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
                   return await rizx.send_message("I Can't Add @RiZoeLX's Owner As a Sudo")
               elif int(id) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(id) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(id) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                   fname = k.first_name
                   nname = f"[{fname}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        elif username.isnumeric():
            try:
               if int(username) in RiZoeLX:
                   return await rizx.send_message("I Can't Add @RiZoeLX's Owner As a Sudo")
               elif int(username) == OWNER_ID:
                   return await rizx.send_message("This guy is Owner Of this Bots.")
               elif int(username) in DEV:
                   return await rizx.send_message("This guy is a Full sudo user.")
               elif int(username) in SUDO_USERS:
                   return await rizx.send_message("This guy is a sudo user.")
               else:
                  id = int(username)
                  nname = f"[{id}](tg://user?id={id})"
            except Exception as ex:
                await rizx.send_message(f"**Error!** \nln {str(ex)}")
                return
        else:
            await rizx.send_message("Error! Send User ID or Username")
            return
        ok = await rizx.send_message(f"__Adding {id} As A Full Sudo Users__")
        if fullsudo:
            newsudo = f"{fullsudo} {id}"
        else:
            newsudo = f"{id}"
        await ok.edit(f"**🔱 Full Sudo Added** \n\n User: {nname} \n User ID: {id} \n\n Wait until Restart !! ")
        heroku_var[rizoel] = newsudo
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
         await event.reply("**Kid !! Only Owner Can Add Full Sudos**")
