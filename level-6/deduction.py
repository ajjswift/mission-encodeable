import random

# ----------------
# Subprograms
# ----------------

def declare_number():
    global random_number
    random_number = random.randint(1000, 9999)

# ----------------
# Main program
# ----------------

declare_number()

guessedCorrectly = False
numberOfGuesses = 0

while not guessedCorrectly:
    userGuess = input("Enter a 4-digit number: ")
    numberOfGuesses += 1

    if userGuess == str(random_number):
        guessedCorrectly = True
        print("Congratulations! You guessed correctly!")
        print(f"You took {numberOfGuesses} guesses.")
    else:
        hasBash = False
        hasBosh = False

        for i, letter in enumerate(userGuess):
            if letter in str(random_number):
                hasBash = True
            if letter == str(random_number)[i]:
                hasBosh = True
        
        if hasBosh:
            print("BOSH")
        elif hasBash:
            print("BASH")
        else:
            print("BISH")