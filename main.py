from vkwave.bots import SimpleLongPollBot
from all_json import SETTINGS

bot = SimpleLongPollBot(tokens=SETTINGS["token"], group_id=SETTINGS["group_id"])


# Test
@bot.message_handler()
def handle_message(event):
    return "Hello! I am bot!"


bot.run_forever()
