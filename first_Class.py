class first_Class:

# declaring a constructor

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @staticmethod
    def set_name(name):
        return name

    def get_name():
        return self.name

    def set_age(self, age):
        if age > 18:
            self.age = age

    def get_age():
        return self.age

if __name__ == '__main__':

    class1 = first_Class('Jude', 27)

    print(class1.get_name())




