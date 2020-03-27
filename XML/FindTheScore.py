import xml.etree.ElementTree as etree
xml =  "\n".join( [ input() for _ in range(int(input()))])
tree = etree.ElementTree(etree.fromstring(xml))
print(tree.getroot().attrib)
print(list(tree.getroot()))
