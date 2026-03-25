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

    def update_thing(self, item, amount):
        # `item` is the name of the attribute to change (e.g. 'happieness', 'hunger', 'energy')
        # Use getattr/setattr so we modify the actual attribute, and clamp to [0, 100].
        if not hasattr(self, item):
            raise AttributeError(f"Pet has no attribute '{item}'")
        value = getattr(self, item)
        num_value = int(value)
        num_value += amount
        if num_value > 100:
            num_value = 100
        elif num_value < 0:
            num_value = 0
        setattr(self, item, num_value)

    def found_toy(self):
        self.update_thing("happieness", 15)
        return f"{self.name} found a toy! {self.name}'s happieness increased!"
    
    def found_food(self):
        self.update_thing("hunger", -10)
        self.update_thing("happieness", 5)
        return f"{self.name} found a treat! {self.name}'s happieness increased!"
    
    def got_sick(self):
        self.update_thing("energy", -20)
        self.update_thing("happieness", -15)
        return f"{self.name} got sick! {self.name}'s energy and happieness decreased!"
    
    def birthday(self):
        self.age += 1
        return f"{self.name} had a birthday! {self.name} is now {self.age} month(s) old!"