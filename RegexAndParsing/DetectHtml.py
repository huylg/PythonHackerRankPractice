from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->",i[0],">",i[1])
parser = MyParser()
for _ in range(int(input())):
    s = input()
    parser.feed(s)

