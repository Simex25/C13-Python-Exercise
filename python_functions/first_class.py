class BioData:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __set_name__(self, name):
        self.name = name

    def __get_name__(self):
        return self.name

    def __set_age__(self, age):
        self.age = age

    def __get_age__(self):
        return self.age
