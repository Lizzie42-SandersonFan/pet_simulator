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
        value += amount
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        setattr(self, item, value)

    def found_toy(self):
        self.happieness += 10
        if self.happieness > 100:
            self.happieness = 100
        elif self.happieness < 0:
            self.happieness = 0
        return f"{self.name} found a toy! {self.name}'s happiness increased!"
    
dog = PetCreator("Buddy", "Dog", 0, 50,50,50)
print(dog)
dog.update_thing("happieness", 10)
print(dog)