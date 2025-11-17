from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow meow"

class Pig(Animal):
    def make_sound(self):
        return "Oink oink"

class Horse(Animal):
    def make_sound(self):
        return "Yeeh"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
