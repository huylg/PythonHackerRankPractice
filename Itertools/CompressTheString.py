import itertools as it
l = list(map(int, input()))
for i,k in it.groupby(l):
    print("(%d, %d)"%(len(list(k)),i),end = " ")
