""" commands: .tspam text """
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="tspam"))
async def tmeme(e):
     tspam = str(e.text[7:])
     message = tspam.replace(" ", "")
     for letter in message:
         await e.respond(letter)
     await e.delete()
