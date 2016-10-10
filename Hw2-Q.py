# Bridget Mohn and Eric Wilson
# CS 466R
# Homework 2
#

import sys


def main():
    # Input filename and Output filename
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    #make sure we've got the right things
    print("Input:" + input_file + "\nOutput:" + output_file)

    # Opens the input and output files
    fin = open(str(input_file), "r")
    fout = open(str(output_file), "w")

    # Declaration for Array, array length, and the comparison sequences
    temp = []
    motifSequence = ""
    bestScore = 0
    score = 0
    medianString = ""
    bestSubStringA = ""
    bestSubStringB = ""

    for line in fin.readlines():
        # Add each line in the file (each sequence) into the array
        temp.append(line)

    # Remove the header from the sequences
    for line in fin.readlines():
        # Add each line in the file (each sequence) into the array
        temp.append(line)

    # Delete the first line and strip newline characters off remaining strings
    del temp[0]

    for line in temp:
        line = line.strip();

    for i in range(0, temp.length() - 1):
        stringA = temp[i]
        for j in range(1, temp.length() - 1):
            stringB = temp[j]
            for k in range(0, 9):
                subStringA = stringA.subString(k, k + 8)
                for l in range(0, 9):
                    subStringB = stringB.subString(l, l + 8)
                    score = compareFunction(subStringA, subStringB)
                    if (score > bestScore):
                        bestScore = score
                        bestSubStringA = subStringA
                        bestSubStringB = subStringB

    # Then find the median string given the two subStrings of the best scoring 8mers
    findMedianString(bestSubStringA, bestSubStringB)

    # Close the input and output files
    fin.close()
    fout.close()


# Function that compares two 8mers
def compareFunction(a, b):
    i = 0
    score = 0
    while (i < a.length()):
        if (a[i] == b[i]):
            score = score + 1
        else:
            i += 1
            continue
    return score


def findMedianString(a, b):
    medianString = ""
    i = 0
    while (i < a.length()):
        if (a[i] == b[i]):
            medianString.append(i)
        else:
            medianString.append('-')

    return medianString
