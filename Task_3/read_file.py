
import sys
import _json

from pprint import pprint


list_file = ['1_story.txt', '2_story.txt', '3_story.txt']
amount_lines_list = [] # Создание копии
for one_file in list_file:
    with open(one_file, 'rt', encoding='utf8') as file:
        first_line = one_file
        text = file.readlines()
        len_text = len(text)
        amount_lines_list.append(len_text)
print(sorted(amount_lines_list))
with open('4_story.txt', 'a', encoding='utf8') as file:
    print(amount_lines_list)

    file.write(first_line)
    file.write(len_text)
