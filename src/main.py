# LD 1st Pet Simulator Personal Project
from helpers import *
from actions import *
from classes import PetCreator
import random

# First, welcome the user and have them either load a pet or create a pet
# Show the user their pet's stats and have them select an action

def main():
    # Reading the CSV to get saved information relating to the user and what has happened
    try:
        with open("docs/user_info.csv", "r") as file:
            reader = csv.DictReader(file)
            row = next(reader) # read header
            the_time = int(row['hour'])
            the_day = int(row['day'])
            user_money = int(row['money'])
    except Exception as inst:
        print(inst)
        print("Could not read file in getting the user variables")
    # This will be used to know if I should recomend the user save if they leave without having saved
    changes = False
    current_pet = ''

    def action_main():
        nonlocal current_pet
        nonlocal the_time
        nonlocal the_day
        nonlocal user_money
        nonlocal changes
        clear_screen()

        print(f"Current pet: {current_pet.name}({current_pet.species}) | Time: {the_time}:00 | Current Balance: ${user_money}")
        print(current_pet)
        while True:
            trigger_num = random.randint(1, 9)
            # Trigger a random event using random
            # Hope this works
            if trigger_num == 3:
                event = current_pet.found_toy()
                print(event)
                changes = True
            elif trigger_num == 7:
                event = current_pet.found_food()
                print(event)
                changes = True
            elif trigger_num == 5:
                event = current_pet.got_sick()
                print(event)
                changes = True

            # Check if the pet has a birthday! (age them up a month, only doing this every 28 days because that is easier math)
            if the_day % 28 == 0:
                current_pet.birthday()
            
            type_print(f"What would you like to do with {current_pet.name}:\n1) Feed {current_pet.name}\n2) Play with {current_pet.name}\n3) Put {current_pet.name} to Sleep\n4) Check {current_pet.name}'s Statuses\n5) Manage your Pets\n6) Save\n7) Leave Program\n")
            choice = input(f"Type the number corresponding to your action (NOTE: You have ${user_money} remaining):\n")
            if choice == "1":
                # Feed
                money_spent = feed(current_pet)
                user_money -= money_spent
                the_time += 1
                # Call time check when it's built (in helpers file)
                day_add = check_time(the_time)
                if day_add == 1:
                    the_day += 1
                changes = True
            elif choice == "2":
                # Play
                money_spent = play(current_pet)
                user_money -= money_spent
                the_time += 1
                # Call time check when it's built (in helpers file)
                day_add = check_time(the_time)
                if day_add == 1:
                    the_day += 1
                changes = True
            elif choice == "3":
                # Sleep
                money_spent = sleep(current_pet)
                user_money -= money_spent
                the_time += 1
                # Call time check when it's built (in helpers file)
                day_add = check_time(the_time)
                if day_add == 1:
                    the_day += 1
                changes = True
            elif choice == "4":
                # Show stats
                print(f"{current_pet.name}'s Stats:")
                print(current_pet)
            elif choice == "5":
                # Manage
                location = manage(current_pet)
                if location == 0:
                    # user coming from just leaving the manage function
                    continue
                elif location == 1:
                    # user is coming from switching pets and I am making them load a pet to switch
                    return
                else:
                    print("What happened to my code in action_main manage part???")
            elif choice == "6":
                # Save
                save_pet(current_pet)
                save_user(user_money, the_time, the_day)
                print("Data Saved!")
            elif choice == "7":
                # Leave
                if changes == True:
                    while True:
                        will_save = input("It seems that things have changed. Would you like to save these changes? (YES/NO)").strip().upper()
                        if will_save == "YES":
                            # Call save functions
                            save_pet(current_pet)
                            save_user(user_money, the_time, the_day)
                            break
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
        type_print("Would you like to\n1) Make New Pet\nor\n2) Load Pet\n")
        action = input("Enter the number corresponding to what you want to do\n")
        if action == "1":
            current_pet = make_pet()
            # write the pet to CSV
            try:
                with open("docs//pet_data.csv", "a", newline='') as csv_file:
                    fieldnames = ['name','species','age','hunger','happieness','energy']
                    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                    writer.writerow({'name': current_pet.name, 'species': current_pet.species, 'age': current_pet.age, 'hunger': current_pet.hunger, 'happieness': current_pet.happieness, 'energy': current_pet.energy})
            except:
                print("Could not open file in action_main making a pet")
            break
        elif action == "2":
            # check if pets saved in CSV
            try:
                with open("docs//pet_data.csv", "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    # If no error is thrown, save the pets in a list to be printed for the user
                    pets = []
                    for line in content:
                        pets.append({headers[0]: line[0], headers[1]: line[1],headers[2]: line[2],headers[3]: line[3],headers[4]: line[4],headers[5]: line[5]})
            except Exception as instant:
                print(instant)
                print("Could not open file in main to see if there is at least one pet")
                continue
            # Check if the pets list is empty. If it is, there are no pets to load
            if pets:
                type_print("Here are the pets you can load from:\n")
                for item in pets:
                    type_print(f"- Name: {item['name']}, Species: {item['species']}, Age: {item['age']}\n")
                # Now that options are shown, have user give name and species
                while True:
                    load_name = input("Enter the name of the pet you would like to load:\n").strip().title()
                    load_species = input("Enter the species of the pet you would like to load:\n").strip().title()
                    # Info obtained, now find that pet in the csv and save that information. We can then take the CSV info and pass it into PetCreator and set that as current pet
                    try:
                        with open("docs//pet_data.csv", "r", newline='') as the_file:
                            the_content = csv.reader(the_file)
                            the_headers = next(the_content)
                            for line in the_content:
                                if line[0] == load_name and line[1] == load_species:
                                    the_name = line[0]
                                    the_species = line[1]
                                    pet = PetCreator(the_name, the_species, line[2], line[3], line[4], line[5])
                                    current_pet = pet
                                    break
                                else:
                                    continue
                            if current_pet == '':
                                # Made it through the for loop and now want to see if a current pet was even established to know if I should inform the user of spelling errors
                                print("Could not find that pet you typed in. Please check spelling and capitalization")
                                continue
                            else:
                                # get out of loading while loop
                                break
                    except:
                        print("Could not open file in main and getting info for the loaded pet")
                    break
                # get out of big action selection while loop
                break
            else:
                print("It seems that you have no pets to load from. Create a pet first!")
                continue
        else:
            print("Invalid input. Try again")
            continue

    # Moving on to letting the user do things with their pet
    action_main()
    
    # this should happen if the user leaves from action_main
    print("Continue taking good care of your pet when you come back!")
    return

main()