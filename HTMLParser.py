from html.parser import  HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name,value in attrs:
            print("->",name,">",value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        for name,value in attrs:
            print("->",name,">",value)


parser = MyHTMLParser()
n = int(input())

for i in range(0,n):
    s = str(input())
    parser.feed(s)


