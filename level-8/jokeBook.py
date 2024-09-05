# This program allows the user to display a random joke from a text file, and write their own jokes to the text file

# ----------------
# Imports
# ----------------

import random

# ----------------
# Constants
# ----------------
FILE_PATH = "level-8/jokes.txt"

# ----------------
# Subprograms
# ----------------

def read_jokes_from_file(file_path):
    with open(file_path, 'r') as jokes_file:
        jokes = jokes_file.readlines() # Creates an array populated with the lines of the file; one new item for every object.
    return jokes

def addJokeToFile(joke):
    with open(FILE_PATH, 'a') as jokes_file:
      jokes_file.write("\n" + joke)

def choose_random_joke(jokes):
    random_joke = random.choice(jokes)
    return random_joke

# ----------------
# Main Program
# ----------------


print("Welcome to the Joke Book!")
addOrReceive = input("Would you like to add a joke or receive a joke? (a/r): ").lower()

if addOrReceive == "r":
    jokes = read_jokes_from_file(FILE_PATH)
    random_joke = choose_random_joke(jokes)
    print("Random Joke:", random_joke)

if addOrReceive == "a":
    joke = input("What's your joke? ")
    addJokeToFile(joke)




