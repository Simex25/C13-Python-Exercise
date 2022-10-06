if __name__ == '__main__':
    """comparing integers using if statement and comparison operation."""
    print('Enter two integers, and i will tell you', 'the relationships they satisfy.')
    number1 = int(input('Enter first integer: '))
    number2 = int(input('Enter second integer: '))
    if number1 == number2:
        print(number1, 'is equal to', number2)
    if number1 != number2:
        print(number1, 'is not equal to', number2)
    if number1 < number2:
        print(number1, 'is less than', number2)
    if number1 > number2:
        print(number1, 'is greater than', number2)
    if number1 <= number2:
        print(number1, 'is less than or equal to', number2)
    if number1 >= number2:
        print(number1, 'is greater than or equal to', number2)

