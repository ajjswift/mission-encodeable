# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Subprograms
# ----------------

def shuffle_list(list):
    random.shuffle(list)
    return list

# ----------------
# Main program
# ----------------

list = ["apple", "banana", "cherry", "date", "elderberry"]
shuffled_list = shuffle_list(list)

print(f"Your shuffled list is {shuffled_list}.")