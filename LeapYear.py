def is_leap(year):
    return bool((not year%400) or (year%100 and not year%4))

year = int(input())
print(is_leap(year))