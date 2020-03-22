from itertools import permutations
inp = input().split()
str, k = inp[0], int(inp[1])
for i in permutations(str,k):
    print("".join(i))
