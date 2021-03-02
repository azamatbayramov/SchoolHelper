from vkwave.bots import SimpleLongPollBot
from filters import NotGroupMemberFilter
from all_json import SETTINGS
import periods

bot = SimpleLongPollBot(tokens=SETTINGS["token"], group_id=SETTINGS["group_id"])


@bot.message_handler(NotGroupMemberFilter())
async def not_group_member_handler(event):
    return "Упс! Походу ты не подписан на группу. Подпишись и возвращайся :)"


@bot.message_handler()
async def main_handler(event):
    now_time = periods.get_now_time()
    period = periods.get_period(now_time)
    if period:
        remaining_time = periods.get_time_to_period_finish(now_time, period)
        if period.period_type == periods.LESSON:
            text = f"""Сейчас {period.number} урок.\nДо звонка {remaining_time.seconds // 60} минут."""
        elif period.period_type == periods.BREAK:
            text = f"""Сейчас перемена.\nСледующий урок {period.number + 1}-й.\nДо звонка {remaining_time.seconds // 60} минут."""

        return text
    else:
        return "До уроков еще далеко :)"


bot.run_forever()
