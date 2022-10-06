class target_heart_rate:
    def __init__(self, age):
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def get_maximum_heart_rate(self):
        return 220 - self.get_age()
        # return self.maximum_heart_rate

    def get_target_rate(self):
        heart = 50 * self.get_maximum_heart_rate()
        rate = 85 * self.get_maximum_heart_rate()
        return "the target heart rate is: ", heart, rate
