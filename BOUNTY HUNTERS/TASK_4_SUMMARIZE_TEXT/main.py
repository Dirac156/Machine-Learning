#! /usr/bin/env python


from module.read_file import read_text_file
from summarize_text import summarize_text


text = read_text_file('./0-test.txt')
result = summarize_text(text)

print("\n==================== starting test 0 ==\n")
print(f'{result}')

print("== end Test == \n")

text = read_text_file('./1-test.txt')
result = summarize_text(text)

print("\n==================== starting test 1 ==\n")
print(f'{result}')

print("== end Test == \n")

text = read_text_file('./2-test.txt')
result = summarize_text(text)

print("\n==================== starting test 2 ==\n")
print(f'{result}')

print("== end Test == \n")
