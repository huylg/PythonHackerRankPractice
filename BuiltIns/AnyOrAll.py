n = int(input())
l = list(map(int,input().split()))
print(all([all([i >=0 for i in l]),any([str(i)==str(i)[::-1] for i in l])]))

