import datetime


def extract_time_zone(date_str: str):
    """ """

    date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")

    # get timezone informations
    tz = date.tzinfo
    # get timezone name
    tzinfo = tz.tzname(date)

    return tzinfo
