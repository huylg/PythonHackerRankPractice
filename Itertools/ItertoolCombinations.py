from itertools import combinations
param = input().split()
s = param[0]
k = int(param[1])
for i in range(1,k+1):
    l = list()
    for j in list(combinations(s,i)):
        l.append("".join(sorted(j)))
    for j in  sorted(l):
        print(j)
