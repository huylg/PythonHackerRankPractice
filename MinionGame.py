def minion_game(string):
    vowels = set("AEIOU")

    kevinScore  = 0
    kevinTemp = 0
    stuartScore = 0
    stuartTemp = 0
    for ch in string:
        if ch in vowels:
            #process
            kevinTemp += 1
        else:
            stuartTemp += 1
        kevinScore += kevinTemp
        stuartScore += stuartTemp
    if kevinScore>stuartScore: 
        print("Kevin",kevinScore)
    elif kevinScore<stuartScore:
       print("Stuart",stuartScore)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
