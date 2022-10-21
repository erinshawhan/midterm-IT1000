import math
from math import pi

def user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
                continue
            return value
            break
        except:
            print("Please enter a numerical value.")
            continue

def calculations():
    radius = float(user_input("Radius in feet: "))
    height = float(user_input("Height in feet: "))
    formatted_cost = "{:.2f}".format(user_input("Cost per pint of coating: $"))
    cost_per_pint = float(formatted_cost)
    surface_area = (2 * pi * radius * height + 2 * pi * radius ** 2)
    pints = math.ceil(surface_area / 50)
    print("\nNumber of pints needed:", pints)
    rounded_cost = round(pints * cost_per_pint, 2)
    total_cost = "{:.2f}".format(rounded_cost)
    print("Total cost: $", total_cost, sep="")
    

def main():
    print("This program calculates the amount and cost of coating for a cylinder.\n")
    while True:
        calculations()
        answer = input("Would you like to perform another calculation (y/n)? ")
        if answer == "y":
            print("\n")
            continue
        if answer != "y":
            break

main()
