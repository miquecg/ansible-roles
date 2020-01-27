from datetime import timedelta
from functools import reduce, wraps
from itertools import chain, repeat

def formatted(func):
    @wraps(func)
    def date_with_format(*args, **kwargs):
        format = kwargs.pop('fmt', '%Y-%m-%d')
        date = func(*args, **kwargs)
        return date.strftime(format)

    return date_with_format

@formatted
def move_date(date, month=0):
    if month <= 0:
        times = abs(month)
        steps = backwards_month_iterator(times)
        return reduce(lambda new_date, step_back: step_back(new_date), steps, date)

def back_to_first_day(date):
    return date.replace(day=1)

def subtract_one_day(date):
    return date - timedelta(days=1)

def backwards_month_iterator(times):
    funcs = chain([[back_to_first_day]], repeat([subtract_one_day, back_to_first_day], times))
    return chain.from_iterable(funcs)

class FilterModule(object):

    def filters(self):
        return {
            'day_one': move_date
        }
