# LD Functions for the actions
import csv
from classes import PetCreator

# ACTIONS:
# feed, play, sleep, check stats, manage pets (show current pets, create new, switch pet, release pet, back), save, leave program 

# Feed: Show user types of food. One will be free and others will cost money. If using money, have a variable that is the money saved from the CSV and subtract from that. The new amount will be changed when the user saves. Subtract from hunger and add to happiness
def feed(name):
    while True:
        print(f"Pick a food for {name}:\n1) Basic Pet Feed (FREE!) - Hunger -20 & Happieness +5\n2) Premium ($5) - Hunger -25 & Happieness +10\n3) Treat ($2) - Hunger -7 & Happieness +15\n4) Hoome Meal($10) - Hunger -20 & Happieness +20\n5) Back to Main Menu\n")
        choice = input("Pick the number corresponding to your food choice\n")
        if choice == "1":
            # Go to the class method and get the things updated
            name.update_thing("hunger", -20)
            name.update_thing("happieness", 5)

# Play: show user types of toys to play with. Some will cost $$$. Same principle for food

# Sleep: Have user select bed and move time up four hours. Add 30% to energy

# Check stats: Show the user the current pet's stats

# Manage pets: Show the surrent pets saved then ask if they want to make a new pet, switch pets (cannot do if have only one)(also save previous pet changed stats), release a pet (see a past project to get this code), or go back to main menu

# Save: Get the info for current pet equiped and save its stats. Then, go to use info, update money, day, and time

# Leave: Ask user if they are sure they want to leave and ask them if they are sure they have saved. Maybe I could somehow check if they have saved?

# After the user does something, move time forward an hour
# Use random to trigger a random event. Probably 1-8 and only 3 and 7 trigger event. call this after time advance and DO NOT ADVANCE THE TIME