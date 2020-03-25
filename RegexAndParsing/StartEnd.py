import re
s = input()
r = input()
rs = list(re.finditer(r'(?<={}){}'.format(r[0],r[1:]),s))
[print('({}, {})'.format(i.start()-1,i.end()-1)) for i in rs] if rs else print('(-1, -1)')
