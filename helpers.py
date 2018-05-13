from datetime import datetime

DATETIME_TEMPLATES = {
    'datetime': '%b %d, %Y %H:%M:%S',
    'date': '%d/%m/%Y',
    'time': '%H:%M:%S'
}


def str2date(str_date, date_type='date'):
    if not str_date:
        return None
    return datetime.strptime(str_date, DATETIME_TEMPLATES[date_type])


def tstamp2date(tstamp):
    if not tstamp:
        return None
    return datetime.fromtimestamp(int(str(tstamp).lstrip('0')[:10]))


def date2str(date, date_type='date'):
    if not date:
        return None
    return date.strftime(DATETIME_TEMPLATES[date_type])
