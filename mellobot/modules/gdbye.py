"""Emoji
Available Commands:
.gdbye"""


import asyncio

from uniborg.util import fire_on_cmd

from firebot import CMD_HELP


@fire.on(fire_on_cmd(pattern=r"gdbye"))
async def _(event):

    animation_interval = 2
    animation_ttl = range(0, 11)

    await event.edit("Thanks for contacting me..\n I'm Going to leave now...")
    animation_chars = [
        "**Bye  🙏\n Ending this chat 😒**",
        "**I'm leaving this chat now  🙏**",
        "You can again contact me anytime you like",
        "Please Don't forget to join @MELLOLAB our group",
        "**Have a Good Day.. **",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


CMD_HELP.update(
    {
        "gdbye": "**Good Bye**\
\n\n**Syntax : **`.gdbye `\
\n**Usage :** A nice way to say good bye"
    }
)
