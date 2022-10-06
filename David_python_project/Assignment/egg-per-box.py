import math

egg_per_box = 6
no_of_eggs = 28

no_of_boxes = math.ceil(no_of_eggs / egg_per_box)
print(f"Number of needed boxes is: {no_of_boxes}")

no_of_remaining_eggs = no_of_eggs % egg_per_box
print(f"Number of remaining eggs placed in the box is: {no_of_remaining_eggs}")

no_eggs_needed_to_fill_the_last_box = egg_per_box - no_of_remaining_eggs
print(f"The number of eggs needed to fill the last box is: {no_eggs_needed_to_fill_the_last_box}")