import random
answer = ['python', 'java', 'kotlin', 'javascript']
#answer = ['wlkdwwd', 'java']
typed_input = {''}
answer = random.choice(answer)
#print(answer)
selected_answer = list(answer)
hide_answer = answer.replace(answer,str("-" * len(answer)))
#print(selected_answer)
print("H A N G M A N\n")
# print(hide_answer)
count = 0
while count == 0:
    # ask if player want to play
    play_exit = input('Type "play" to play the game, "exit" to quit:')
    if play_exit == 'play':  
        while count <= 7:
        #for z in range(8):
            print()
            print(hide_answer)
            letter = input('Input a letter:')
            index_test = -1
            keep_index = list()
            if len(letter) > 1:
                        print("You should input a single letter")
                        #count += 1 not count for this falut
                        continue
            if letter.islower() == False:
                        print("It is not an ASCII lowercase letter")
                        #count += 1 not count for this falut
                        continue
            if letter in typed_input:
                        print("You already typed this letter")
                        #count += 1 not count for this falut
                        continue
            typed_input.add(letter) #add all typed letter to this set
            if answer.find(letter,0) == -1:
                        print("No such letter in the word")
                        count += 1
                        continue
            if hide_answer == answer:
                        print("You guessed the word!")
                        print("You survived!")
                        break
            #elif hide_answer.find(letter,0) != -1:
                        #print("You already typed this letter")      # to check if input same letter as its already in
                        #count += 1
                        #continue
            for i in range(len(answer)):
                        index_test = answer.find(letter,index_test + 1)
                        if index_test != -1:
                                    keep_index.append(index_test)
            new_hint = list(hide_answer)
            for j in keep_index:
                        new_hint.insert(j,str(letter))
                        new_hint.pop(j + 1)
            hide_answer = ""
            for k in new_hint:
                        hide_answer += k
            print()
            #print(hide_answer)
        else:
            print("You are hanged!")
            #print("Thanks for playing!")
    #print("We'll see how well you did in the next stage")
    #print(typed_input)
    elif play_exit == "exit":
        break
