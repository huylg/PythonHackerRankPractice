from collections import OrderedDict
n = int(input())
orderedList = OrderedDict()
for _ in range(n):
    params = input().rsplit(" ",1)
    if not  params[0] in orderedList:
        orderedList[params[0]] = 0
    orderedList[params[0]]+=int(params[1])
for i in orderedList:
    print (i, orderedList[i])
