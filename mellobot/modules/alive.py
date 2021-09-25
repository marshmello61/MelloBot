"""Check if firebot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from telethon import version
from uniborg.util import fire_on_cmd, sudo_cmd

from firebot import ALIVE_NAME, CMD_HELP, Lastupdate
from firebot.Configs import Config
from firebot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MelloBot"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "__**// Project MelloBot running //**__\n\n"

pm_caption += f"**==============================**\n\n"
pm_caption += f"`User:` **{DEFAULTUSER}**\n\n"
pm_caption += f"**=========== Info =============**\n"
pm_caption += f"**=**`Telethon:` `{version.__version__}` \n"
pm_caption += f"**=**`Version:` `{currentversion}`\n"
pm_caption += f"**=**`Uptime:` `{uptime}`\n"
pm_caption += f"**=**`Support:` [Join](https://t.me/MelloLab)\n"
pm_caption += f"**==============================**\n"
pm_caption += f"// Security by Project MelloBot\n"
pm_caption += " [Github](https://github.com/marshmello61/MelloBot) • [Group](https://t.me/MelloHub)"


@fire.on(fire_on_cmd(pattern=r"start"))
@fire.on(sudo_cmd(pattern=r"start", allow_sudo=True))
async def chris(alive):
    await alive.get_chat()
    """ For .start command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "start": "**Start**\
\n\n**Syntax : **`.start`\
\n**Usage :** Check if Project MelloBkt is running"
    }
)
