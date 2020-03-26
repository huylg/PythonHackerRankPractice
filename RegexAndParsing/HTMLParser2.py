from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)
    def handle_comment(self, data):
        l = data.split("\n")
        print('>>> Multi-line Comment') if len(l)>1 else print('>>> Single-line Comment')
        [print(i) for i in l if i]

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

