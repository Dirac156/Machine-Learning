import sys
from location_timezone import get_local_timezone

try:
    location = input("Enter the name of the place you want to know the timezone: ")
    
    result = get_local_timezone(location)

    print(result)

except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit(0)
