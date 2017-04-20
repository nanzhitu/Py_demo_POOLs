#encoding=utf-8
import types

char_list =[]

file_object = open('log.txt')
output = open('data.txt', 'w')
match = open('match.txt')
i = 0;

try:
    for line_match in match:
        if str(line_match.strip()) != '':
            char_list.append(line_match.strip())
    print char_list
finally:       
    match.close()

num = len(char_list)
try:
    for line in file_object:
        for match_i in range(num):
            if line.find(char_list[match_i]) != -1:
                output.write(line)
                break;
       
finally:
    file_object.close()
    output.close()
     
