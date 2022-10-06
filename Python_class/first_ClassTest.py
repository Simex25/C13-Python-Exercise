from Python_class.First_class import First_class

if __name__ == '__main__':
    bug = First_class("james", 21)

    print(bug.get_name(), bug.get_age())

    bug.set_name("peekaboo")
    print(bug.get_name())
