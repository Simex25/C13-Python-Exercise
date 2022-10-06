if __name__ == '__main__':
    name = input("Enter patient' name: ")
    age = int(input("Enter your age: "))
    max_heart_rate = 220 - age
    target_heart_rate = max_heart_rate * 0.85
    print("The Patient's name: %s\nPatient's age: %d\nMax Heart Rate: %d\nTarget Heart Rate: %.2f" % (name, age, max_heart_rate, target_heart_rate))
