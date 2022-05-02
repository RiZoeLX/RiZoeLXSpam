#RiZoeLXSpam By @TheRiZoeL

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from RiZoeLXSpam.utils import load_plugins, load_Assistant, Start_Assistant
import logging
from telethon import events
from . import RiZoeL, Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, BOT_TOKEN, OWNER_ID, hl, loop
from . import STRING, STRING2, STRING3, STRING4, STRING5 , STRING6, STRING7, STRING8, STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30, STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40
from telethon.tl import functions


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

if BOT_TOKEN:
    print("Setting up Assisting Bot")
    path = "RiZoeLXSpam/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            Start_Assistant(shortname.replace(".py", ""))


if BOT_TOKEN:
    path = "RiZoeLXSpam/assistant/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_Assistant(shortname.replace(".py", ""))
    print("Assisting Bot set up completely!")


async def logss():
     owner = int(OWNER_ID)
     Log_msg = "**🔶 RiZoeL X Spam Started 🔶 **\n\n"
     Log_msg += f"• **Owner:** [{owner}](tg://user?id={owner}) \n"
     if BOT_TOKEN:
        Findme = await RiZoeL.get_me()
        Name = Findme.first_name
        username = Findme.username
      #  id = telethon.utils.get_peer_id(Findme)
       # XX.append(id)
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
        await Riz(functions.channels.JoinChannelRequest(channel="@RiZoeLXSpam_Logs"))
        await Riz.send_message(-1001647867895, Log_msg)
        await Riz(LeaveChannelRequest(-1001647867895))
     except Exception as ex:
        print(ex)
        pass

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
