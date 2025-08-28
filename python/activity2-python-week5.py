class Animal:
    def move(self):
        print("Animals can move in different ways.")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")

class Bird(Animal):
    def move(self):
        print("The bird flies 🕊️")

# Polymorphism in action
animals = [Dog(), Fish(), Bird()]

for a in animals:
    a.move()
