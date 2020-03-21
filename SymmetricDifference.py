m = int(input())
lm = set(map(int,input().split()))
n = int(input())
ln = set(map(int,input().split()))
for i in ( sorted(lm.union(ln)-(lm.intersection(ln)))):
    print(i)
