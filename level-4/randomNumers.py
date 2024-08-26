# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Subprograms
# --------------
def generate_random_float():
    random_float = random.random()
    return random_float

def generate_random_int(num1, num2):
    random_int = random.randint(num1, num2)
    return random_int

# ----------------
# Main program
# ----------------

random_float = generate_random_float()
random_int = generate_random_int(1, 10)
print(f"The random float generated is {random_float}.")
print(f"The random integer generated is {random_int}.")