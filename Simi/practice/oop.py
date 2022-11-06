class Dog:
    specie = "canis familiars"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old")

    def sound(self, sound):
        print(f"{self.name} sound is {sound}")

    def coat_colour(self, colour):
        print(f"{self.name}'s coat colour is {colour}")


class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        if mileage > 0:
            self.mileage = mileage

    def drive(self, mileage):
        return mileage


class GoldenRetriever(Dog):
    def speak(self, sound="bark"):
        return sound


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

