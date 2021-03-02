from all_json import SCHEDULE
import datetime

LESSON = 0
BREAK = 1


class Period:
    def __init__(self, number, start_time, finish_time, period_type):
        self.number = number
        self.start_time = start_time
        self.finish_time = finish_time
        self.period_type = period_type

    def check_time(self, time):
        if self.start_time <= time <= self.finish_time:
            return True
        else:
            return False


def get_period_list(schedule_file):
    period_list = []

    for period_j in schedule_file["schedule"]["lessons"] + schedule_file["schedule"]["breaks"]:
        start_time = datetime.time(hour=period_j["time"]['start']['hour'],
                                   minute=period_j["time"]['start']['minute'])
        finish_time = datetime.time(hour=period_j["time"]['finish']['hour'],
                                    minute=period_j["time"]['finish']['minute'])
        if period_j in schedule_file["schedule"]["lessons"]:
            period = Period(period_j['number'], start_time, finish_time, LESSON)
        elif period_j in schedule_file["schedule"]["breaks"]:
            period = Period(period_j['number'], start_time, finish_time, BREAK)

        period_list.append(period)

    return period_list


PERIODS = get_period_list(SCHEDULE)


def get_period(time):
    for period in PERIODS:
        if period.check_time(time):
            return period
    return False


def get_time_to_period_finish(time, period):
    finish_time = datetime.datetime(1, 1, 1, period.finish_time.hour, period.finish_time.minute, 1)
    time = datetime.datetime(1, 1, 1, time.hour, time.minute, 1)
    remaining_time = finish_time - time
    return remaining_time


def get_now_time():
    now_time = datetime.datetime.utcnow().time()
    now_hour = (now_time.hour + 5) % 24
    now_time = datetime.time(hour=now_hour, minute=now_time.minute, second=now_time.second)

    return now_time
