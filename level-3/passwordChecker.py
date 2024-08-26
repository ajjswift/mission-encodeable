# A program to check if a user's password matches the default password

# ----------------
# Imports
# ----------------

from getpass import getpass

# ----------------
# Constants
# ----------------
PASSWORD = "LetMeIn"
ALLOWED_ATTEMPTS = 3
# ----------------
# Subprograms
# ----------------

def check_password(password):
    if password == PASSWORD:
        return True
    else:
        print("Incorrect password.")
        return False

# ----------------
# Main program
# ----------------

successfulPassword = False
used_attempts = 0

while not successfulPassword and used_attempts < ALLOWED_ATTEMPTS:
    user_password = getpass("Enter your password: ")
    correctPassword = check_password(user_password)
    if correctPassword:
        successfulPassword = True
        break
    used_attempts += 1

if not successfulPassword:
    print("Access forbidden. Too many incorrect attempts.")
else:
    print("Access granted!")
