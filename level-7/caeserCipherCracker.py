# A program to:

# ----------------
# Subprograms
# ----------------


# ----------------
# Main program
# ----------------

word = input("Enter a ciphered word: ")

for i in range(27):
    currentShift = i
    wordarr = []
    for letter in word:
        wordarr.append(chr((ord(letter) - currentShift) % 26 + 65))
    print(f"CURRENT SHIFT: {i}" + "".join(wordarr))
    print()