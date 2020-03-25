import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s =sorted(input())
    c = Counter(s)
    for i in c.most_common(3):
        print(i[0],i[1])

    
