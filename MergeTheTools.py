def merge_the_tools(string, k):
    length = len(string)
    subStringLength = length//k
    for i in  range(subStringLength):
        temp = list( string[i*subStringLength:(i+1)*subStringLength])
        del  temp[i]
        print("".join(temp))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
