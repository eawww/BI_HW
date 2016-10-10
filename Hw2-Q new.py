#Bridget Mohn and Eric Wilson
#CS 466R
#Homework 2
#

import sys

#Input filename and Output filename 
input_file = sys.argv[1]
output_file = sys.argv[2]

#make sure we've got the right things
print("Input:" + input_file + "\nOutput:" + output_file)

#Opens the input and output files
fin = open(str(input_file), "r")
fout = open(str(output_file), "w")

#Declaration for Array, array length, and the comparison sequences
temp = []
motifSequence = ""
bestScore = 0
score = 0 
medianString = ""
bestSubStringA = ""
bestSubStringB = ""

#Function that compares two 8mers
def compareFunction(a, b):
    i = 0
    score = 0
    while (i < a.length()):
        if(a[i] == b[i]):
            score = score + 1
        else:
            i += 1
            continue
    return score

def findMedianString(a, b):
    medianString = ""
    i = 0
    while (i < a.length()):
        if(a[i] == b[i]):
            medianString.append(i)
        else:
            medianString.append('-')

    return medianString
        

#Remove the header from the sequences
for line in fin.readlines():
    #Add each line in the file (each sequence) into the array
    temp.append(line)

#Delete the first line and strip newline characters off remaining strings
del temp[0]

for line in temp:
    line = line.strip();

#Loop through the first two seqeuences and find the best scoring 8mers
def main():
    stringA = temp[i]
    stringB = temp[j]
    for i in range(0, 9):
        subStringA = stringA.subString(i, i+8)
        for j in range(0, 9):
            subStringB = stringB.subString(j, j+8)
            score = compareFunction(subStringA, subStringB)
            if (score > bestScore):
                bestScore = score
                bestSubStringA = subStringA
                bestSubStringB = subStringB

    #Then find the median string given the two subStrings of the best scoring 8mers
    findMedianString(bestSubStringA, bestSubStringB)

    #For each sequence and each sequences set of 8mers see how similar they are to the medianString
    for k in range(2, temp.length() - 1):
        stringA = temp[k]
        for m in range(0, 9):
            subStringA = stringA.subString(n, n+8)
            score = compareFunction(medianString, subStringA)
            if (score > bestScore):
                bestScore = score
                motifSequence = subStringA #????

    # For each of the remaining sequences in the array
    for k in range(2, temp.length() - 1):
        stringA = temp[k]
        # Make all their possible 8mers
        for m in range(0, 9):
            subStringA = stringA.subString(n, n + 8)
            # Score the comparision of current 8mer to the median string
            score = compareFuntion(medianString, subStringA)
            #
            if (score > bestScore):
                bestScore = score
                # The motif sequences becomes the highest scoring 8mer
                motifSequence = subStringA  ???????`

        
        

#Close the input and output files
fin.close()
fout.close()
