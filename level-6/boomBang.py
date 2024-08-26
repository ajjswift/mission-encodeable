# A program that will output 'Boom' when the number is a multiple of 4, 'Bang' when the number is a multiple of 6 and 'BoomBang!' when the number is a multiple of 4 and 6

# ----------------
# Constants
# ----------------

BOOM_NUMBER = 4
BANG_NUMBER = 6

# ----------------
# Subprograms
# ----------------
def boom_bang(maximum_number):
    for number in range(1, maximum_number + 1):
        if number % BOOM_NUMBER == 0 and number % BANG_NUMBER == 0:
            print("BoomBang!")
        elif number % BOOM_NUMBER == 0:
            print("Boom")
        elif number % BANG_NUMBER == 0:
            print("Bang")
        else:
            print(number)

# ----------------
# Main program
# ----------------
print("Welcome to BoomBang! A twist on the classic game FizzBuzz...")
maximum = int(input("Enter the number you'd like to count up to: "))
boom_bang(maximum)