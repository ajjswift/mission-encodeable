# A program to calculate the size of a population after a given number of years, given the average growth per year.
import math

# ----------------
# Subprograms
# ----------------

def calculate_population_size(current_population_size, growth_rate, years):
    new_population_size = current_population_size * (growth_rate ** years)
    return new_population_size

# ----------------
# Main program
# ----------------

population_size = int(input("Enter the size of the current population: "))
population_growth = float(input("Enter the current percentage growth of the population per year (in the format 1.XX): "))
years = int(input("Enter the number of years to calculate the population size for: "))

new_population_size = math.floor(calculate_population_size(population_size, population_growth, years)) # floor() is used to round down the result to the nearest whole number, as population sizes are whole numbers.
print(f"The population size after {years} years will be {new_population_size}.")
