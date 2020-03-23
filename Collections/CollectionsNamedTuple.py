from collections import namedtuple
n = int(input())
Student=namedtuple('Student',input())
students = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(sum(students)/n)
