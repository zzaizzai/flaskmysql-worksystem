import datetime


def time_now():
    now = datetime.datetime.now()
    d = now.strftime('%Y-%m-%d %H:%M:%S')
    return d 