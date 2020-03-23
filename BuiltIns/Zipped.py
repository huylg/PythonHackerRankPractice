n,m = map(int,input().split(" "))
X = [map(float,input().split()) for _ in range(m)]
z = zip(*X)
for i in list(z):
    print(sum(i)/m)
