# A program to play the classic game of Hangman

# ----------------
# Import libraries
# ----------------

import random
import os
# ----------------
# Constants
# ----------------

HANGMAN_PICS = [r'''
  -----
      |
      |
      |
      |
      |
=========''',r'''
  -----
  |   |
      |
      |
      |
      |
=========''', r'''
  -----
  |   |
  O   |
      |
      |
      |
=========''', r'''
  -----
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  -----
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Once again, converted to raw text to avoid any issues.

WORDS = ["sloth", "koala", "leopard", "tiger", "panda", "elephant", "giraffe"]


# ----------------
# Subprograms
# ----------------

def choose_random_word():
    global random_word
    random_word = random.choice(WORDS)

# ----------------
# Main program
# ----------------

choose_random_word()
print("Welcome to Hangman!")

# Create a list of underscores to represent the word
global word_display
word_display = []
for i in range(len(random_word)):
    word_display.append("_")

print(' '.join(word_display))

# Create a list to store the letters guessed by the player
global guessed_letters
guessed_letters = []

# Create a variable to store the number of incorrect guesses
global incorrect_guesses
incorrect_guesses = 0

wordGuessed = False
while not wordGuessed:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HANGMAN_PICS[incorrect_guesses])
    print()

    print(' '.join(word_display))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                word_display[i] = guess
        print(' '.join(word_display))
    else:
        incorrect_guesses += 1
        print(HANGMAN_PICS[incorrect_guesses - 1])

    if "_" not in word_display:
        wordGuessed = True
        print("Congratulations! You guessed the word!")
    elif incorrect_guesses == 6:
        wordGuessed = True
        print(f"Sorry, you have run out of guesses. The word was {random_word}.")