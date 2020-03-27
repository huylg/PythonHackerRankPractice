import numpy as np
n = int(input())
l1 = list()
l2 = list()
[l1.append(list(map(int,input().split()))) for _ in range(n)]
[l2.append(list(map(int,input().split()))) for _ in range(n)]
arr1 = np.array(l1)
arr2 = np.array(l2)
np.set_printoptions(legacy='1.13')
print(np.dot(arr1,arr2))
