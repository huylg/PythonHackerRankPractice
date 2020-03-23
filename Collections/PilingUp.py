from collections import deque

q = int(input())
for _ in range(q):
    n = int(input())
    d = deque(map(int,input().split()))
    temp = 2**31+1
    while len(d) > 0:
        if d[0] > d[-1] and d[0]<=temp :
            temp = d.popleft()
        elif d[-1] >= d[0] and d[-1]<=temp:
            temp = d.pop()
        else:
            break;
    print({True:'Yes',False:'No'}[len(d)==0])

