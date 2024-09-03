# A program to generate cRAzY tExT

# ----------------
# Import libraries
# ----------------

import random

# ----------------
# Subprograms
# ----------------

def makeCrazyText(text):
    crazy_text = ""
    for letter in text:
        if letter.isalpha(): # Check character is a letter to avoid errors from spaces, punctuation, numbers, etc.
            isUpper = random.choice([True, False]) # Using T/F instead of 1/0 to make the code more readable
            if isUpper:
                crazy_text += letter.upper()
            else:
                crazy_text += letter.lower()
        else:
            crazy_text += letter
    return crazy_text

# ----------------
# Main program
# ----------------

text = input("Enter some text: ")
crazy_text = makeCrazyText(text)
print(f"Your crazy text is: {crazy_text}")