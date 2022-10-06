# If one inch of rain falls on an acre of land,
# how many gallons of water have accumulated on that acre?

import math
from decimal import Decimal
import statistics

if __name__ == '__main__':
    # area = 4046
    # depth = 0.0254
    # volume = area * depth
    # gallons = volume * 264.172
    #
    # print(gallons)
    # x = 13 / 4
    # print(x)
    #
    # number = int (input("Input a number between 1 an 10 "))
    # square = number * number
    # print (square)
    #
    # grade = int(input("Enter Grade: "))
    # if grade >= 90:
    #     print ('Congratulations! your grade of', grade, 'earns you an \'A\' in this course')


    # r = int(input('Enter a number: '))
    # total = 0
    #
    #       -- WHILE LOOP --
    # n = 1
    # print("The factors of {} are: ".format(r), end='')
    # while n <= r:
    #     if r % n == 0:
    #         total = total + n
    #         print(n, ' ', end='')
    #     n = n + 1
    # print("\nSum of the factors of {} = {}".format(r, total))
    # if r == total:
    #     print ('{} is a perfect number'.format(r))
    # else:
    #     print ('{} is not a perfect number'.format(r))
    #
    #        -- FOR LOOP --
    # print("The factors of {} are: ".format(r), end='')
    # for n in range (1, r):
    #     if r % n == 0:
    #         total += n
    #         print(n, ' ', end='')
    # print("\nSum of the factors of {} = {}".format(r, total))
    # if r == total:
    #     print ('{} is a perfect number'.format(r))
    # else:
    #     print ('{} is not a perfect number'.format(r))


    # i = 0
    # total = 0
    # passes = 0
    # fail = 0
    # grade = int(input('enter grade: '))
    #
    # y = Decimal('4')
    # x = Decimal('7')
    # t = y / x
    # print(t)


    # principal = Decimal(input("Enter amount invested: "))
    # rate = Decimal(5/100)
    # total = 0
    # for year in range(1, 11):
    #     amount = principal * (1 + rate) ** year
    #     profit = amount - principal
    #     principal = amount
    #     total += profit
    #     print(f"{profit:>.2f}")
    # print(f'\n{total:>.2f}')
    #
    # # statistics.mean()
    # # statistics.median()
    # # statistics.mode()

    ## EXERCISE 3.6
    # problem = input('What is ypur problem?  ')
    # diagnosis = input('Have you had this problem before (yes or no)? ')
    # if diagnosis == 'yes':
    #     print('Well, you have it again.')
    # elif diagnosis == 'no':
    #     print('Well, you have it now')


    # # EXERCISE 3.7
    # print("Hour\t Number of Bacteria")
    # for n in range(0, 16, 5):
    #     B = 200 * 2 ** n
    #     # print (n, '\t\t', B)
    #     print(f"{n:>4}\t\t{B:>15}")


    # # EXERCISE 3.8
    # total = 0
    # maximum = 0
    # minimum = 100
    # for x in range(1, 8):
    #     record = int(input(f'Number of infections recorde for day{x}: '))
    #     total += record
    #     average = total / x
    #     minimum = min(minimum, record)
    #     maximum = max(maximum, record)
    # print(f'\nTotal infaction for the week = {total}\nAverage = {average}'
    #       f'\nHighest daily infection recorded = {maximum}'
    #       f'\nLowest daily infection recorded = {minimum}')


    # # EXERCISE 3.11
    # total = 0
    # t_doe = 0
    # doe = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
    # n = 1
    # while doe != -1:
    #     birthrate = (n ** 1.5) + 1
    #     number_of_baby_rabbits = int(doe  * birthrate)
    #     total += number_of_baby_rabbits
    #     t_doe += doe
    #     print(f'On average {birthrate:>.1f} baby rabbits were born for each doe')
    #     print(f'Number of baby rabbits born in the past month: {number_of_baby_rabbits}\n')
    #     doe = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
    #     n += 1
    # print(f'Total number of baby rabbits for each doe so far: {total / t_doe:>.3f}')

    # EXERCISE 3.15
    first_number = 0
    # for n in range (1, 10):
    #     print(f'{n}')

    f = [5, 3, 9, 0, 1]
    temp = 0
    for i in range(0, len(f)):
        for j in range(1, len(f)):
            if f[j] < f[i]:
                temp  = f[j]
                f[j] = f[i]
                f[i] = temp

    print(4 / 3)
