if __name__ == '__main__':
    user_input = int(input("Please enter any value: "))
    print("Result of a given {0} are:".format(user_input))

    for i in range(1, user_input):
        print(i)

        total_sum = 0
        if user_input % i == 0:
            total_sum += i
            print()
            print("user_input is", user_input, "i value is:", i)

        if total_sum == user_input:
            print("The number is perfect")
        else:
            print("The number is not perfect")
