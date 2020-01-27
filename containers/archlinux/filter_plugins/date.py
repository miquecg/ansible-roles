from datetime import timedelta
from functools import reduce, wraps

def formatted(func):
    @wraps(func)
    def date_with_format(*args, **kwargs):
        format = kwargs.pop('fmt', '%Y-%m-%d')
        date = func(*args, **kwargs)
        return date.strftime(format)

    return date_with_format

@formatted
def move_date(date, months_back=0):
    new_month = change_month(date, months_back)
    return change_day_to_first(new_month)

def change_month(date, months_back):
    times = max(0, months_back)
    return reduce(lambda new_date, _: change_day_to_first(new_date) - timedelta(days=1), range(times), date)

def change_day_to_first(date):
    return date.replace(day=1)

class FilterModule(object):

    def filters(self):
        return {
            'day_one': move_date
        }
