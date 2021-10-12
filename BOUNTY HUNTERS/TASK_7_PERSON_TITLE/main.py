import sys
from corrolate_title_person import correlate_person_title

try:
    person_name = input('Enter the name of a person: ')
    print(correlate_person_title(person_name))
except:
    error = sys.exc_info[0]
    print(error)
