# A program which constantly asks "Are we nearly there yet?"

# ----------------
# Subprograms
# ----------------
def ask_if_nearly_there():
    arrived = False
    while not arrived:
        answer = input("Are we nearly there yet?")
        if answer == "yes":
            arrived = True
    print("Finally!")
  
# ----------------
# Main program
# ----------------
ask_if_nearly_there()