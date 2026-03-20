# LD 1st Pet Simulator Personal Project
from helpers import type_print
from actions import *
from classes import PetCreator
import random

# First, welcome the user and have them either load a pet or create a pet
# Show the user their pet's stats and have them select an action

def main():
    # These variables will need to be changed to acess what is in the CSV
    the_time = 8
    the_day = 1
    user_money = 1000
    # This will be used to know if I should recomend the user save if they leave without having saved
    changes = False

    def action_main():
        nonlocal current_pet
        nonlocal the_time
        nonlocal user_money
        nonlocal changes

        print(f"Current pet: {current_pet.name}({current_pet.species}) | Time: {the_time}:00 | Current Balance: ${user_money}")
        print(current_pet)
        while True:
            trigger_num = random.randint(1, 8)
            # Trigger a random event using random
            # Hope this works
            if trigger_num == 3:
                event = current_pet.name.found_toy()
                print(event)
            elif trigger_num == 7:
                event = current_pet.name.found_food()
                print(event)
            
            type_print(f"What would you like to do with {current_pet.name}:\n1) Feed {current_pet.name}\n2) Play with {current_pet.name}\n3) Put {current_pet.name} to Sleep\n4) Check {current_pet.name}'s Statuses\n5) Manage your Pets\n6) Save\n7) Leave Program\n")
            choice = input("Type the number corresponding to your action:\n")
            if choice == "1":
                # Feed
                money_spent = feed(current_pet.name)
                user_money -= money_spent
                changes = True
                the_time += 1
                # Call time check when it's built (in helpers file)
            elif choice == "2":
                # Play
                money_spent = play(current_pet.name)
                user_money -= money_spent
                changes = True
                the_time += 1
                # Call time check when it's built (in helpers file)
            elif choice == "3":
                # Sleep
                money_spent = sleep(current_pet.name)
                user_money -= money_spent
                changes = True
                the_time += 1
                # Call time check when it's built (in helpers file)
            elif choice == "4":
                # Show stats
                print(f"{current_pet.name}'s Stats:")
                print(current_pet)
            elif choice == "5":
                # Manage
                # BUILD
                pass
            elif choice == "6":
                # Save
                # BUILD
                pass
            elif choice == "7":
                # Leave
                if changes == True:
                    while True:
                        will_save = input("It seems that things have changed. Would you like to save these changes? (YES/NO)").strip().upper()
                        if will_save == "YES":
                            # Call save function when built
                            # BUILD
                            pass
                        elif will_save == "NO":
                            break
                        else:
                            print("Invalid input. Please enter YES or NO")
                            continue
                return
                
            else:
                print("Invalid input. Try again")
                continue
    
    # Welcome part and pet selection
    print("Welcome User to Pet Simulator!\n")
    while True:
        type_print("Would you like to\n1) Make New Pet\nor\n2) Load Pet")
        action = input("Enter the number corresponding to what you want to do\n")
        if action == "1":
            current_pet = make_pet()
            # BUILD
            # write the pet to CSV
            break
        elif action == "2":
            # BUILD
            # check if pets saved in CSV
            # If yes, show and have select
            pass
        else:
            print("Invalid input. Try again")
            continue

    # Moving on to letting the user do things with their pet
    action_main()
    
    # this should happen if the user leaves from action_main
    print("Continue taking good care of your pet when you come back!")
    return