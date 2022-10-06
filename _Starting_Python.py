
if __name__ == '__main__':

    import math

    # calculate the area and circumference of a circle from its radius
    # step 1: prompt for a radius
    # step 2:
    # directly receiving input from user and assigning it to variable 'radius'

    i = 2
    factor = 0
    total = 0

    number = int(input('enter a number: '))
    while i < number:
        factor = number / i
        total = total + factor
        i += 2
        print('factor is: ', int(factor))
        print()
        print('total is: ', int(total))

    print()
    print('The sum of the factor is: ', int(total))

    print()
    if number == total:
        print('Perfect number')
    elif number != total:
        print('invalid')



