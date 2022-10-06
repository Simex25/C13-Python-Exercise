if __name__ =='__main__':
    factor_name = input("Enter number")
    number = int(factor_name)   # casting in python

    i = 1
    sum = 0
    while i < number:

        if number % i == 0:
            print("The factor of the number: ",i)
            sum += i
        i += 1

    print("")
    print("The sum of the factor is: ", sum)

    if sum == number:
        print("The number is a perfect number ")
    else:
        print()
        print("The number is not a perfect number")















