def solve(s):
    l = list(s)
    i = 0
    while i < len(s):
        if(s[i] == " " and i+1<len(s)):
            l[i+1] = l[i+1].upper()
        i+=1
    return "".join(l)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

