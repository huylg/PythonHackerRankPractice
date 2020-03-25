import itertools as it
n,m = map(int,input().split(" "))
l = list()
for i in range(n):
    l.append((set(map(int,input().split()[1:]))))
p = list(it.product(*l))
M = 0
Mtemp = 0
for i in p:
    temp = 0
    for j in i:
        temp += j**2
    temp = temp % m
    if temp > M:
        M = temp
        litemp = i
print(M)
print(litemp)
