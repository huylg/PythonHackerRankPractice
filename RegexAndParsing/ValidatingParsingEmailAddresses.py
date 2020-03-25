import email.utils
import re
r = r'^[A-Za-z][\w\-\.]+@[A-Za-z]*\.[A-Za-z]{1,3}$'
for _ in range(int(input())):
    s = input()
    name, mail = email.utils.parseaddr(s)
    if re.match(r,mail):
        print(s)

