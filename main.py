from vkwave.bots import SimpleLongPollBot
from all_json import SETTINGS

bot = SimpleLongPollBot(tokens=SETTINGS["token"], group_id=SETTINGS["group_id"])

