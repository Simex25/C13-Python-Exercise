class FirstClass:
    """create a constructor """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        '''To make a function static'''

    def first_func(self, name):
        print(name)

    '''To set and get'''

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


