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
    else:
        print("Pls choose a valid operator!")

with open("countries-and-capitals.txt") as f:
    word_list = f.read().splitlines()

