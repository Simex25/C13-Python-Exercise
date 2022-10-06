if __name__ == '__main__':
    print('Enter a number and i will tell the factors')

    numbers = int(input('Enter an integer: '))
   # print(f"Factors of {numbers} are:", end=' ')

    user_input = numbers
    count = 1
    sum_count = 0

    while count < numbers:
        if numbers % count == 0:
            print("The factors of the numbers", numbers, "is", count)
            sum_count = sum_count + count
        count = count + 1
    print("The sum is: ", sum_count)
    if sum_count == numbers:
        print("The number is perfect")
    else:
        print("The number is not perfect")
