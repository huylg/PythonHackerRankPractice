import re
r = r'^(?!.*(\d)(-?\1){3})[456]\d{3}((?:-\d{4}){3}|(?:\d{4}){3})$'

[print('Valid') if (bool(re.match(r,input()))) else print('Invalid') for _ in range(int(input()))]

