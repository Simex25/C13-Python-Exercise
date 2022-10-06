def double(x):
    x *= 2
    return x


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    for counter in range(1, 4):
        number = double(number)
        print(number)
