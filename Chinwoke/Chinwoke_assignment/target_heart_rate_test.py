from Assignments.target_heart_rate import target_heart_rate

if __name__ == '__main__':
    patient_profile = target_heart_rate(21)
    patient_profile.set_age(int(input("Enter your age: ")))
    print(f'patient age is {patient_profile.get_age()}')
    print(f'the patient maximum heart rate is {patient_profile.get_maximum_heart_rate()}')
    print(f'{patient_profile.get_target_rate()}')

