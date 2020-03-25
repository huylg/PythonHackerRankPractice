from collections import Counter
n = int(input())
l = [input() for _ in range(n)]
c = (Counter(l))
print(len(c))
for i in c:
    print (c[i],end=" ")
