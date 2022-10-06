from David_python_project.Class import cohortThirteen

if __name__ == '__main__':
    new_object = cohortThirteen("David", 90)

    print(new_object.get_name())
    new_object.__set_name__("Fil here Fill here")

    # Note that when we used static method in set name
    # iIt gives us the argument in the constructor since it is static and cannot be changed
    print(new_object.get_name())

    print(new_object.get_age())
    new_object.__set_age__(27)
    print(new_object.get_age())