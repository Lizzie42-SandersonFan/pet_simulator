# LD Functions for the actions
import csv
from classes import PetCreator
import random
from helpers import type_print

# ACTIONS:
# feed, play, sleep, check stats, manage pets (show current pets, create new, switch pet, release pet, back), save, leave program 
def make_pet():
    the_name = input("Enter the name for your pet:\n").strip().title()
    the_species = input("Enter the species for your pet:\n").strip.title()
    pet = PetCreator(the_name, the_species, 0, random.randint(1,100), random.randint(1,100), random.randint(1,100))
    return pet

# Feed: Show user types of food. One will be free and others will cost money. If using money, have a variable that is the money saved from the CSV and subtract from that. The new amount will be changed when the user saves. Subtract from hunger and add to happiness
def feed(name):
    while True:
        type_print(f"Pick a food for {name}:\n1) Basic Pet Feed (FREE!) - Hunger -20 & Happieness +5\n2) Premium Food($5) - Hunger -25 & Happieness +10\n3) Treat ($2) - Hunger -7 & Happieness +15\n4) Home-Made Meal($10) - Hunger -20 & Happieness +20\n5) Back to Main Menu\n")
        choice = input("Pick the number corresponding to your food choice\n").strip().lower()
        if choice == "1":
            # Basic Pet food
            # Go to the class method and get the things updated
            name.update_thing("hunger", -20)
            name.update_thing("happieness", 5)
            print(f"You fed {name} Basic Food!")
            # return how much user spent
            return 0
        elif choice == "2":
            # Premium food
            # Go to the class method and get the things updated
            name.update_thing("hunger", -25)
            name.update_thing("happieness", 10)
            print(f"You fed {name} Premium Food!")
            # return how much user spent
            return 5
        elif choice == "3":
            # Treat
            # Go to the class method and get the things updated
            name.update_thing("hunger", -7)
            name.update_thing("happieness", 15)
            print(f"You fed {name} Treat!")
            # return how much user spent
            return 2
        elif choice == "4":
            # Home-made meal
            # Go to the class method and get the things updated
            name.update_thing("hunger", -20)
            name.update_thing("happieness", 20)
            print(f"You fed {name} a Home-Made Meal!")
            # return how much user spent
            return 10
        elif choice == "5":
            # back to main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Play: show user types of toys to play with. Some will cost $$$. Same principle for food
def play(name):
    while True:
        type_print(f"What would you like use to play with {name}:\n1) Chew Toy (FREE!) - Happieness +10 & Energy -7\n2) Throw Toy (FREE!) - Happieness +20 & Energy -20\n3) Hose ($5) - Happieness +15 & Energy -15\n4) Scratch Post ($5) - Happieness + 12 & Energy -5\n 5) Back to Main Menu\n")
        choice = input("Enter the number for the toy you would like to use:\n").strip().lower()
        if choice == "1":
            # Chew Toy
            # Go to the class method and get the things updated
            name.update_thing("energy", -7)
            name.update_thing("happieness", 10)
            print(f"You played with {name} using Chew Toy!")
            # return how much user spent
            return 0
        elif choice == "2":
            # Throw Toy
            # Go to the class method and get the things updated
            name.update_thing("energy", -20)
            name.update_thing("happieness", 20)
            print(f"You played with {name} using Throw Toy!")
            # return how much user spent
            return 0
        elif choice == "3":
            # Hose
            # Go to the class method and get the things updated
            name.update_thing("energy", -15)
            name.update_thing("happieness", 15)
            print(f"You played with {name} using Hose!")
            # return how much user spent
            return 5
        elif choice == "4":
            # Scratch Post
            # Go to the class method and get the things updated
            name.update_thing("energy", -5)
            name.update_thing("happieness", 12)
            print(f"You played with {name} using Scratch Post!")
            # return how much user spent
            return 5
        elif choice == "5":
            # back to main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Sleep: Have user select bed and move time up four hours. Add 30% to energy
def sleep(name):
    while True:
        type_print(f"Select a bed for {name} to sleep in:\n1) Basic bed (FREE!) - Energy +20\n2) Premium Bed ($20) - Energy +40\n3) Back to Main Menu\n")
        choice = input("Enter the number corresponding to what you want to do:\n").strip().lower()
        if choice == "1":
            # Basic bed
            name.update_thing("energy", 20)
            print(f"{name} slept in Basic Bed!")
            return 0
        elif choice == "2":
            # premium bed
            name.update_thing("energy", 40)
            print(f"{name} slept in Premium Bed!")
            return 20
        elif choice == "3":
            # main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Check stats: Show the user the current pet's stats (done in main menu)

# Manage pets: Show the surrent pets saved then ask if they want to make a new pet, switch pets (cannot do if have only one)(also save previous pet changed stats), release a pet (see a past project to get this code), or go back to main menu
# BUILD

# Save: Get the info for current pet equiped and save its stats. Then, go to user info, update money, day, and time
# BUILD
def save(pet, money, time, day):
    # First, using the kind of logic from past project, find the pet in the CSV that matches the pet passed in. Then, update(write new file then delete old file) that pet.
    # Next, 
    pass

# Leave: Ask user if they are sure they want to leave and ask them if they are sure they have saved. Maybe I could somehow check if they have saved? (done in main menu)

# After the user does something, move time forward an hour
# Use random to trigger a random event. Probably 1-8 and only 3 and 7 trigger event. call this after time advance and DO NOT ADVANCE THE TIME