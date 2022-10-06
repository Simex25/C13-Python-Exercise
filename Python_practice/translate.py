if __name__ == '__main__':
    text = "I like to eat bread and egg"
    new_text = text.replace("a", str(4))
    new_text = new_text.replace("b", str(8))
    new_text = new_text.replace("e", str(3))
    new_text = new_text.replace("l", str(1))
    new_text = new_text.replace("o", str(0))
    new_text = new_text.replace("s", str(5))
    new_text = new_text.replace("t", str(7))

    print(new_text)
