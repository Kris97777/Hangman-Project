import random
import time


level = 0
lives = 0
correct_letter = []
guessed_letter = []


def main_game():
	welcome_message()
	select_difficulty()
	display_hangman()
	hide_country()
	guess_letter()
	show_hangman_status = display_hangman()
	letter_is_guessed = guess_letter()
	if letter_is_guessed is True:
		show_hangman_status


def welcome_message():
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
	time.sleep(2)


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
	print(" __ " * len(country))


def guess_letter():
	guess1 = input("Guess a letter! \n")
	if validate_input(guess1) is True:
		guessed_letter.append(guess1)
	else:
		print("Sorry, that's not a letter!")
	while "_" in guessed_letter:
		guess2 = input("Guess another letter! \n")
		if validate_input(guess2) is True:
			guessed_letter.append(guess2)
		else:
			print("Sorry, that's not a letter!")
	return True


def validate_input(guess):
	if ord(guess) >= 65 and ord(guess) <= 90 or ord(guess) >= 97 and ord(guess) <= 122 :
		return True
    	
	else:
		return False


def incorrect_guess():
	pass


def correct_guess():
	pass


main_game()
#print(correct_letter)


#ctlr k u kiszedni kommentet
#ctlr k c komment
