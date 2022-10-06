class first_class:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def first_function(self, name):
        self.name = name

    def age_function(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
