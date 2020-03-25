import calendar
m,d,y = map(int,input().split())
wd = calendar.weekday(y,m,d)
print(['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'][wd])

