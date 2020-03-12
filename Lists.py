if __name__ == '__main__':
    N = int(input())
    myList = []

    for _ in range(N):
        command, *strs = input().split()
        param = list(map(int, strs))
        if(command == "insert"):
            myList.insert(param[0], param[1])
        else:
            if(command == "print"):
                print(myList)
            else:
                if(command == "remove"):
                    myList.remove(param[0])
                else:
                    if(command == "append"):
                        myList.append(param[0])
                    else:
                        if(command == "sort"):
                            myList.sort()
                        else:
                            if(command == "pop"):
                                myList.pop()
                            else:
                                if(command == "reverse"):
                                    myList.reverse()

