# LD 1st Pet Simulator Personal Project
from helpers import type_print
# First, welcome the user and have them either load a pet or create a pet
# Show the user their pet's stats and have them select an action

def main():
    print("Welcome User to Pet Simulator!\n")
    while True:
        type_print("Would you like to\n1) Make New Pet\nor\n2) Load Pet")
        action = input("Enter the number corresponding to what you want to do\n")
        if action == "1":
            # Make new pet
            pass
        elif action == "2":
            # check if pets saved in CSV
            # If yes, show and have select
            pass
        else:
            print("Invalid input. Try again")
            continue