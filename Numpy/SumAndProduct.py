import numpy as np
n,m = map(int,input().split())
l = list()
[l.append(list(map(int,input().split()))) for _ in range(n)]
arr = np.array(l)
print(np.prod(np.sum(arr,axis=0)))
