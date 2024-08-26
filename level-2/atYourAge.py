# A program to:

# ----------------
# Subprograms
# ----------------
    

# I hate match-case, so using if-elif-else instead
def at_your_age(age):
    if age < 8:
        print("You are too young to play this game.")
    elif age == 8:
        print ("At your age, three-time Olympic gold medal winner Wilma Rudolph walked for the first time.")
    elif age == 9:
        print("At your age, Mozart wrote his first symphony.")
    elif age == 10:
        print("At your age, Stevie Wonder signed his first record deal.")
    elif age == 11:
        print("At your age, Victoria van Meter became the first girl to fly across the United States.")
    elif age == 12:
        print("At your age, Steven Spielberg got his first movie camera")
    elif age == 13:
        print("At your age, Jordan Romero became the youngest person to climb Mount Everest.")
    elif age == 14:
        print("At your age, Laura Dekker sailed around the world solo")
    elif age == 15:
        print("At your age, Hanson Crockett Gregory invented the doughnut.")
    elif age == 16:
        print("At your age, Lana del Ray released her first album, 'Born to Die'.")
    else:
        print("You are too old to play this game.")

# ----------------
# Main program
# ----------------

age = int(input("How old are you? "))
at_your_age(age)