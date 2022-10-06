if __name__ == '__main__':
    number = int(input("Enter a number: "))
    total = 0
    print("the factors are: ", end=' ')
    for i in range(1, number):
        if number % i == 0:
            print("\nFactor", i, end=' ')
            total += i
    print("\nSum of factors is: ", total)
    if number == total:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number !")
