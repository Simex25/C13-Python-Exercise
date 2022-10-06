# count = 1
# counter = 0
# while count <= 5:
#     num1 = int(input('Enter your score'))
#     if num1 < 0 or num1 > 100:
#         print('Not correct: enter a valid number!')
#         counter += 1
#     else:
#         grade = 0
#         if 90 <= num1 <= 100:
#             print("You graded A")
#         elif 70 <= num1 < 90:
#             print("You are graded B")
#         elif 50 <= num1 < 70:
#             print("You are graded C")
#         elif 40 <= num1 < 50:
#             print('You are graded D')
#         elif 30 <= num1 < 40:
#             print('You are graded E')
#         else:
#             print('fail')
#             count += 1
#             print(f'Grade is {grade}')
#             break

def first_function():
    counter = 0
    while counter < 3:
        num1 = int(input('Enter your grade: '))
        print(f'Your grade is %d' % num1)
        if 90 <= num1 <= 100:
            print("You graded A")
        elif 70 <= num1 < 90:
            print("You are graded B")
        elif 50 <= num1 < 70:
            print("You are graded C")
        elif 40 <= num1 < 50:
            print('You are graded D')
        elif 30 <= num1 < 40:
            print('You are graded E')
        else:
            print("\nfail: ZERO TALENT")
            counter += 1
            print('Goodbye')
            break


if __name__ == '__main__':
    first_function()
