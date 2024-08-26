# This program will demonstrate a function

# ----------------
# Subprograms
# ----------------

def check_age(age):
    if age >= 18:
        print("You are old enough to vote.")
    else:
        print("You are not old enough to vote.")

# ----------------
# Main program
# ----------------

user_age = input("How old are you?")
check_age(int(user_age))