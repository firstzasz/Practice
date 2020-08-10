

import random
answer = ['python', 'java', 'kotlin', 'javascript']
#answer = ['wlkdwwd', 'java']
answer = random.choice(answer)
#print(answer)
selected_answer = list(answer)
hide_answer = answer.replace(answer,str("-" * len(answer)))
#print(selected_answer)
print("H A N G M A N")
print()
print(hide_answer)
for _ in range(8):
    letter = input('input a letter:' + " > ")
    index_test = -1
    keep_index = list()
    for i in range(len(answer)):
        index_test = answer.find(letter,index_test + 1)
        if index_test != -1:
            keep_index.append(index_test)
    new_hint = list(hide_answer)
    for i in keep_index:
        new_hint.insert(i,str(letter))
        new_hint.pop(i + 1)
    hide_answer = ""
    for i in new_hint:
        hide_answer += i
    print()
    print(hide_answer)