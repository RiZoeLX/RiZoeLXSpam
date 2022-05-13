import os 
import asyncio
from telethon import events, Button, version
from datetime import datetime
from RiZoeLXSpam import ALIVE_PIC, rizoelversion, OWNER_ID
from RiZoeLXSpam import STRING, STRING2, STRING3, STRING4, STRING5 , STRING6, STRING7, STRING8, STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30, STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40
from telethon.tl.functions.users import GetFullUserRequest


btn = [
      [ 
      Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/RiZoeLX"),
      Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/DNHxHELL")
      ],
      [
      Button.url("• Source Code •", "https://GitHub.com/RiZoeLX/RiZoeLXSpam")
      ],
      [
      Button.inline("• Help And Commands •", data="help")
      ],
      ]


help_btn = [
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Pins", data="pins"), Button.inline("Pugres", data="purges")],
    [Button.inline("Locks", data="locks"), Button.inline("Misc", data="misc")],
    [Button.inline("Chat Cleaner", data="zombies")]]

      
HELP_TEXT = """
**Help Menu:**

**Available Modules Given Below Click On buttons To Know usage**

__Report Bugs At :__ **@DNHxHELL**

All cmd can be used with ! or /.
"""
 
ADMIN_TEXT = """
**• A module from which admins of the chat can use!**

‣ `/promote` - To Promote a user in the chat.
‣ `/demote` - To Demote a user in the chat.
‣ `/invitelink` - To get invitelink of a chat.
"""

BANS_TEXT = """
**• Some people need to be publicly banned; spammers, annoyances, or just trolls.**

‣ `/kickme` - To self Kick you from a chat.
‣ `/kick` - To kick someone from a chat.
‣ `/unban` - To unban a member from the chat.
‣ `/ban` - To Ban Someone from a chat.
‣ `/dban` - To delete the replied msg and bans the user.
‣ `/sban` - To delete the replied msg and kicks the user.
‣ `/skick` - To Delete Your msg and kicks the user 
‣ `/dkick` - To delete your msg and and kicks the replied user.
"""

CLEANER_HELP = """
**• This is A Module To Remove Deleted Accounts From Your Groups!**

‣ `/zombies` - To find zombies accounts in your chat.
‣ `/zombies clean` - To remove the deleted accounts from your chat.
"""


LOCKS_HELP = """
**• Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!**

‣ `/lock` - To lock a module in the chat.
‣ `/unlock` - To unlock a module in the chat.
‣ `/locktypes` - To get a list of modules can be locked
"""


MISC_HELP = """
**• An "odds and ends" module for small, simple commands which don't really fit anywhere.**

‣ `/id` - To get current chat id or replied user id.
‣ `/info` - To get info of a user.
"""


PINS_TEXT = """
**• All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!**

‣ `/pin` - To pinned a reply msg.
‣ `/unpin` - To Unpin the latest pinned msg.
‣ `/unpinall` - To unpinall all pinned msgs at once.
‣ `/pinned` - To get current pinned msg.

**Note:** __Add `notify` after ?pin to notify all chat members.__
"""


PR_HELP = """
**• Need to delete lots of messages? That's what purges are for!**

‣ `/purge` - Reply to a msg to delete msgs from there.
‣ `/spurge` - Same as purge, but doesnt send the final confirmation message.
‣ `/del` - Deletes the replied to message.
"""


#-------------------------------#---------------------------#-----------------------------#---------------------------#


@RiZoeL.on(events.NewMessage(pattern="[!/]start"))
async def start_all(event):

   if event.is_private:
      find_me = await event.client.get_me()
      bot_name = find_me.first_name
      bot_username = find_me.username
      replied_user = await event.client(GetFullUserRequest(event.sender_id))
      chat = event.chat_id
      firstname = replied_user.user.first_name
      id = replied_user.user.id
      start_owner = f"**Hello [{firstname}](tg://user?id={id}) My master !!**\n I'm Spam Your Spam assistant Bot You can Control Your Spam userbots using me \n\n __Send /help or !help for more info__"
      start_sudo = f"**Hello [{firstname}](tg://user?id={id}) Sudo !!** \n I'm {bot_name} A Spam Assistant bot \n\n __Send /help or !help for more info__"
      start_users = f"**Hello [{firstname}](tg://user?id={id}) !!** \n I'm {bot_name} A Spam Assistant bot Assistant bot \n\n __click Below Buttons for more info__"
      if event.sender_id == OWNER_ID or event.sender_id in DEV:
          await RiZoeL.send_message(chat, start_owner, buttons=btn)
      elif event.sender_id in SUDO_USERS:
          await RiZoeL.send_message(chat, start_sudo, buttons=btn)
      else:
          await RiZoeL.send_message(chat, start_users, buttons=btn)
          return
   if event.is_group:
       await event.reply("**I am alive 24/7!**")
       return


