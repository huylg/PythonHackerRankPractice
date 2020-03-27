#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
rawResult = "".join(["".join(i) for i in (list(zip(*matrix)))])
r = r'(?<=\w)[^\w]+(?=\w)'
result = re.sub(r,' ',rawResult)
print(result)
