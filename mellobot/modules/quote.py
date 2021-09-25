from quote import quote

from firebot import CMD_HELP
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="qs (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    result = quote(input_str, limit=3)
    sed = ""

    for quotes in result:
        sed += str(quotes["quote"]) + "\n\n"

    await event.edit(
        f"<b><u>Quotes Successfully Gathered for given word </b></u><code>{input_str}</code>\n\n\n<code>{sed}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "quotes": "**Quotes**\
\n\n**Syntax : **`.qs <text>`\
\n**Usage :** Automatically gets quotes for given plugin."
    }
)
