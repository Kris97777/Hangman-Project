import random
print ("Welcome to HANG == MAN")

levels = 0
lives = 0

while True:
    x = input ("Pls choose your level: 1 for rookie or 2 for expert. \n")
    if x == ("1"):
        levels = 1
        lives = 6
        print ("You choose the rookie level.")
        break
    
    if x == ("2"):
        levels = 2
        lives = 3
        print ("You choose the expert level.")
        break

words = open("countries-and-capitals.txt")
hangman_list = []
