from collections import deque
n = int(input())
result = deque()
for _ in range(n):
    params  = input().split()
    cmd = params[0]
    if cmd == "append":
        val = int(params[1])
        result.append(val)
    elif cmd == "appendleft":
        val = int(params[1])
        result.appendleft(val)
    elif cmd == "pop":
        result.pop()
    else:
        result.popleft()
[print(i, end =" ") for i in result]

