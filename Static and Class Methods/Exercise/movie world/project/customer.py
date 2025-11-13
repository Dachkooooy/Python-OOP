from gym.project import DVD

class Customer:
    def __init__(self, name:str, age:int, c_id:int):
        self.name = name
        self.age = age
        self.id = c_id
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        dvd_names = ', '.join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvd_names})"