import numpy as np
l = list()
for _ in range(int(input())):
    l.append(list(map(float,input().split())))
print(np.linalg.det(l))
