def get_grade():
    user_input = int(input("Enter a grade: "))
    counter = 0
    while counter < 3:
        counter += 1
        if user_input < 0 or user_input > 100:
            user_input = int(input("invalid input buffon!, Re-enter a grade:"))
            continue
        else:
            if user_input > 90:
                print("A")
            elif 89 >= user_input >= 70:
                print("B")
            elif 69 >= user_input >= 50:
                print("C")
            elif 49 >= user_input >= 40:
                print("D")
            elif 39 >= user_input >= 30:
                print("E")
            else:
                print("Zero talent")
            break


if __name__ == '__main__':
    get_grade()
