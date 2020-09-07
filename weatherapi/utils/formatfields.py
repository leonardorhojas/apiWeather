from datetime import datetime
import tzlocal



def unixtime_to_date(unix_timestamp, format_date):
    """
    Function to convert unixtime to human readable hour/date
    :param unix_timestamp:
    :param format_date:
    :return: human readable hour/date in H:M or Y-m-d  H:M: time/date format
    """
    # take TZ and format the date to datetimeformat
    local_timezone = tzlocal.get_localzone()
    date_timestamp = datetime.fromtimestamp(unix_timestamp, local_timezone)
    # check type of conversion date/hour
    date = ''
    if format_date == 'date':
        date = date_timestamp.strftime("%Y-%m-%d  %H:%M:%S")
    elif format_date == 'hour':
        date = date_timestamp.strftime("%H:%M")
    return date
