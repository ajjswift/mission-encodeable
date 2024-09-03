# A program to convert text into Pig Latin.

# ----------------
# Constants
# ----------------

VOWELS = ["a", "e", "i", "o", "u"]

# ----------------
# Subprogram
# ----------------
def one_word_translator(word):
    if word[0] not in VOWELS:
        return word[1:] + word[0] + "ay"
    else:
        return word + "yay"
    
def passInAllWords(words):
    translated_words = []
    for word in words:
        translated_words.append(one_word_translator(word))
    return " ".join(translated_words)


# ----------------
# Main program
# ----------------
print("Welcome to the Pig Latin Translator!")
sentence = input("Enter a sentence to translate: ")
print(passInAllWords(sentence.split()))