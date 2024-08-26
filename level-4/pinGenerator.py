# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Subprograms
# ----------------
def generate_pin(birthday):
    random.seed(birthday)

    pin = random.randint(1000, 9999)
    return pin

# ----------------
# Main program
# ----------------

birthday = input("Enter your birthday in the format DDMMYYYY: ")
pin = generate_pin(birthday)
print(f"Your new pin is {pin}.")