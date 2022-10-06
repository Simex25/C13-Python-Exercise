if __name__ == '__main__':
    user_input = int(input("Enter an integer: "))
    i = 1
    sum = 0
    while i < user_input:
        if user_input % i == 0:
            print("The factor of the number is", i)
            sum += i

        i+=1
    print(" ")
    print("The sum of the factor is: ", sum)

if sum == user_input:
    print("The number is a perfect number")
else:
    print()
    print("not a perfect number")