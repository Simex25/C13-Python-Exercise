if __name__ == '__main__':
    number = int(input("Enter a number"))
    reverse = 0
    i = number
    while i > 0:
        digit = i % 10
        reverse = reverse * 10 + digit
        i = i // 10

        print(digit, end=" ")
