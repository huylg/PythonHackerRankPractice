import textwrap

def wrap(string, max_width):
    result = ""
    for str in textwrap.wrap(string,max_width):
        result += str + "\n"
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)