import random

# A list of words that
potential_words = ["examplpye", "words", "someone", "can", "guess"]

# word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
# TIP: the number of letters should match the word
current_word = list(word)
# Some useful variables
guesses = [] #holds all previously guessed letters
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ").lower

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	if guess.isalpha() and len(guess) == 1 and guess not in guesses :
		guesses.append(guess)
		print(guesses)
		if guess in current_word :
			print ("Your guess is right")
		#guess is right
		else:
			fails += 1
			print("You guessed incorrectly.")
		#guess is wrong
		print("You have " + str(maxfails - fails) + " tries left!")

	else:
		print ("Invalid statement: {guess}")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
#add a random commet

	display = ""
	for i in current_word:
		if i in guesses:
			display += i + " "
			winning += i

		else:
			display +="_"

	print(display)

	if winning == word:
		print("You won!)")
		exit(0)

	#display status of how far we are

print(F"You have lost. The word is {word}")
