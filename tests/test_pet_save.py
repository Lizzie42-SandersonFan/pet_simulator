import csv
import os
import random
from classes import PetCreator

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

def make_pet():
    the_name = input("Enter the name for your pet:\n").strip().title()
    the_species = input("Enter the species for your pet:\n").strip().title()
    pet = PetCreator(the_name, the_species, 0, random.randint(1,100), random.randint(1,100), random.randint(1,100))
    return pet

test_pet = make_pet()
save_pet(test_pet)