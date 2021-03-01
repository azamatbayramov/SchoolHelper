from vkwave.bots import SimpleLongPollBot
from filters import NotGroupMemberFilter
from all_json import SETTINGS

bot = SimpleLongPollBot(tokens=SETTINGS["token"], group_id=SETTINGS["group_id"])


@bot.message_handler(NotGroupMemberFilter())
async def not_group_member_handler(event):
    return "Упс! Походу ты не подписан на группу. Подпишись и возвращайся"


bot.run_forever()
