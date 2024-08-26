# A program to generate a random clickbait newspaper headline

# ----------------
# Import libraries
# ----------------

import random

# ----------------
# Constants
# ----------------

PEOPLE = ["Baby", "Toddler", "Teenager", "Man", "Woman", "Elderly woman", "Elderly man", "Elephant", "Doctor", "Fish"]
ACTIVITIES = ["does a poo", "rides elephant", "falls out of hot air balloon", "makes silly noise", "flies kite", "eats a sandwich", "does a trump"]
PLACES = ["school", "playground", "attic", "swimming pool", "cinema", "bowling alley", "restaurant"]
NOUNS = ["elephant", "dog", "banana", "athlete", "teddy bear", "walkie talkie"]
FEELINGS = ["amused", "shocked", "surprised", "humiliated", "astonished", "bowled over", "amazed"]

# ----------------
# Subprograms
# ----------------

def generate_type1():
  chosen_person = random.choice(PEOPLE)
  chosen_activity = random.choice(ACTIVITIES)
  chosen_place = random.choice(PLACES)
  headline = f"{chosen_person} {chosen_activity} in {chosen_place}."
  return headline

def generate_type2():
  chosen_person = random.choice(PEOPLE)
  chosen_feeling = random.choice(FEELINGS)
  chosen_activity = random.choice(ACTIVITIES)
  headline = f"{chosen_person}, {chosen_feeling}, {chosen_activity}."
  return headline

def generate_type3():
  chosen_number = random.randint(1, 10)
  chosen_place = random.choice(PLACES)
  chosen_noun = random.choice(NOUNS)
  chosen_feeling = random.choice(FEELINGS)
  headline = f"{chosen_number} {chosen_place}{chosen_number > 1 and 's'} that leave {chosen_noun}s {chosen_feeling}."
  return headline
  

# ----------------
# Main program
# ----------------
sentence_type = random.randint(1, 3)
match sentence_type:
  case 1:
    sentence = generate_type1()
  case 2:
    sentence = generate_type2()
  case 3:
    sentence = generate_type3()

print(sentence)

