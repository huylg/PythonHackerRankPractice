from itertools import combinations_with_replacement
params = input().split()
s = sorted(params[0])
k = int(params[1])
for j in list(combinations_with_replacement(s,k)):
        print("".join(j))
