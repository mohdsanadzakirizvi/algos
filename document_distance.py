from math import sqrt, acos


def openFile(docname):
    lines = []
    with open(docname, 'r') as doc:
        lines = doc.readlines()
    return lines


def wordSplit(lines):
    lines2 = []
    for line in lines:
        lines2.append(line.split())
    return lines2


def linesToDict(splittedLines):
    dictTable = {}
    for group in splittedLines:
        for word in group:
            if word not in dictTable:
                dictTable[word] = 1
            if word in dictTable:
                dictTable[word] += 1
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
    wordSplit(l1)
    wordSplit(l2)
    dictA = linesToDict(l1)
    dictB = linesToDict(l2)
    num = innerProduct(dictA, dictB)
    denom = sqrt(innerProduct(dictA, dictA)*innerProduct(dictB, dictB))
    documentDistance = acos(num/denom)
    print "The document distance is %lf" % (documentDistance)

if __name__ == '__main__':
    main()
