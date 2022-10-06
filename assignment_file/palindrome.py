if __name__ == '__main__':
    number = int(input("Enter a number: "))
    temp = number
    count = 0
    while number > 0:
        each_number = number % 10
        count = count * 10 + each_number
        number = number // 10
    if temp == count:
        print("The number is a palindrome!")
    else:
        print("The number is not a palindrome")