@RiZoeL.on(events.callbackquery.CallbackQuery(data="help"))
async def Help_cmds_(event):
       await event.edit(HELP_TEXT, buttons=help_btn)


@RiZoeL.on(events.callbackquery.CallbackQuery(data="admin"))
async def admin(event):
    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


@RiZoeL.on(events.callbackquery.CallbackQuery(data="bans"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


@RiZoeL.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


@RiZoeL.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):
    await event.edit(LOCKS_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])
 
 
@RiZoeL.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


@RiZoeL.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):
    await event.edit(PINS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


@RiZoeL.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

  
#-------------------------------#---------------------------#-----------------------------#---------------------------#



RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"

        
@RiZoeL.on(events.NewMessage(pattern="[!/]ping"))
async def Botping(e):
   if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000              
        pingop = f"๏ sᴘᴀᴍ X ᴀssɪsᴛᴀɴᴛ ๏\n\n ᴘᴏɴɢ: `{ms}` ᴍs \n ᴠᴇʀsɪᴏɴ: {rizoelversion}" 
        await fuk.edit(pingop)
        


@RiZoeL.on(events.NewMessage(pattern="[!/]alive"))
async def alive(event):
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
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
           Caption = f"**RɪZᴏᴇL X Sᴘᴀᴍ Hᴇʀᴇ.** \n\n"
           Caption += f"━━━━━━━━━ × ━━━━━━━━━┑\n"
           Caption += f"• **RiZoeLXSpam Vr:** `{rizoelversion}` \n"
           Caption += f"• **Python Vr:** `3.10.4` \n"
           Caption += f"• **Telethon Vr:** `{version.__version__}` \n"
           Caption += f"• **Master:** [{OWNER_ID}](tg://user?id={OWNER_ID}) \n"
           Caption += f"• **Active IDs:** `{ids}` \n"
           Caption += f"━━━━━━━━━ × ━━━━━━━━━┙\n"
           await RiZoeL.send_file(event.chat_id, 
                                RIZ_PIC, 
                                caption=Caption, 
                                buttons=[
           [
           Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/RiZoeLX"),
           Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/DNHxHELL")
           ], 
           ], 
           )        
        except Exception as ex:
           Caption = f"**RɪZᴏᴇL X Sᴘᴀᴍ Hᴇʀᴇ.** \n\n"
           Caption += f"━━━━━━━━━ × ━━━━━━━━━┑\n"
           Caption += f"• **RiZoeLXSpam Vr:** `{rizoelversion}` \n"
           Caption += f"• **Python Vr:** `3.10.4` \n"
           Caption += f"• **Telethon Vr:** `{version.__version__}` \n"
           Caption += f"• **Master:** [{OWNER_ID}](tg://user?id={OWNER_ID}) \n"
           Caption += f"━━━━━━━━━ × ━━━━━━━━━┙\n"
           await RiZoeL.send_file(event.chat_id, 
                                RIZ_PIC, 
                                caption=Caption, 
                                buttons=[
           [
           Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/RiZoeLX"),
           Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/DNHxHELL")
           ], 
           ], 
           )

@RiZoeL.on(events.NewMessage(pattern="[!/]restart"))
async def restart(event):
  if event.sender_id in DEV:
     text = "**• Restarting •**"
     await event.reply(text, parse_mode=None, link_preview=None )
     try:
        await RiZoeL.disconnect()
     except Exception:
        pass
     os.execl(sys.executable, sys.executable, *sys.argv)
     quit()
    
  if event.sender_id in SUDO_USERS:
        await event.reply("**Sorry !! You can't Use this Cmd only Owner and Full Sudo Users can**")
       
