import random
print ("Welcome to HANG == MAN")

levels = 0
lives = 0

while True:
    x = input ("Pls choose your level: 1 for rookie(6 lives) or 2 for expert(3 lives). \n")
    if x == ("1"):
        levels = 1
        lives = 6
        print ("You choose the rookie level, with 6 lives!")
        break
    
    if x == ("2"):
        levels = 2
        lives = 3
        print ("You choose the expert level, with 3 lives!")
        break
    if x == ("quit"):
        print("Good Bye!")
        break
    else:
        print("Pls choose a valid operator!")

def pick_a_random():
    with open("countries.txt") as f:
        word_list = []

    print(random.choice(open('countries.txt').read().split()).strip()) #by anandskumar, thx :)



while True:
    if ((level == 2) and (lives == 3)) or ((level == 1) and ((lives ==6) or (lives == 5))):
	    print("_________")
	    print("|	 |  ")
	    print("|        ")
	    print("|        ")
	    print("|        ")
	    print("|        ")
	    print("|________")
    elif ((level == 2) and (lives == 2)) or ((level == 1) and ((lives == 4) or (lives == 3))):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|")
	    print ("|")
	    print ("|")
	    print ("|________")
    elif ((level == 2) and (lives == 1)) or ((level == 1) and ((lives ==2) or (lives == 1))):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	 |")
	    print ("|	 |")
	    print ("|")
	    print ("|________")
    elif ((level == 2) and (lives == 3)) or ((level == 1) and ((lives == 6) or (lives == 5))):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|")
	    print ("|	 |")
	    print ("|        ")
	    print ("|________")
    elif ((level == 2) and (lives == 2)) or ((level == 1) and ((lives ==4) or (lives == 3))):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|")
	    print ("|________")
    elif ((level == 2) and (lives == 1)) or ((level == 1) and (lives == 2)):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|	/ ")
	    print ("|________")
    elif (lives == 0):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|	/ \ ")
	    print ("|________")
    print(string_game_word)