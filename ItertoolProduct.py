from itertools import product
l1 = map(int, input().split())
l2 = map(int, input().split())
for t in  list(product(l1,l2)):
    print(t,end = ' ')

