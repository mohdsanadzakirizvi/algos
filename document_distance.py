from math import sqrt, acos
from string import maketrans


def openFile(docname):
    lines = []
    with open(docname, 'r') as doc:
        lines = doc.readlines()
    return lines


def wordSplit(lines):
    lines2 = []
    tranTable = maketrans('?.!;:,-(){}[]_\n\t', ' '*16)
    for line in lines:
        line = line.lower()
        line = line.translate(tranTable)
        lines2.append(line.split())
    return lines2


def linesToDict(splittedLines):
    dictTable = {}
    listLength = 0
    for groups in splittedLines:
        listLength = len(groups)
        if listLength > 1:
            for word in groups:
                if word not in dictTable:
                    dictTable[word] = 0
                if word in dictTable:
                    dictTable[word] += 1
        elif listLength <= 1:
            groups = str(groups).strip('[]')
            if groups not in dictTable:
                dictTable[groups] = 0
            if groups in dictTable:
                dictTable[groups] += 1
    return dictTable


def innerProduct(dictA, dictB):
    num = 0
    for word in dictA:
        if word in dictB:
            num += dictA[word]*dictB[word]
    return num


def main():
    num = denom = 0
    l1 = l2 = []
    dictA = dictB = {}
    documentDistance = 0.0
    f1 = raw_input("Enter file 1 name ")
    f2 = raw_input("Enter file 2 name ")
    l1 = openFile(f1)
    l2 = openFile(f2)
    l1 = wordSplit(l1)
    l2 = wordSplit(l2)
    dictA = linesToDict(l1)
    dictB = linesToDict(l2)
    num = innerProduct(dictA, dictB)
    denom = sqrt(innerProduct(dictA, dictA)*innerProduct(dictB, dictB))
    documentDistance = acos(num/denom)
    print "The document distance is %lf" % (documentDistance)

if __name__ == '__main__':
    main()
