from collections import Counter

num = int(input())
shoes = Counter(map(int,input().split()))

q = int(input())
result = 0
for i in range(q):
    shoe, cost = map(int,input().split())
    if(shoe in shoes.keys()  ):
        if(shoes[shoe] > 0):
            result += cost
            shoes[shoe] -= 1
print(result)

