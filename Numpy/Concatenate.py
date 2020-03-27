import numpy as np
N, M, P = map(int,input().split())
nl = []
ml = []
[nl.append(list(map(int,input().split()))) for _ in range(N)]
[ml.append(list(map(int,input().split()))) for _ in range(M)]
nArr = np.array(nl)
mArr = np.array(ml)
print(np.concatenate((nArr,mArr),axis=0))

