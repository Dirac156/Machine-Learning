#! /usr/bin/env python


from module.read_file import read_text_file
from part_of_speech import part_of_speech


text = read_text_file('./0-test.txt')
result = part_of_speech(text)

print("\n==================== starting test 0 ==\n")
for item in result:
    print(f'{item[0]} : {item[1]}')

print("== end Test == \n")

text = read_text_file('./1-test.txt')
result = part_of_speech(text)

print("\n==================== starting test 1 ==\n")
for item in result:
    print(f'{item[0]} : {item[1]}')

print("== end Test == \n")

text = read_text_file('./2-test.txt')
result = part_of_speech(text)

print("\n==================== starting test 2 ==\n")
for item in result:
    print(f'{item[0]} : {item[1]}')

print("== end Test == \n")
