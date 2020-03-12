class student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

if __name__ == '__main__':
    arr = []
    min = 100
    secondMin = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append(student(name,score));

    for i in arr:
        if(i.score<min):
            secondMin = min
            min = i.score
        else:
            if(i.score<secondMin and i.score!=min):
                secondMin=i.score

    result = [x.name for x in arr if x.score == secondMin ]
    result.sort()
    [print(x) for x in result]
