# A program to: 

# ----------------
# Subprograms
# ----------------

def user_age():
    global age
    age = int(input("Enter your age: "))

def convert_to_seconds():
    seconds = age * 31557600
    return seconds

def convert_to_minutes():
    minutes = age * 525960
    return minutes

def convert_to_hours():
    hours = age * 8766
    return hours

def convert_to_days():
    days = age * 365.25
    return days

def convert_to_weeks():
    weeks = age * 52
    return weeks

def convert_to_months():
    months = age * 12
    return months

# ----------------
# Main program
# ----------------

# Welcomes the user to the Lifetime Statistics program
print("Welcome to the Lifetime Statistics program!")

# Calls the user_age function and assigns the result to the variable age
user_age()

# Convert to different units.

print("You are", convert_to_seconds(age), "seconds old.")
print("You are", convert_to_minutes(age), "minutes old.")
print("You are", convert_to_hours(age), "hours old.")
print("You are", convert_to_days(age), "days old.")
print("You are", convert_to_weeks(age), "weeks old.")
print("You are", convert_to_months(age), "months old.")

