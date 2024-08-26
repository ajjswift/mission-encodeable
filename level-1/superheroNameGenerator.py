# A program to generate a superhero name

# ----------------
# Subprograms
# ----------------

def generate_name(user_adjective, user_animal):
    superhero_name = user_adjective + " " + user_animal
    return superhero_name  

# ----------------
# Main program
# ----------------

# Welcomes the user to the Superhero Name Generator
print("Welcome to the Superhero Name Generator!")

# Asks the user to enter an adjective and a species of animal
user_adjective = input("Enter an adjective (describing word): ")
user_animal = input("Enter your favourite species of animal: ")

# Calls the generate_name function and assigns the result to the variable superhero_name
superhero_name = generate_name(user_adjective, user_animal)
print("Your superhero name is: " + superhero_name)