import functools as ft
n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    query = input().split(" ")
    if query[0] == "pop":
        s.pop()
    elif query[0] == "remove":
        s.remove(int(query[1]))
    else:
        s.discard(int(query[1]))
if len(s)>0: 
    print(ft.reduce(lambda a,b: a+b,s))
else:
    print(0)    
