# LD Classes needed

class PetCreator:
    def __init__(self, name, species, age, hunger, happieness, energy):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.happieness = happieness
        self.energy = energy
    
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age} Months\nHunger: {self.hunger}\nHappieness: {self.happieness}\nEnergy: {self.energy}\n"
    
    def update_hunger(self, amount):
        self.hunger += amount
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0

    def update_happy(self, amount):
        self.happieness += amount
        if self.happieness > 100:
            self.happieness = 100
        elif self.happieness < 0:
            self.happieness = 0

    def update_energy(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        elif self.energy < 0:
            self.energy = 0