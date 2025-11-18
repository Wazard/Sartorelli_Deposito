class Animal:
    def __init__(self, name: str, age: int, sound: str = "Generic sound"): # accepts respectively string int and string (last being optional)
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self): # plays sound
        return f"{self.sound}!"

    def describe_peculiarity(self): # describes peculiarity
        return "Is alive"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"


class Lion(Animal):
    def __init__(self, name: str, age: int, hunt_method: str, sound = "Roar"): # accepts father's inputs + str for hunting method
        super().__init__(name, age)
        self.hunt_method = hunt_method

    def describe_peculiarity(self):
        return f"{self.name} hunts by {self.hunt_method}"


class Penguin(Animal):
    def __init__(self, name: str, age: int, swim_speed: float, sound = "Honk"): # accepts father's inputs + int for speed
        super().__init__(name, age, sound)
        self.swim_speed = swim_speed

    def describe_peculiarity(self):
        return f"{self.name} swims at {self.swim_speed} m/s"


class Giraffe(Animal):
    def __init__(self, name, age, sound = "Hum"):
        super().__init__(name, age, sound)


lion = Lion("Alex", 5, hunt_method="dancing and performing")
giraffe = Giraffe("Melman", 7)
penguin = Penguin("Riko", 3, swim_speed=2.5, sound= "Kaboom")

animals = [lion, giraffe, penguin]

for animal in animals:
    print(f"{animal.name} ({animal.age} years old) says: {animal.make_sound()}")

for animal in animals:
    print(animal.describe_peculiarity())