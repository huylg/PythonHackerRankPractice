import numpy as np
arr = np.array(list(map(float,input().split())))
np.set_printoptions(sign=' ')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
