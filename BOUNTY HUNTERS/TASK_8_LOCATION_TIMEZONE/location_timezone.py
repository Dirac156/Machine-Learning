# importing module
import datetime
import pytz
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from timezonefinder import TimezoneFinder

def find_location_data(location):
    """ Find the longitude and latitude of a certain location """
    gp = Nominatim(user_agent="timezoneLocation")
    
    try:
        return gp.geocode(location, timeout=None)
    except GeocoderTimedOut:
        return find_location_data(location)


def get_local_timezone(location_input: str):
    """ 
        get location, transform location to coordonate, get the timezone of the
        coordinate and translate it to GMT timezone 
    """
    # getting Latitude and Longitud
    location = find_location_data(location_input)

    x = datetime.datetime.now()

     # find the timezone assioated
    tf = TimezoneFinder()

    timeZone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    timeZ = pytz.timezone(timeZone).localize(
        datetime.datetime(x.year, x.month, x.day)).strftime('%z')


    # invert sign and return in 'Etc/GMT' format
    if timeZ[0] == '-':
        time_zone = 'GMT-' + timeZ[2]
    else:
        time_zone = 'GMT+' + timeZ[2]

    return timeZone, time_zone 
