# A program to tell the user which continents are still on their travel bucket list

# ----------------
# Constants
# ----------------

CONTINENT_LIST = ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"]

# ----------------
# Subprograms
# ----------------

def ask_for_continents():
    continents = CONTINENT_LIST.copy()
    add_continents = True
    while add_continents:
        user_input = input("Enter a continent, or f when finished: ")
        if user_input == "f":
            add_continents = False
        else:
            continents.pop(continents.index(user_input))
    return continents


# ----------------
# Main program
# ----------------

print("Welcome to the Continent Bucket List Checker!")
print("This program will allow you to enter the continents you have visited, and will tell you which continents are still on your travel bucket list.")


remaining_continents = ask_for_continents()

if (len(remaining_continents) == len(CONTINENT_LIST)):
    print("You have not visited any continents yet!")
elif (len(remaining_continents) == 0):
    print("Congratulations! You have visited all the continents!")
else:
    print(f"The {len(remaining_continents)} continents still on your bucket list are:")
    for continent in remaining_continents:
        print("-", continent)