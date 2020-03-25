import re
for i in range(int(input())):
    s = input()
    print('Valid') if (re.search(r'[A-Za-z0-9]{10}',s) and re.search(r'[0-9].*[0-9].*[0-9]',s) and re.search(r'[A-Z].*[A-Z]',s) and not re.search(r'(.).*\1',s)) else print('Invalid')
