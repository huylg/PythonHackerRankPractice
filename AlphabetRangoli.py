

def print_rangoli(size):

    width = 4*size - 3

    for i in range(2*size-1):
        j = abs(size - i -1)
        k = j
        temp = chr(size-1+ord('a'))
        j+= 1
        h = size - 2
        while h >= k:
            temp += "-{}".format(chr(h+ord('a')))
            h-=1
            
        while j <= size-1:
            temp += "-{}".format(chr(j+ord('a')))
            j+=1
      
        print(temp.center(width,"-"))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
