n = int(input())
for _ in range(n):
    a,b = input().split(" ")
    try:
        print(int(a)//int(b))
    except ValueError    as  e:
        print('Error Code:', e)
    except   ZeroDivisionError  as  e:
        print('Error Code:', e)


