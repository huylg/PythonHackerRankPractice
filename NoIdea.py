from collections import Counter
n,m = map(int,input().split())
arr = Counter(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
result = 0
for i in a:result += arr[i]

for i in b:result -= arr[i]


print(result)
