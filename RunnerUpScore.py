if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = -100
    secondMax = -100
    for i in arr:
        if(i>max):
            secondMax = max
            max = i
        else:
            if(i>secondMax and i!=max):
                secondMax = i

    print(secondMax)
