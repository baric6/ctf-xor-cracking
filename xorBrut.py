#by baric

#this gens random words and xor them to get the correct password 

#need pw len 11
#first letter is ascii 78 == captial "N"
#xor == 12645638

import random


while True:

    #gen random word
    ##################################################################################
    word = []
    word.append(chr(78))
    for i in range(10):

        word.append(chr(random.randint(40,122)))

    password =  ''.join(word) 
    ##################################################################################

    #xor word
    ##################################################################################
    builder = 0
    for c in password:
        builder += ord(c)

    builder = builder << 2
    builder = ~builder
    builder = builder ^ 12648430
    builder = ~builder
    if builder == 12645638 and ord(password[0]) == 78 and len(password) == 11:
        print('\ncorrect')
        print("\nPASSWORD: "+''.join(word)+"\n")
        break
    else:
        print(str(builder) + " :: " + ''.join(word))
        word.clear()
    ###################################################################################
    


    

    

    


