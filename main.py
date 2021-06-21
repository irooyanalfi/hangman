import random

def drawHangman(idx = 0):
	hg = ["""
	--------
	|      |
	|      O
	|
	|
	|
	|
	""", 
	"""
	--------
	|      |
	|      O
	|      |
	|
	|
	|
	""", 
	"""
	--------
	|      |
	|      O
	|     /|
	|
	|
	|
	""", """
	--------
	|      |
	|      O
	|     /|\\
	|
	|
	|
	""", 
	"""
	--------
	|      |
	|      O
	|     /|\\
	|     /
	|
	|
	""", """
	--------
	|      |
	|      O
	|     /|\\
	|     / \\
	|
	|
	"""]
	print(hg[idx])

def checkGame(tries, word_guessed, answer):
	percobaan = len(word_guessed)
	win_counter = 0

	matched_char = [char in word_guessed for char in answer]
	for x in range(len(matched_char)):
		if matched_char[x] :
			print(answer[x], end=" ")
			percobaan -= 1
			win_counter += 1
		else:
			print('_', end=" ")
	print("\n")

	if(percobaan < 6):
		if win_counter == len(answer):
			return 1, percobaan

	if percobaan < 0:
		return 0, 0
	else:
		return 0, percobaan
		#print(matched_char)
	#if(tries > 6):
	#	print("Permainan Berakhir. Anda kalah.")

def insertGuess(word_guessed, guess):
	if guess.isalpha() :
		for x in range(len(guess)):
			if guess[x] in word_guessed:
				print("Anda telah menebak huruf "+guess[x])
			else:
				word_guessed.append(guess[x])
	else:
		print("Maaf, anda hanya boleh memasukkan alfabet")
	return word_guessed

# open a file
file = open("wordlist.txt").read().splitlines()
answer = random.choice(file).upper()
win = 0
tries = 0
word_guessed = []
print('_ '*len(answer))

while 1:
	if win:
		print("Selamat anda menang !!")
		break
	if tries > 5:
		print("Permainan Berakhir. Anda kalah.")
		print("jawaban yang benar ialah : "+answer)
		break
	drawHangman(tries)
	#print('_ ' * len(answer))
	guess = input("Tebak kata dimaksud dengan memasukkan huruf atau kata:")
	guess = guess.upper()
	word_guessed = insertGuess(word_guessed, guess)
	win, tries = checkGame(tries, word_guessed, answer)
	#print(tries, word_guessed, answer) 


