import re
m = re.search(r'([A-Za-z0-9])\1',input())
print( m.groups()[0] if m else -1  )

