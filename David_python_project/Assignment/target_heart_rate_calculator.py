if __name__ == '__main__':
    age = int(input("Enter your age: "))
    print()

    maximum_heart_rate = 220 - age

    print("Maximum heart rate is: " + str(maximum_heart_rate))

    heart_rate_percentage_range = int(input("Enter heart rate percentage range between 50 and 85"))
    print("Heart rate percentage range is: " +str(heart_rate_percentage_range))

    target_heart_rate = (heart_rate_percentage_range * maximum_heart_rate) / 100
    print("Target heart rate is: " + str(target_heart_rate))
