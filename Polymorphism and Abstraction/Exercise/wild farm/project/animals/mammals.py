from animals.project import Mammal
from animals.project import Meat, Vegetable, Fruit, Seed

class Mouse(Mammal):
    @property
    def weight_increment(self):
        return 0.10

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

class Dog(Mammal):
    @property
    def weight_increment(self):
        return 0.40

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):
    @property
    def weight_increment(self):
        return 0.30

    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    @staticmethod
    def make_sound():
        return "Meow"

class Tiger(Mammal):
    @property
    def weight_increment(self):
        return 1.0

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
