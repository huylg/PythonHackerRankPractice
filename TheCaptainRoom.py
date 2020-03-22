from collections import Counter
n = int(input())
c = Counter(map(int,input().split()))
for i in c.keys():
    if c[i] < n:
        print(i)
        break
