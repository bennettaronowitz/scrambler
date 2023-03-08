from random import randint
from sys import argv

RED = "\033[1;31m"
BLUE = "\033[1;34m"

def scramble(word):
	word = word.replace(" ", "").lower()
	scrambled = ""
	selected_indexes = []
	while len(selected_indexes) != len(word):
		index = randint(0,len(word)- 1)
		if index not in selected_indexes:
			selected_indexes.append(index)
			scrambled += word[index]
	return scrambled
	
word = argv[1]
print(f"{RED}A scrambled version of {BLUE}{word} {RED}is {BLUE}{scramble(word)}.") 
