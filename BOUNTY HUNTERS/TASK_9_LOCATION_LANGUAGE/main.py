import sys
from find_language import get_local_language

try:
    location = input("Enter a geographical location: ")
    result = get_local_language(location)

    #official languages
    print("Official languages")
    print(result[0])
    print("Unofficial languages")
    print(result[1])

except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit(0)
