def merge_the_tools(string, k):
    amountOfSubStrings = len(string)//k
    for i in range(amountOfSubStrings):
        l = list(string[i*k:(i+1)*k])
        s = set()
        temp = list("")
        for j in l:
            if not j in s:
                temp.append(j)
                s.add(j)
        print("".join(temp))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
