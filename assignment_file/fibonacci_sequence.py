def fibonacci_sequence(n):
    if n < 0:
        print("Cannot find the fibonacci of a negative number.")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == '__main__':
    number = int(input("Enter an integer: "))

    result = fibonacci_sequence(number)
    print("Fibonacci (%d) = %d" % (number, result))