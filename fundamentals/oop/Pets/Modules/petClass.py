class Pet:
    def __init__(self, petName, type, sound, health = 100, energy = 100):
        self.petName = petName
        self.type = type
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
        super().__init__(petName, type, sound)
        self.petName = petName
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.breed = breed
    

class Cat(Pet):
    def __init__(self, petName, type = "Cat", sound = "Meow", health = 100, energy = 100):
        super().__init__(petName, type, sound)
        self.petName = petName
        self.type = type
        self.health = health
        self.energy = energy

class Hamster(Pet):
    def __init__(self, petName, type = "Hamster", sound = "Squeel", health = 100, energy = 100):
        super().__init__(petName, type, sound)
        self.petName = petName
        self.type = type
        self.health = health
        self.energy = energy