import numpy as np
n, m = map(int,input().split())
l1 = list()
l2 = list()
for _ in range(n):
    l1.append( list(map(int,input().split())))
for _ in range(n):
    l2.append( list(map(int,input().split())))
a = np.array(l1)
b = np.array(l2)

print((a+b),(a-b),(a*b),(a//b),(a%b),(a**b),sep="\n")
