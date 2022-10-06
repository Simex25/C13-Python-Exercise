if __name__ == '__main__':
    number = int(input("Enter a number: "))
    print(f"Factors of {number} are:")
    count = 1
    factor_total = 0
    while count < number:
        if number % count == 0:
            factor_total += count
            print(count, end=' ')

        count += 1

    print(f"Sum of the factors of {number} is {factor_total}")

    if number == factor_total:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")
