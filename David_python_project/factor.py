# if __name__ == '__main__':
#     number = int(input('Enter the number: '))
#     total = 0
#     counter = 1
# while counter < number:
#     if number % counter == 0:
#         total = total + counter
#         print(counter)
#
#     counter += 13
# print(f"Total is: {total}")

if __name__ == '__main__':
    user_input = int(input("Enter a number-: "))
    total_sum = 0

    for x in range(1, user_input):
        print(x)
        if user_input % x == 0:
            print("User Input", user_input, "X value: ", x)
            total_sum += x
            print("Total -->", total_sum)

    print("Total sum == ", total_sum)
    if total_sum == user_input:
        print("This is the perfect number-:")
    else:
        print("Zero talent ")
