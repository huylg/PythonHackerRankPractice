n,m = map(int,input().split())
arr = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
result = 0
for i in a:
    if i in arr:
        result += 1
for i in b:
    if i in arr:
        result -= 1


print(result)
