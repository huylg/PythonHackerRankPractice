superSet = set(map(int,input().split()))
result = True
n = int(input())
for i in range(n): 
    subSet = set(map(int,input().split()))
    result &= (len(subSet -  superSet)==0) and (len(superSet - subSet)>0)
print(result)

