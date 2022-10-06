def student_grade():
    score = ""
    grade = 0
    count = 0
    counter = 0
    while counter < 5:
        grade = int(input('Enter the student grade: '))
        if grade < 0 or grade > 100:
            print('Invalid grade')
            count += 1
        else:
            print(f'\nYour grade is --> {score}', end='')
            if 90 <= grade <= 100:
                print('A')
            elif 70 <= grade <= 89:
                print('B')
            elif 60 <= grade <= 69:
                print('C')
            elif 50 <= grade <= 59:
                print('D')
            elif 39 <= grade <= 49:
                print('E')
            elif 0 <= grade < 39:
                print("Zero talent")
        # print(f'\nYour grade is {score}')
        counter += 1

        if count == 3:
            print('Too many incorrect grade')
            break


if __name__ == '__main__':
    student_grade()
