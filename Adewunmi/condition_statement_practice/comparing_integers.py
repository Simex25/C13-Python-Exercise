if __name__ == '__main__':
    """Comparing integers using if statements and comparison operators."""

    print("Enter two numbers to display the relationship them share")

    number1 = int(input("Enter the first number: "))

    number2 = int(input("Enter the second number: "))

    if number1 > number2:
        print(f'{number1} > {number2}')
    elif number2 > number1:
        print(f'{number2} > {number1}')
    elif number2 < number1:
        print(f'{number1} < {number2}')
    elif number2 < number1:
        print(f'{number2} < {number1}')
    else:
        print(f'{number2} == {number1}')
