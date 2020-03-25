import re
restr = '^[-+]?[0-9]*\.[0-9]+$'
n = int(input())
for _ in range(n):
    print(not  re.fullmatch(restr,input())==None)
