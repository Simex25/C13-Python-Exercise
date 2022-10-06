from Nneka.pascal import First_name

if __name__ == '__main__':
    papi = First_name("jude", 26)

    print(papi.get_name(), papi.get_age())

    papi.set_name("john")
    print(papi.get_name())
''