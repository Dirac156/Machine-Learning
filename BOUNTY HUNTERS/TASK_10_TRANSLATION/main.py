from module.read_file import read_text_file
from translate_mistranslated import translate
from auto_correct_w import correct_word

text = read_text_file('text.txt')
result = translate(text)

print(text)
print("===")
print(result)

result_c = correct_word(result)

print("final_result: ", result_c)