if __name__ == '__main__':
    number = int(input("Enter a number: "))
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end='')