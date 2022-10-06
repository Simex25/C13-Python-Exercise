#  (Eggs per Box) Typically 6 eggs fit in one box. Write a script to calculate the number of boxes a farmer
# needs to store 28 eggs. The script will also determine how many eggs are placed in the last uncompleted box,
# and how many additional eggs are needed to fill this last box.
if __name__ == '__main__':
    eggs = int(input("Enter amount of Eggs: "))
    box = eggs // 6
    add_eggs = eggs % 6

    if 0 < add_eggs <= 5:
        box = box + 1

        un_box = add_eggs

    fill = 6 - add_eggs
    if fill < eggs:
        print(f"The number of boxes needed is {box}, \n"
              f"{un_box} eggs are in the uncompleted box \n"
              f"and {fill} eggs are needed to fill the last box")

    else:
        print(f"The number of boxes needed are {box}")