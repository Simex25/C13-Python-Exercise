if __name__ == '__main__':
    number_of_egg = int(input("Enter the number of egg: "))
    box = number_of_egg // 6
    reminder = number_of_egg % 6
    new_box = 6 - reminder
    if reminder == 0:
        print(f"{box}boxes are needed.")
    else:
        print(f"{box} boxes are needed with a reminder of {reminder} eggs")
        print(f"{new_box} eggs are needed are to complete the box.")
