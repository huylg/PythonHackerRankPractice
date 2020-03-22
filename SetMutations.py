import functools as ft
n = int(input())
s = set(map(int,input().split()))
qu = int(input())
for i in range(qu):
    param = input().split(" ")
    cmd  = param[0]
    l = int(param[1])
    subset = set(map(int,input().split()))
    if cmd == "update":
        s |= subset
    elif cmd == "intersection_update":
        s &= subset
    elif cmd == "symmetric_difference_update":
        s ^= subset
    else:
        s -= subset
if len(s)>0:
    print(ft.reduce(lambda a,b: a+b,s))
else:
    print(0)
