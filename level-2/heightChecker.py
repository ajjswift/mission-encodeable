# A program where the user can input their height and be informed of another object that is their height
# ----------------
# Subprograms
# ----------------

def check_height(user_height):
    if user_height == 100:
        print("You are the same height as a 1m tall ruler.")
    elif user_height == 150:
        print("You are the same height as a 1.5m tall person.")
    elif user_height == 200:
        print("You are the same height as a 2m tall door.")
    elif user_height < 80:
        print("You are not yet tall enough to use this height checker.")
    elif user_height < 90:
        print("You are about the same height as a snooker table, which is roughly 80cm tall!")
    elif user_height < 100:
        print("You are about the same height as the UK's Royal Sceptre, which is roughly 92cm tall!")
    elif user_height < 110:
        print("You are about the same height as an Olympic hurdle in the men's high hurdle event, which is 106.7cm tall!")
    elif user_height < 120:
        print("You are about the same height as a wild turkey, which is roughly 115cm tall!")
    elif user_height < 130:
        print("You are about the same height as an emperor penguin, which is roughly 120cm tall!")
    elif user_height < 140:
        print("You are about the same height as a hippo, which is roughly 130cm tall")
    elif user_height < 150:
        print("You are about the same height as a UK Post Box, which is roughly 140cm tall!")
    elif user_height < 160:
        print("You are about the same height as a gorilla, which is roughly 150cm tall!")
    elif user_height < 170:
        print("You are about the same height as the average rainfall in Thailand, which is 162.2cm!")
    elif user_height < 180:
        print("You are about the same height as computing pioneer Alan Turing, who is believed to have been roughly 170cm tall.")
    else:
        print("You are too tall to use the height checker.")

# ----------------
# Main program
# ----------------
print("Welcome to the height checker!")
user_height = int(input("Enter your height to the nearest centimetre: "))
check_height(user_height)