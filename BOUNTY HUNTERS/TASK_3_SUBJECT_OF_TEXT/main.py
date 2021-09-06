#! /usr/bin/env python


from module.read_file import read_text_file
from identify_subject import identify_subject


text = read_text_file('./0-test.txt')
result = identify_subject(text)

print("\n==================== starting test 0 ==\n")
for key, value in result.items():
    print(f'*sentecnce* = {key} : *subject* = {value}')

print("== end Test == \n")

text = read_text_file('./1-test.txt')
result = identify_subject(text)

print("\n==================== starting test 1 ==\n")
for key, value in result.items():
    print(f'*sentecnce* = {key} : *subject* = {value}')

print("== end Test == \n")

text = read_text_file('./2-test.txt')
result = identify_subject(text)

print("\n==================== starting test 2 ==\n")
for key, value in result.items():
    print(f'*sentecnce* = {key} : *subject* = {value}')

print("== end Test == \n")
