if __name__ == '__main__':
    guess = int(input("Guess a number: "))

    number = 45

    while 0 <= guess or guess <= 100:
        if guess < number:
            print("Too low!!!\nRe-run the app and try again later. Thank you.")

            # It gives me infinite loop without including the break
            break
        elif guess > number:
            print("Too high!!!\nRe-run the app and try again later. Thank you.")
            break
        elif guess == number:
            print("Correct guess\nYour precision was right, keep it up\nYou can also run the app again.")
            break
