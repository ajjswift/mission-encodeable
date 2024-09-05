# A game in which a user must guess the songs by their names.

# ----------------
# Import libraries
# ----------------

import random

# ----------------
# Subprograms
# ----------------

def chooseRandomSong():
    with open('level-8/songs.txt', 'r') as song_file:
        random_song = random.choice(song_file.readlines())
    return random_song

def turnIntoMysteryString(s):
    print(s.split(', '))
    artistUnsplit = s.split(', ')[1]
    artistSplit = artistUnsplit.split(' ') # Add in checking for multi-worded artist names.
    songTitleUnsplit = s.split(', ')[0]
    songTitleSplit = songTitleUnsplit.split(' ')

    string = ""

    for word in songTitleSplit:
        string += word[0] + ('_' * len(word[1:])) + " "
    
    string += "by "

    for word in artistSplit:
        string += word[0] + ('_' * len(word[1:])) + " "

    return string

def splitSongForIncorrect(s):
    return s.split(', ')[0] + ' by ' + s.split(', ')[1]

# ----------------
# Main program
# ----------------

print('Welcome to Guess The Song!')
print("When prompted, enter your answer by filling in the blanks")

song = chooseRandomSong()
mysteryString = turnIntoMysteryString(song)

print("")
print(mysteryString)
print("")

answer = input("What is the answer? ")

if answer.lower() == (splitSongForIncorrect(song).lower()):
    print("Correct!")
else:
    print(answer.lower())
    print(splitSongForIncorrect(song).lower())
    print(f"Incorrect. The song was {splitSongForIncorrect(song)}")