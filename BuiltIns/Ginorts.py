
def compare(x):
    if(x>='a' and x<='z'):
        return ord(x) - 97
    elif (x>='A' and x<='Z'):
        return 26 + ord(x)-65
    else:
        return 26*2 + int(x) + (1-int(x)%2)*10
    
l = input()
print("".join(sorted(l,key = lambda x: compare(x))))

