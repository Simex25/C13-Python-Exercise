
if __name__ == '__main__':
    array = []
    total = 0
    for number in range(7):
        user_inputs = int(input(f'Enter the number of reported infected people for day {number + 1} '))
        array.append(user_inputs)

    print(f'The sum_total of the values is { sum(array)} ')
    print(f'The average of the values is %.2f' % (sum(array) / len(array)))
    print(f'The minimum of the values is %d' % (min(array)))
    print(f'The maximum of the values is %d' % (max(array)))
