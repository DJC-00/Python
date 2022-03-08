
# class Ninja:
#     def __init__(self, firstName, lastName, pet, treats = 20, petFood = 100):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.pet = pet
#         self.treats = treats
#         self.petFood = petFood

#     def walk(self):
#         print(f"Taking {self.pet.petName} for a walk!")
#         self.pet.play();

#     def feed(self):
#         print(f"Feeding {self.pet.petName}.")
#         self.pet.eat()

#     def bathe(self):
#         print(f"Giving {self.pet.petName} a bath!")
#         print(f"Momo {self.pet.noise()}s in annoyance")

"""
class Pet:
    def __init__(self, petName, type, tricks, sound, health = 100, energy = 100):
        self.petName = petName
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self):
        self.energy += 25;

    def eat(self):
        self.energy +=5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        return self.sound

class Dog(Pet):
    def __init__(self, petName, breed, tricks, type = "Dog", sound = "Woof", health = 100, energy = 100):
        super().__init__(petName,tricks, type, sound)
        self.petName = petName
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.breed = breed
    

class Cat(Pet):
    def __init__(self, petName, tricks, type = "Cat", sound = "Woof", health = 100, energy = 100):
        super().__init__(petName,tricks, type, sound)
        self.petName = petName
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

class Hamster(Pet):
    def __init__(self, petName, tricks, type = "Hamster", sound = "Woof", health = 100, energy = 100):
        super().__init__(petName,tricks, type, sound)
        self.petName = petName
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
"""

from Modules import ninjaClass, petClass

# Momo = Pet("Momo","Dog",["sit", "stay"])
Momo = petClass.Dog("Momo", "Shiba-Inu", ["sit", "stand"])
KitKat = petClass.Cat("KitKat")
Hammy = petClass.Hamster("Hammy")
DJ = ninjaClass.Ninja("DJ","Castle",Momo)
Lyndsay = ninjaClass.Ninja("Lyndsay","IDK",KitKat)
Joe = ninjaClass.Ninja("Joe","Bobberson", Hammy)


DJ.walk()
DJ.feed()
DJ.bathe()
print(Momo.breed)

Lyndsay.bathe()
Joe.bathe()

