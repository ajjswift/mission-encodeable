# ----------------
# Constants
# ----------------

BASE_FARE = 5.00
ZONE_MULTIPLIER = 2.50

# ----------------
# Subprograms
# ----------------

def calculate_fare(start_zone, end_zone):
    fare = BASE_FARE + abs(end_zone - start_zone) * ZONE_MULTIPLIER
    return f"£{fare:.2f}"
# ----------------
# Main program
# ----------------


start_zone = int(input("Enter the starting zone: "))
end_zone = int(input("Enter the ending zone: "))
fare = calculate_fare(start_zone, end_zone)

print(f"The fare from Zone {start_zone} to Zone {end_zone} is {fare}.")