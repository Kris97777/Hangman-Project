import random
import time

level = 0
lives = 0
guessed_letter = []

#csináltam egy main functiont amibe majd az egészet belepakoljuk később
def main_game():
	welcome_message()
	select_difficulty()
	display_hangman()
	hide_country()




#kiprinteli a fasza kis intro dolgokat
def welcome_message():
	#time.sleep(2)
	print("")
	print("  _   _                                                     ")
	print(" | | | | __ _ _ __   __ _  ____ ____  _ __ ___   __ _ _ __  ")
	print(" | |_| |/ _` | '_ \ / _` ||____|____|| '_ ` _ \ / _` | '_ \ ")
	print(" |  _  | (_| | | | | (_| | ____ ____ | | | | | | (_| | | | |")
	print(" |_| |_|\__,_|_| |_|\__, ||____|____||_| |_| |_|\__,_|_| |_|")
	print("                    |___/                       ")
	print("")
	#time.sleep(1)
	print("Welcome to HANG == MAN")
	#time.sleep(2)


#választ egy nehézséget ami megadja az életek számát,ezen belül van a a hangman ascii art is,szerintem az később kapjon saját functiont
def select_difficulty():
	global level
	global lives
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
			print("Please choose an existing difficulty! (1 for rookie or 2 for expert)")
	# while True:
	# time.sleep(2)
def display_hangman():
	#while True:
	if (level == 2) and (lives == 3) or (level == 1) and (lives == 6):
		print("_________")
		print("|	 |  ")
		print("|        ")
		print("|        ")
		print("|        ")
		print("|        ")
		print("|________")
		print(" ")
		time.sleep(2)
		

	elif (level == 1) and (lives == 5):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|")
		print("|")
		print("|")
		print("|________")
		print(" ")
		time.sleep(2)
	

	elif (level == 2) and (lives == 2) or (level == 1) and (lives == 4):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|	 |")
		print("|	 |")
		print("|")
		print("|________")
		print(" ")
		time.sleep(2)
	

	elif (level == 1) and (lives == 3):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|	\|")
		print("|	 |")
		print("|        ")
		print("|________")
		print(" ")
		time.sleep(2)


	elif (level == 2) and (lives == 1) or (level == 1) and (lives == 2):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|	\|/")
		print("|	 |")
		print("|")
		print("|________")
		print(" ")
		time.sleep(2)


	elif (level == 1) and (lives == 1):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|	\|/")
		print("|	 |")
		print("|	/ ")
		print("|________")
		print(" ")
		time.sleep(2)


	elif (level == 1 or 2) and (lives == 0):
		print("_________")
		print("|	 |")
		print("|	 O")
		print("|	\|/")
		print("|	 |")
		print("|	/ \ ")
		print("|________")
		print(" ")
		time.sleep(2)


def win_or_lose():
	pass


# Ez valamiért nem stimmel, levágja a több szavas országok végeit, rá kéne jönni miért és javítani
def pick_country():
	countries = []
	capitals = []
	with open("countries-and-capitals.txt") as countries_txt:
		for line in countries_txt:
			splitted_line=(line.split("|"))
			countries.append(splitted_line[0].replace(" ", ""))
			capitals.append(splitted_line[1])
		chosen_country = (random.choice(countries))
		return list(chosen_country)
		
def hide_country():
	country = pick_country()
	print(country)


def guess_letter():
	guess1 = input("Guess a letter! \n")
	if validate_input(guess1) is True:
		guessed_letter.append(guess1)
		print("You guessed right!")
	else:
		print("Sorry, wrong guess!")
		return lives-1
	while "_" in guessed_letter:
		guess2 = input("Guess another letter! \n")
		if validate_input(guess2) is True:
			guessed_letter.append(guess2)
			print("You guessed right!")
		else:
			print("Sorry, wrong guess!")
			return lives-1


def validate_input(guess):
	if ord(guess) >= 65 and ord(guess) <= 90 or ord(guess) >= 97 and ord(guess) <= 122 :
		return True
    	
	else:
		return None
    	



# 	username = input("Choose a username: ")
# final_username = username.translate({ ord(c): None for c in "._!" })
	

#ez lefuttatja a main body-t
main_game()
# hide_country()
#print(pick_country())

#Ez Gábor megoldása a random ország megnézésére,csak ki kell venni kommentből hogy teszteljünk
#for x in range(20):
	#country = pick_country()
	#print(country)

#ami még kell:
#-implementálni a list funckiót a random város nevére
#	>>> x = 'abc'
#	>>> list(x)
#	['a', 'b', 'c']
#-egy loop megcsinálása hogy találgathasson a user, több eset:
#	nem betű(ascii validator implementálás)
#	eltalálja(_ átváltozik helyes betűvé,betű a guessed_letters halmazba kerül)
#	nem találja el(-1 élet,betű a guessed_letters halmazba kerül)
#-victory és defeat üzenetek 
#	ha lives <= 0 akkor defeat
#	ha guessed letters = random ország betűivel akkor victory
#ctlr k u kiszedni kommentet
#ctlr k c komment
