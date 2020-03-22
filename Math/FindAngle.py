import math
AB = float(input())
BC = float(input())
AC = math.sqrt(AB**2 + BC**2)
print(int(round(math.degrees(math.asin(AB/AC)))),end="")
print("°")
