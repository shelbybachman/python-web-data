#!/usr/bin/env python3

import re
import numpy as np

data = open('data/regex_sum_1474128.txt')

list_numbers = []
for line in data:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)

    if len(numbers) == 0:
        continue
    else:
        for i in range(len(numbers)):
            number = float(numbers[i])
            list_numbers.append(number)

print(np.sum(list_numbers))
