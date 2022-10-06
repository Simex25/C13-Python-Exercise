class cohortThirteen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __set_name__(name):
        # static method doesn't allow self
        return name

    def __set_age__(self, age):
        self.age = age

    def get_name(self):
        return  self.name

    def get_age(self):
        return self.age


# if __name__ == '__main__':
#     first_class.first_function()
#     first_class.age_function()
