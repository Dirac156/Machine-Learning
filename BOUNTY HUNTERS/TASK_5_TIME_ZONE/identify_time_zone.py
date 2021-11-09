import datetime
import datefinder


def get_date_mentionned(text: str):
    """ """
    matches = datefinder.find_dates(text)

    dates = []

    for match in matches:
        try:
            
            dates.append((datetime.datetime.strptime(str(match), "%Y %m %d %H:%M:%S %z")).isoformat(' '))
        except:
            dates.append((datetime.datetime.strptime(str(match), "%Y-%m-%d %H:%M:%S")).isoformat(' '))

    return dates
