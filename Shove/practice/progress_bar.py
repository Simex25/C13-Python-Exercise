from gettext import install

import pip
import time
import tqdm

count = 0

for i in tqdm.tdqm(range(100)):
    count += i
    time.sleep(0.4)  # only for test
print(f'{count = }')
