import decimal


class first_assignment:

    @staticmethod
    def fill_in_the_gap():
        grade = int(input('Enter grade: '))
        if grade >= 90:
            print(f'Congratulations! Your grade of {grade} earns you an A in this course.')
        else:
            print('Good try, you can always do better')

    @staticmethod
    def multiplication_table():
        factor = 1
        while factor <= 12:
            for number in range(1, 13):
                value = factor * number
                print(f'{value:>5}', end='  ')
            print('')
            factor += 1

    @staticmethod
    def hourly_wage_calculator():
        """
        w = new hourly wage
        o = original hourly wage
        p = percentage increase or decrease
        n = number of years
        """
        p = 0.03
        o = float(input("Employee's wage: "))
        n = int(input('Hou many years has this employee worked: '))
        remark = input("Has this employee been of good performance or suboptimal\n"
                       "Press 'G' for good performance or 'S' for suboptimal -> ")
        if remark == 'G':
            w = o * ((1 + p) ** n)
            print(w)
        if remark == 'S':
            w = o * ((1 - p) ** n)
            print(w)

    @staticmethod
    def target_heart_rate_calculator():
        age = int(input('Enter your age: '))
        maximum_heart_rate = 220 - age
        print(f'According to the American Heart Association AHA your maximum heart rate is {maximum_heart_rate}bpm')
        minimum_heart_target = 0.50 * maximum_heart_rate
        maximum_heart_target = 0.85 * maximum_heart_rate
        print(f'Your target heart rate ranges between {minimum_heart_target} and {maximum_heart_target}')

    @staticmethod
    def flu_patient_data():
        total = 0
        maximum = 0
        minimum = 100
        for x in range(1, 8):
            record = int(input(f'Number of infections recorde for day{x}: '))
            total += record
            average = total / x
            minimum = min(minimum, record)
            maximum = max(maximum, record)
        print(f'\nTotal infection for the week = {total}\nAverage = {average}'
              f'\nHighest daily infection recorded = {maximum}'
              f'\nLowest daily infection recorded = {minimum}')

    @staticmethod
    def triangle():
        side_lengths = [0, 0, 0]
        for side in range(0, 3):
            length = int(input('Enter the length of the sides of a triangle: '))
            side_lengths[side] = length
        if side_lengths[0] == side_lengths[1] and side_lengths[1] == side_lengths[2]:
            print('The triangle is an equilateral triangle')
        else:
            print('The triangles is not equilateral')

    @staticmethod
    def refactor():
        number = input('Enter a number: ')
        index = len(number) - 1
        while index >= 0:
            print(number[index], end='  ')
            index -= 1

    @staticmethod
    def bacteria_count():
        print("Hour\t Number of Bacteria")
        for n in range(0, 16, 5):
            B = 200 * 2 ** n
            # print (n, '\t\t', B)
            print(f"{n:>4}\t\t{B:>15}")

    @staticmethod
    def turing_test():
        problem = input('What is your problem?  ')
        diagnosis = input('Have you had this problem before (yes or no)? ')
        if diagnosis == 'yes':
            print('Well, you have it again.')
        elif diagnosis == 'no':
            print('Well, you have it now')

    @staticmethod
    def egg_box():
        egg_per_box = 6
        eggs = int(input('How many eggs do you have: '))
        number_of_boxes_needed = eggs // egg_per_box
        eggs_in_incomplete_box = eggs % egg_per_box
        if eggs_in_incomplete_box != 0:
            number_of_boxes_needed += 1
        remainder = 6 - eggs_in_incomplete_box
        print(f'You have {eggs} eggs\nHence you need {number_of_boxes_needed} egg boxes to store them')
        if eggs_in_incomplete_box != 0:
            if eggs_in_incomplete_box > 1:
                print(f'The last box contains {eggs_in_incomplete_box} eggs, '
                      f'you will need {remainder} eggs to complete the box')
            if eggs_in_incomplete_box == 1:
                print(f'The last box contains {eggs_in_incomplete_box} egg, '
                      f'you will need {remainder} eggs to complete the box')

    @staticmethod
    def palindrome():
        number = list(input('Enter a number: '))
        index = len(number) - 1

    @staticmethod
    def fibonacci_sequence():
        print('This is a fibonacci sequence, in which each number is a sum of the two preceding ones\n'
              'The first 10 fibonacci numbers are as follows')
        numbers = list(input('Enter first two numbers separated by comma: '))
        print(f'{len(numbers)}')
        # while var <= 10:
        #     position = int(input('Enter the index to display value\n'
        #                          'NOTE: first number has an index value 0 '))
