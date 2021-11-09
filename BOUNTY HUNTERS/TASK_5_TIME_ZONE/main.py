from identify_time_zone import get_date_mentionned
from extract_time_zone import extract_time_zone
from module.read_file import read_text_file

text = read_text_file('text.txt')

result = get_date_mentionned(text)

date = "2016-04-15T08:27:18-0500"

result2 = extract_time_zone(date)

print(result)

print(result2)
