# LD Functions for the actions
import csv
import random
import os
import time
from classes import PetCreator
from helpers import type_print

# ACTIONS:
# feed, play, sleep, check stats, manage pets (show current pets, create new, switch pet, release pet, back), save, leave program 
def make_pet():
    the_name = input("Enter the name for your pet:\n").strip().title()
    the_species = input("Enter the species for your pet:\n").strip().title()
    pet = PetCreator(the_name, the_species, 0, random.randint(1,100), random.randint(1,100), random.randint(1,100))
    return pet

# Feed: Show user types of food. One will be free and others will cost money. If using money, have a variable that is the money saved from the CSV and subtract from that. The new amount will be changed when the user saves. Subtract from hunger and add to happiness
def feed(pet):
    while True:
        type_print(f"Pick a food for {pet.name}:\n1) Basic Pet Feed (FREE!) - Hunger -20 & Happieness +5\n2) Premium Food($5) - Hunger -25 & Happieness +10\n3) Treat ($2) - Hunger -7 & Happieness +15\n4) Home-Made Meal($10) - Hunger -20 & Happieness +20\n5) Back to Main Menu\n")
        choice = input("Pick the number corresponding to your food choice\n").strip().lower()
        if choice == "1":
            # Basic Pet food
            # Go to the class method and get the things updated
            pet.update_thing("hunger", -20)
            pet.update_thing("happieness", 5)
            print(f"You fed {pet.name} Basic Food!")
            # return how much user spent
            return 0
        elif choice == "2":
            # Premium food
            # Go to the class method and get the things updated
            pet.update_thing("hunger", -25)
            pet.update_thing("happieness", 10)
            print(f"You fed {pet.name} Premium Food!")
            # return how much user spent
            return 5
        elif choice == "3":
            # Treat
            # Go to the class method and get the things updated
            pet.update_thing("hunger", -7)
            pet.update_thing("happieness", 15)
            print(f"You fed {pet.name} Treat!")
            # return how much user spent
            return 2
        elif choice == "4":
            # Home-made meal
            # Go to the class method and get the things updated
            pet.update_thing("hunger", -20)
            pet.update_thing("happieness", 20)
            print(f"You fed {pet.name} a Home-Made Meal!")
            # return how much user spent
            return 10
        elif choice == "5":
            # back to main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Play: show user types of toys to play with. Some will cost $$$. Same principle for food
def play(pet):
    while True:
        type_print(f"What would you like use to play with {pet.name}:\n1) Chew Toy (FREE!) - Happieness +10 & Energy -7\n2) Throw Toy (FREE!) - Happieness +20 & Energy -20\n3) Hose ($5) - Happieness +15 & Energy -15\n4) Scratch Post ($5) - Happieness + 12 & Energy -5\n5) Back to Main Menu\n")
        choice = input("Enter the number for the toy you would like to use:\n").strip().lower()
        if choice == "1":
            # Chew Toy
            # Go to the class method and get the things updated
            pet.update_thing("energy", -7)
            pet.update_thing("happieness", 10)
            print(f"You played with {pet.name} using Chew Toy!")
            # return how much user spent
            return 0
        elif choice == "2":
            # Throw Toy
            # Go to the class method and get the things updated
            pet.update_thing("energy", -20)
            pet.update_thing("happieness", 20)
            print(f"You played with {pet.name} using Throw Toy!")
            # return how much user spent
            return 0
        elif choice == "3":
            # Hose
            # Go to the class method and get the things updated
            pet.update_thing("energy", -15)
            pet.update_thing("happieness", 15)
            print(f"You played with {pet.name} using Hose!")
            # return how much user spent
            return 5
        elif choice == "4":
            # Scratch Post
            # Go to the class method and get the things updated
            pet.update_thing("energy", -5)
            pet.update_thing("happieness", 12)
            print(f"You played with {pet.name} using Scratch Post!")
            # return how much user spent
            return 5
        elif choice == "5":
            # back to main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Sleep: Have user select bed and move time up four hours. Add 30% to energy
def sleep(pet):
    while True:
        type_print(f"Select a bed for {pet.name} to sleep in:\n1) Basic bed (FREE!) - Energy +20\n2) Premium Bed ($20) - Energy +40\n3) Back to Main Menu\n")
        choice = input("Enter the number corresponding to what you want to do:\n").strip().lower()
        if choice == "1":
            # Basic bed
            pet.update_thing("energy", 20)
            print(f"{pet.name} slept in Basic Bed!")
            return 0
        elif choice == "2":
            # premium bed
            pet.update_thing("energy", 40)
            print(f"{pet.name} slept in Premium Bed!")
            return 20
        elif choice == "3":
            # main menu
            return 0
        else:
            print("Invalid input. Try again")
            continue

# Check stats: Show the user the current pet's stats (done in main menu)

