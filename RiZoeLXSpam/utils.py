from RiZoeLXSpam import (Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, Riz21, Riz22, Riz23, Riz24, Riz25, Riz26, Riz27, Riz28, Riz29, Riz30, Riz31, Riz32, Riz33, Riz34, Riz35, Riz36, Riz37, Riz38, Riz39, Riz40, DEV, SUDO_USERS, hl, RiZoeL)
import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re


def load_plugins(shortname):
        path = Path(f"RiZoeLXSpam/plugins/{shortname}.py")
        name = "RiZoeLXSpam.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Riz = Riz
        mod.logger = logging.getLogger(shortname)
        # auto-load
        mod.RiZoeL = RiZoeL
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
        mod.hl = hl
        mod.DEV = DEV
        mod.SUDO_USERS = SUDO_USERS
        # support for paperplaneextended
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["RiZoeLXSpam.plugins." + shortname] = mod
        print("• RiZoeLXspam Successfully imported:  " + shortname)


async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)



def Start_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Checking Bot Token......")
        print("Starting Bot")
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.RiZoeL = RiZoeL
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
        sys.modules["RiZoeLXSpam.assistant" + shortname] = mod


def load_Assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/plugins/{shortname}.py")
        name = "RiZoeLXSpam.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("> Loading Spam Assistant <")
        print("XSpam Assistant " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"RiZoeLXSpam/assistant/plugins/{shortname}.py")
        name = "RiZoeLXSpam.assistant.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.RiZoeL = RiZoeL
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
        sys.modules["RiZoeLXSpam.assistant.plugins." + shortname] = mod
        print("XSpam Assistant  " + shortname)
