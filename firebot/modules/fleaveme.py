"""Emoji
Available Commands:
.fleave"""

import asyncio

from telethon import events

from firebot import CMD_HELP


@fire.on(events.NewMessage(pattern=r"\.fleave", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "fleave":

        await event.edit(input_str)

        animation_chars = [
            "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
            "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
            "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "**Chat Message Exported To** `./Inpu/`",
            "**Chat Message Exported To** `./Inpu/homework/`",
            "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
            "__Legend is leaving this chat.....! Gaand Marao Bc..__",
            "__Legend is leaving this chat.....! Gaand Marao Bc..__",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])


CMD_HELP.update(
    {
        "fleaveme": "**Fleaveme**\
\n\n**Syntax : **`.fleave`\
\n**Usage :** Prank plugin."
    }
)