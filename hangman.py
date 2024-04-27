import random   

import pyfiglet
  

# Word chosen at random from list. 
#words = [ "sunflower" , "tulip" , "rose" , "lily" , "jasmine" , "poppy"]
#words = ['red','pi']

print(pyfiglet.figlet_format("Hangman"))

print("You chose Hangman!")
print("Here are the rules for easy level: We will give you a word with missing letters, and you have to guess the letters!")
print()
print("You can only guess wrong 5 times for the easy level and 10 times for the hard level")

while True:

    '''with open("easy.txt", "r") as file:
    data = file.read()
    words = data.split()
    
    # Generating a random number for word position
    word_pos = random.randint(0, len(words)-1)
    x = words[word_pos]'''


    print("Would you like the easy level or hard level?")
    y = input()
    if y == 'easy':
        f = open("easy.txt","r")
    elif y=='hard':
        f = open("hard.txt")
    else:
        print("Invalid entry. You can only enter easy or hard.")
        break

    l = f.read()
    words = l.split()
    pos= random.randint(0,len(words))
    x= words[pos]
    Z=[*range(0,len(x))]



    # word is split into letters, and letters put into a list. list name is missing

    missing=[]  
    for i in range(len(x)):
        missing.append(x[i])



    # another list with same size as missing is made which is only filled with *. 
    b=[]

    for i in range(0,len(x)):
        b.append('*')


    # the number of missing letters will be blank. this is precoded by me. it will be the length //2

    blank = len(x)//2

    for i in range(0,blank):
        z= random.choice(Z)           
        Z.remove(z)
        b[z]=missing[z]
        missing[z] = "*" 


    #this is the loop we have to remove letters in random. 
    # happens 'blank' no. of times
    # key is random no. from the length of word
    # the letters u take out of missing, put in it b.
    # once letter removed from b, replace it with *
    # and in b replace * with letter
    # note: the indexes of b and missing should be the same; that is a * in missing corresponds to letter in b

    # b is basiclly thr answer list, with *
    # missing is question list, with * 

    '''for i in range(0,blank):
        key = random.randrange(0,len(x))
        if missing[key] != "*":                
            b[key] = missing[key]
            missing[key] = "*"
    '''



    # *missing puts all the letter in one word
    print("Welcome to Hangman! Here is the word:")
    print(*missing)



    # take input
    #if input is in b--i.e, the answer list, then replace that element in b with * . find index of the element in b. 
    #index in b = index in missing
    #so missing[index] = letter inputted
    #missing has * removed and correct letter
    #if letter is repeated multiple times- for that put it in while loop which runs till input letter is in list b


    A=0
    if y == 'easy':
        while A<5:
            if b.count('*') == len(x):
                print("You won! Congrats:)")
                break
            else:
                y = input("Enter letter: ")
                if y in b:
                    while y in b:
                        index=b.index(y)
                        missing[index] = y
                        b[index] = '*'
                    print(*missing)
                    
                    
                else:
                    if A==4:
                        print("You have used up all your tries:(  the correct answer was",x,"better luck next time!")
                        break
                    else :
                        print("Wrong! Try again")
                        A=A+1
    else:
        while A<8:
            if b.count('*') == len(x):
                print("You won! Congrats:)")
                break
            else:
                y = input("Enter letter: ")
                if y in b:
                    while y in b:
                        index=b.index(y)
                        missing[index] = y
                        b[index] = '*'
                    print(*missing)
                    
                    
                else:
                    if A==7:
                        print("You have used up all your tries:( The correct answer was",x, "better luck next time!")
                        break
                    else :
                        print("Wrong! Try again")
                        A=A+1
        

    x = input("Would you like to try this game again with the hard level? (y for yes, n for no)")
    if x == 'n':
        break
    elif x=='y':
        True
    else:
        "Invalid"
        break