if __name__ == '__main__':
    total = 0
    smallest = 0
    largest = 0
    day = 1
    while day <= 7:
        number = int(input("Enter number of reported infected for each day: ", ))
        if number > total:
            smallest = number
        else:
            largest = number
        total = total + day
        day += 1
    average = total / day
    print("The total report infected for the week is %d" % total)
    print("The average report infected for the week is %d" % average)
    print("The smallest report infected for the week is %d" % smallest)
    print("The largest report infected for the week is %d" % largest)
