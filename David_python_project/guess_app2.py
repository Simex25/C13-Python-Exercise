if __name__ == '__main__':
    number = 45
    counter = 1

while counter > 0:
    guess_number = int(input("Please enter  the guess number: "))
    if guess_number > number:
        print("Too high, try again!!!")
    if guess_number < number:
        print("Too low, try again!!!")
    elif guess_number == number:
        print("Perfect number entered\nGood try")
        break
    counter += 1
