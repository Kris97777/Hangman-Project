import random
print("")
print("  _   _                                         ")
print(" | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print(" | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print(" |  _  | (_| | | | | (_| | | | | | | (_| | | | |")
print(" |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                    |___/                       ")
print("")
print("Welcome to HANG == MAN")

level = 0
lives = 0

while True:
    x = input("Choose your difficulty: 1 for rookie(6 lives) or 2 for expert(3 lives). \n")
    if x == ("1"):
        level = 1
        lives = 6
        print ("You chose the rookie difficulty, with 6 lives!")
        break
    
    if x == ("2"):
        level = 2
        lives = 3
        print("You chose the expert difficulty, with 3 lives!")
        break
    if x == ("quit"):
        print("Good Bye!")
        break
    else:
        print("Please choose an existing difficulty! (1 for rookie or 2)")

def pick_a_random():
    with open("countries.txt") as f:
		print(random.choice(open('countries.txt').read().split()).strip()) #by anandskumar, thx :)



while True:
    if (level == 2) and (lives == 3) or (level == 1) and (lives == 6):
	    print("_________")
	    print("|	 |  ")
	    print("|        ")
	    print("|        ")
	    print("|        ")
	    print("|        ")
	    print("|________")
    elif (level == 1) and (lives == 5):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|")
	    print ("|")
	    print ("|")
	    print ("|________")
    elif (level == 2) and (lives == 2) or (level == 1) and (lives == 4):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	 |")
	    print ("|	 |")
	    print ("|")
	    print ("|________")
    elif (level == 1) and (lives == 3):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|")
	    print ("|	 |")
	    print ("|        ")
	    print ("|________")
    elif (level == 2) and (lives == 1) or (level == 1) and (lives == 2):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|")
	    print ("|________")
    elif (level == 1) and (lives == 1):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|	/ ")
	    print ("|________")
    elif (level == 1 or 2) and (lives == 0):
	    print ("_________")
	    print ("|	 |")
	    print ("|	 O")
	    print ("|	\|/")
	    print ("|	 |")
	    print ("|	/ \ ")
	    print ("|________")
