if __name__ == '__main__':
    record = []
    day =1
    while day <= 7:
        numbers_per_day = int(input(f"Enter number of infections for day {day}: "))
        record.append(numbers_per_day)
        day += 1

    print()
    print(f"Total number of infections = {sum(record)}")
    print(f"Average number of infections = %.2f" % (sum(record) / 7))
    print(f"Smallest number of infections = {min(record)}")
    print(f"Largest number of infections = {max(record)}")
