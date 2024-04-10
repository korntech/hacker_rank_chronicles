import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    if level == -1:
        level =0
    global maxdepth
    # your code goes here
    if level > maxdepth:
        maxdepth = level
    if not elem.findall("*"):
        return 1
    else:
        return 1 + max(depth(item, level+1) for item in elem.findall("*"))


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)