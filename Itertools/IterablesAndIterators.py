from itertools import combinations
n = int(input())
l = sorted(list(input().split(" ")))
k = int(input())
c = list(combinations(l,k))
result = 0
for i in c:
    if i[0] == 'a': result += 1/len(c)
print(result)

