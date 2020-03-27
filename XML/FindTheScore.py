import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    elements = [node]
    result = 0
    while elements:
        temp = elements.pop(0)
        elements += [i for i in list(temp)]
        result += len(temp.attrib)
    return result

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
