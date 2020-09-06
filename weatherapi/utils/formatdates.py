import tzlocal
from datetime import datetime


def unixtime_to_date(unix_timestamp, format_date):  # TBD to decorator
    local_timezone = tzlocal.get_localzone()
    date_timestamp = datetime.fromtimestamp(unix_timestamp, local_timezone)
    # check type of conversion DRY
    date = ''
    if format_date == 'date':
        date = date_timestamp.strftime("%Y-%m-%d  %H:%M:%S")
    elif format_date == 'hour':
        date = date_timestamp.strftime("%H:%M")
    return date
