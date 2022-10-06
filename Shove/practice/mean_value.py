"""evaluate integers if statements and arithmetic operator"""
if __name__ == '__main__':
    print('Enter three numbers, and i will tell you', 'the mean of the values')

    number1 = int(input('Enter first integer: '))

    number2 = int(input('Enter second integer: '))

    number3 = int(input('Enter third integer: '))

    total = number1 + number2 + number3
    mean = total / 3
    print('The mean is: ', mean)
