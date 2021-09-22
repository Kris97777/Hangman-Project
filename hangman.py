import random
import time
time.sleep(2)
print("")
print("  _   _                                                     ")
print(" | | | | __ _ _ __   __ _  ____ ____  _ __ ___   __ _ _ __  ")
print(" | |_| |/ _` | '_ \ / _` ||____|____|| '_ ` _ \ / _` | '_ \ ")
print(" |  _  | (_| | | | | (_| | ____ ____ | | | | | | (_| | | | |")
print(" |_| |_|\__,_|_| |_|\__, ||____|____||_| |_| |_|\__,_|_| |_|")
print("                    |___/                       ")
print("")
time.sleep(1)
print("Welcome to HANG == MAN")
time.sleep(2)

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


def pick_country():
	with open("countries.txt") as chosen_country:
		chosen_country = (random.choice(open('countries.txt').read().split()).strip()) #by anandskumar, thx :)
		return chosen_country.replace(" ", "")




#while True:
time.sleep(2)
if (level == 2) and (lives == 3) or (level == 1) and (lives == 6):
	print("_________")
	print("|	 |  ")
	print("|        ")
	print("|        ")
	print("|        ")
	print("|        ")
	print("|________")
	time.sleep(2)


elif (level == 1) and (lives == 5):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|")
	print("|")
	print("|")
	print("|________")
	time.sleep(2)


elif (level == 2) and (lives == 2) or (level == 1) and (lives == 4):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|	 |")
	print("|	 |")
	print("|")
	print("|________")
	time.sleep(2)


elif (level == 1) and (lives == 3):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|	\|")
	print("|	 |")
	print("|        ")
	print("|________")
	time.sleep(2)


elif (level == 2) and (lives == 1) or (level == 1) and (lives == 2):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|	\|/")
	print("|	 |")
	print("|")
	print("|________")
	time.sleep(2)


elif (level == 1) and (lives == 1):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|	\|/")
	print("|	 |")
	print("|	/ ")
	print("|________")
	time.sleep(2)


elif (level == 1 or 2) and (lives == 0):
	print("_________")
	print("|	 |")
	print("|	 O")
	print("|	\|/")
	print("|	 |")
	print("|	/ \ ")
	print("|________")
	time.sleep(2)

country = pick_country()
print(country)
