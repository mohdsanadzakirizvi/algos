from math import sqrt, acos
from string import maketrans


def openFile(docname):
    with open(docname, 'r') as doc:
        return doc.readlines()

def wordSplit(lines):
    lines2 = []
    tranTable = maketrans('?.!;:,-(){}[]_\n\t', ' '*16)
    for line in lines:
        line = (line.lower()).translate(tranTable)
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

def docDist(dictA, dictB):
    num = innerProduct(dictA, dictB)
    denom = sqrt(innerProduct(dictA, dictA)*innerProduct(dictB, dictB))
    return acos(num/denom)
   

def main():
    file1 = raw_input("Enter file 1 name ")
    file2 = raw_input("Enter file 2 name ")
    dictA = linesToDict(wordSplit(openFile(file1)))
    dictB = linesToDict(wordSplit(openFile(file2)))
    print "The document distance is:", docDist(dictA, dictB)

if __name__ == '__main__':
    main()
