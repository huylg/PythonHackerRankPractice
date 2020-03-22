qu = int(input())
result = list()
for i in range(qu):
    lenA = int(input())
    setA = set(map(int,input().split()))
    lenB = int(input())
    setB = set(map(int,input().split()))
    result.append(len(setA-setB)==0)
[print(i) for i in result]