# Manage pets: Show the surrent pets saved then ask if they want to make a new pet, switch pets (cannot do if have only one)(also save previous pet changed stats), release a pet (see a past project to get this code), or go back to main menu
def manage(pet):
    def more_than_one():
        try:
            with open("docs/pet_data.csv", "r") as file:
                the_reader = csv.reader(file)
                try:
                    next(the_reader) # read the header
                    next(the_reader) # read the first row (This must exist because they must already be managing a pet)
                    next(the_reader) # If this can be read, there is a second pet
                    return True
                except:
                    # Can not read anything past the header and first pet. Must only be one
                    return False
        except:
            print("Could not open file in MORE THAN ONE function")

    # Show what pets they have
    type_print("Current pets you have:\n")
    try:
        with open("docs/pet_data.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            for line in reader:
                type_print(f"- Name: {line[0]} Species: {line[1]} Age: {line[2]}")
    except:
        print("Could not read file in MANAGE function")
    
    # Now start the menu of actions they can do
    while True:
        type_print("1) Make New Pet\n2) Switch Pets\n3) Release a Pet (CAN NOT BE UNDONE)\n4) Back to Mian Menu\n")
        choice = input("Enter the number of the action you would like to do:\n")
        if choice == "1":
            # New Pet
            new_pet = make_pet()
            # Write the pet to CSV. NO SWITCHING
            try:
                with open("docs/pet_data.csv", "a", newline='') as csv_file:
                    fieldnames = ['name','species','age','hunger','happieness','energy']
                    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                    writer.writerow({'name': new_pet.name, 'species': new_pet.species, 'age': new_pet.age, 'hunger': new_pet.hunger, 'happieness': new_pet.happieness, 'energy': new_pet.energy})
            except:
                print("Could not open file in MANAGE making a new pet")
            break
        elif choice == "2":
            # Switch pets (Check if they have more than one pet)
            second_pet = more_than_one()
            if second_pet == True:
                # Allow them to switch. I'm lazy and don't want to logic this so I will send them to the starting menu where they can load the pet
                type_print("Saving pet . . .")
                save_pet(pet)
                time.sleep(1)
                type_print("Returning to starting menu to load a pet . . .")
                return 1
            else:
                print("It seems that you only have one pet and can not switch. Try something else")
                continue
        elif choice == "3":
            # Release pet
            # Get the information for the pet for deletion
            name = input("Enter the name for the pet you would like to release:\n").strip().title()
            species = input("Enter the species of the pet you would like to release:\n").strip.title()
            try:
                # Get a file to write the changes to
                temp_filename = "temp_pet.csv"
                with open("docs/pet_data.csv", mode='r', newline='') as infile, open(temp_filename, mode='w', newline='') as outfile:
                    next_reader = csv.DictReader(infile)
                    fieldnames = ['name','species','age','hunger','happieness','energy']
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                    writer.writeheader()

                    # Go through OG file and see if we can find a match for deletion
                    for row in next_reader:
                        if name == row[0] and species == row[1]:
                            # Encountered the match. Deleating it, meaning it cannot be written so we pass over it
                            pass
                        else:
                            # Did not match the pet we have, so everything stays the same. Just write it
                            writer.writerow(row)
                    # Put the temp file in place of the OG file
                    os.replace(temp_filename, "docs/pet_data.csv")
            except:
                print("Could not open pet info file in MANAGE function for releasing pet")
                break
        elif choice == "4":
            # Main menu. Different return values tell me where the user is coming from
            return 0
        else:
            print("Invalid input. Try again")

# Save: Get the info for current pet equiped and save its stats. Then, go to user info, update money, day, and time
def save_pet(pet):
    # First, using the kind of logic from past project, find the pet in the CSV that matches the pet passed in. Then, update(write new file then delete old file) that pet.
    try:
        temp_filename = "temp_pet.csv"
        with open("/workspaces/pet_simulator/docs/pet_data.csv", mode='r', newline='') as infile, open(temp_filename, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            headers = next(reader)
            fieldnames = ['name','species','age','hunger','happieness','energy']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if pet.name == row[0] and pet.species == row[1]:
                    # updating an item. Will continue passing to get any pets that may be after the updated pet
                    writer.writerow({'name': pet.name, 'species': pet.species, 'age': pet.age, 'hunger': pet.hunger, 'happieness': pet.happieness, 'energy': pet.energy})
                    continue
                else:
                    # Did not match the pet we have, so everything stays the same. Just write it
                    writer.writerow(row)
                    continue

            os.replace(temp_filename, "/workspaces/pet_simulator/docs/pet_data.csv")
    except:
        print("Could not open pet info file in SAVE_PET function")

def save_user(money, time, day):
    # Next, go into user info and update money, time, and day
    try:
        with open("docs/user_info.csv", mode="w", newline='') as file:
            fieldnames2 = ['money','day','hour']
            writer2 = csv.DictWriter(file, fieldnames=fieldnames2)
            writer2.writeheader()
            writer2.writerow({'money': money, 'day': day, 'hour': time})
    except:
        print("Could not open user info file in the SAVE_USER function")

# Leave: Ask user if they are sure they want to leave and ask them if they are sure they have saved. Maybe I could somehow check if they have saved? (done in main menu)

# After the user does something, move time forward an hour
# Use random to trigger a random event. Probably 1-8 and only 3 and 7 trigger event. call this after time advance and DO NOT ADVANCE THE TIME (done in main menu)