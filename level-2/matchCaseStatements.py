# A program to demonstrate match-case statements using pizza toppings

# ----------------
# Subprograms
# ----------------

def match_toppings(topping):
    match topping:
        case "mushroom":
            print("You chose mushrooms! They add a unique earthy flavour.")
        case "pineapple":
            print("You chose pineapple! A sweet and tangy tropical topping.")
        case "pepperoni" | "salami":
            print("You chose a meaty topping!")
        case _:
            print("Sorry, that topping is not available.")

# ----------------
# Main program
# ----------------

print("Welcome to the pizza topping matcher!")
user_topping = input("Enter a pizza topping: ")
match_toppings(user_topping)