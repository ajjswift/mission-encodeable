# A program to check if the user's password is secure

from getpass import getpass

# ----------------
# Subprograms
# ----------------
  
def count_letters(password):
    cleaned_string = ''.join([char for char in password if char.isalpha()])
    return len(cleaned_string)

def count_uppercase(password):
    cleaned_string = ''.join([char for char in password if char.isupper()])
    return len(cleaned_string)

def count_lowercase(password):
    cleaned_string = ''.join([char for char in password if char.islower()])
    return len(cleaned_string)

def count_numbers(password):
    cleaned_string = ''.join([char for char in password if char.isdigit()])
    return len(cleaned_string)

def count_special_characters(password):
    cleaned_string = ''.join([char for char in password if not char.isalnum()])
    return len(cleaned_string)

def check_password_strength(password):
    password_strength = 0
    if count_letters(password) >= 8:
        password_strength += 1
    if count_uppercase(password) >= 1:
        password_strength += 1
    if count_lowercase(password) >= 1:
        password_strength += 1
    if count_numbers(password) >= 1:
        password_strength += 1
    if count_special_characters(password) >= 1:
        password_strength += 1
    return password_strength

# ----------------
# Main program
# ----------------

score = check_password_strength(getpass("Enter your password: "))

if score == 5:
    print("Your password is strong!")
elif score >= 3:
    print("Your password is moderately strong.")
else:
    print("Your password is weak.")
