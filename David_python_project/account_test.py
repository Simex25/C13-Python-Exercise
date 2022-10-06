from David_python_project.Account import account

if __name__ == '__main__':
    new_object = account("David", 300)
    print(new_object.get_name())
    new_object.set_name("Temz")
    print(new_object.get_name())

    print(new_object.get_balance())
    new_object.set_balance(400)
    print(new_object.get_balance())