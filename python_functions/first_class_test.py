from chapter_four.first_class import BioData

if __name__ == '__main__':

    sam = BioData("Ade", 34)
    print("Initial Record: ", sam.__get_name__(), sam.__get_age__())
    sam.__set_name__("Samuel")
    sam.__set_age__(54)
    print("New Record:", sam.__get_name__(), sam.__get_age__())