def student_grade():
    grade_counter = 1
    while grade_counter <= 3:
        grade = int(input("Enter a student grade: "))
        while grade < 0 or grade > 100:
            print("Invalid input!")
            grade = int(input("Enter a student grade: "))
        if 90 <= grade <= 100:
            print("Your grade is A")
        elif 70 <= grade <= 89:
            print("Your grade is B")
        elif 50 <= grade <= 69:
            print("Your grade is C")
        elif 40 <= grade <= 49:
            print("Your grade is D")
        elif 30 <= grade <= 39:
            print("Your grade is E")
        else:
            print("Zero talent!")
        grade_counter += 1



