""" Command: .ping """

from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ping ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply("PiNgGg! : Calculating...")
    end = datetime.now()
    ms = (end - start).microseconds / 100000
    await mone.edit("‎‎‎‎‎‎‎‎‎PoNgGg!  : {} ms".format(ms))
 
