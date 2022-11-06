if __name__ == '__main__':

    user_input = 0
    number = 70
    count = 0

    while user_input != -1:
        user_input = int(input("Guess the number between 1 and 100  :"))
        if user_input > number:
            print("Too high")
        elif user_input < number:
            print("Too low")
        elif user_input == number:
            print(f"Wow you got it right the number is {number}")
            break
        if user_input == 67:
            print("Owww close, go little high")
        if user_input == 72:
            print("Owww close, go a little lower")
        count = count + 1
        if count == 3:
            user_input = int(input("Enter any number to continue or -1 to quit:"))
        if count == 10:
            print("You should be able to do better")
            if user_input == 1:
                continue
            elif user_input == -1:
                print("Better luck next time")
                break
            else:
                user_input = int(input("Enter any number to continue or -1 to quit:"))

