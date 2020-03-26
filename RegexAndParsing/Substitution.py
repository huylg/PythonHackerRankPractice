import re
for _ in range(int(input())):
    s = input()
    s = re.sub((r'(?<= )\|\| '),"or ",s)
    s = re.sub((r'(?<= )&& '),"and ",s)
    print(s)
