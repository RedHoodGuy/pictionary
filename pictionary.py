import random

array = []
randnum = 0

file = open("pictionary", "r")

for x in file:
	array.append(x)

def pick_word():
    again = "Y"
    while again != "N" and again != "n" and again == "Y" or again == "y":
        randnum = random.randint(0, len(array))
        print(array[randnum])
        again = raw_input("Play again? Y/N\n")

pick_word()
