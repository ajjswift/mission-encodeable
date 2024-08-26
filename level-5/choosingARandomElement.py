# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Subprograms
# ----------------
def choose_random(list):
    random_element = random.choice(list)
    print(f"Your random element is {random_element}.")

# ----------------
# Main program
# ----------------
favourite_animals = ["giraffe", "elephant", "tiger"]
choose_random(favourite_animals)