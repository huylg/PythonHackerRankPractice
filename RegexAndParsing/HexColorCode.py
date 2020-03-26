import re
r = r'#([A-Fa-f0-9]{3})([A-Fa-f0-9]{3})?(?! {)(?!$)'
for _ in range(int(input())):
    sea = (re.finditer(r,input()))
    [print(i.group()) for i in list(sea)]
