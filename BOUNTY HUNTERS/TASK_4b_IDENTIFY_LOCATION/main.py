#! /usr/bin/env python

#read text file

from module.read_file import read_text_file
from find_location import find_location


text = read_text_file('./0-text.txt')
print("\n==================== starting test 0 ==\n")
result = find_location(text)

print(f'countries: {result[0]}, cities: {result[1]}, regions: {result[2]}')

