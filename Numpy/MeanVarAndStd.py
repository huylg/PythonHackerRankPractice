import numpy as np
n,m = map(int,input().split())
l = list()
[l.append(list( map(int,input().split()))) for _ in range(n)]
arr = np.array(l)
np.set_printoptions(legacy='1.13')
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr),12),end='')

