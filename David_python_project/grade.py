def student_grade():
    counter = 1

    while counter <= 3:
        grade = int(input("Enter a grade: "))

        if 90 <= grade <= 100:
            print("A")
            break
        elif 70 <= grade <= 89:
            print("B")
            break
        elif 50 <= grade <= 69:
            print("C")
            break
        elif 40 <= grade <= 49:
            print("D")
            break
        elif 30 <= grade <= 39:
            print("E")
            break
        elif 0 <= grade <= 29:
            print("F\nZero Talent")
            break
        elif grade < 0 or grade > 100:
            print("\nInvalid grade entered!!!.\n\nEnter a grade again:")
            counter += 1


if __name__ == '__main__':
    student_grade()
