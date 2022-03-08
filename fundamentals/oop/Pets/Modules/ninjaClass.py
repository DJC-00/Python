class Ninja:
    def __init__(self, firstName, lastName, pet, treats = 20, petFood = 100):
        self.firstName = firstName
        self.lastName = lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood

    def walk(self):
        print(f"Taking {self.pet.petName} for a walk!")
        self.pet.play();

    def feed(self):
        print(f"Feeding {self.pet.petName}.")
        self.pet.eat()

    def bathe(self):
        print(f"Giving {self.pet.petName} a bath!")
        print(f"{self.pet.petName} {self.pet.noise()}s in annoyance")