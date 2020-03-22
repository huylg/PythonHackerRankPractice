from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())

for i in range(n):
    temp = input()
    d[temp].append(i+1)
q = list()
for i in range(m):
    q.append(input())
for i in range(m):
    temp = q[i]
    if temp in d.keys():
        [print(j,end = " ") for j in d[temp]]

        print("")
    else:
        print(-1)


