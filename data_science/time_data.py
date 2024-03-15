'''Extract, convert and manage time data'''
from datetime import datetime


def seconds_2_date(time_seconds: int) -> datetime:
    '''Get date from the given Seconds'''
    d = datetime.fromtimestamp(time_seconds)
    return d.strftime('%d %b, %Y')
