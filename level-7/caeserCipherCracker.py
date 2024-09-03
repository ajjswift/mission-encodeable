def decipher_word(word):
    word = word.upper()
    shifts = []

    # Store the shifted versions of the word with corresponding shift values
    for i in range(-13, 14):  # Shift range from -13 to +13
        shifted_word = []
        for letter in word:
            if 'A' <= letter <= 'Z':  # Only shift alphabetic characters
                new_char = chr((ord(letter) - 65 + i) % 26 + 65)
                shifted_word.append(new_char)
            else:
                shifted_word.append(letter)
        shifts.append((i, ''.join(shifted_word)))

    return shifts

def print_shifts(shifts):
    max_shift_length = max(len(shift[1]) for shift in shifts)

    # Format the output
    for i, (shift_val, shifted_word) in enumerate(shifts):
        # Aligning all the shifts
        shift_output = f"Shift {shift_val:+3}: {shifted_word.center(max_shift_length)}"
        print(shift_output)

# ----------------
# Main program
# ----------------

word = input("Enter a ciphered word: ")

shifts = decipher_word(word)
print_shifts(shifts)