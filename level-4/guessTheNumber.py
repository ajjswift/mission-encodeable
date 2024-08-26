# A program to test students arithmetic with a simple guess the number game

print("Welcome to Twisted Guess the Number! You'll be presented with two numbers and asked to guess the third, which will either be the sum of the two, the multiple of the two or the second subtracted from the first.")

# ----------------
# Import libraries
# ----------------

import random

# ----------------
# Subprograms
# ----------------

def generate_number(number1, number2):
    options = [number1 + number2, number1 * number2, number1 - number2]
    random_number = random.choice(options)
    return random_number


# ----------------
# Main program
# ----------------

lost = False
score = 0

while not lost:
    number1 = random.randint(1, 11)
    number2 = random.randint(1, 11)
    number3 = generate_number(number1, number2)

    print(f"Your numbers are {number1} and {number2}. What is the third number?")
    guess = int(input("Enter your guess: "))

    if guess == number3:
        print("Congratulations! You guessed correctly!")
        score += 1
    else:
        print(f"Sorry, you guessed incorrectly. The correct answer was {number3}.")
        print(f"Your final score was {score}.")
        lost = True
