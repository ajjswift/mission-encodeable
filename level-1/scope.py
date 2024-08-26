# A program to demonstrate local and global scope

# ----------------
# Subprograms
# ----------------

def scope():
    global number1 
    number1 = 3

# ----------------
# Main program
# ----------------

scope()
print(number1)