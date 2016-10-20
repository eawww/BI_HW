#Bridget Mohn and Eric Wilson
#CS 466R
#Homework 3 - Question 1
#Takes a file containing multiple sequences and makes a amino acid substitution
#matrix and then compare our matrix to a known matrix. 

import sys

#Input filename and output filename is taken from the command line
InputFile = sys.argv[1]
OutputFile = sys.argv[2]

#Opens the input and output file
fin = open(str(InputFile), "r")
fout = open(str(Output), "w")

#Declaration for Array, amino acid counts, and amino acid pair counts
temp = []
countA = 0
countB = 0
countC = 0
countD = 0
countE = 0
countF = 0
countG = 0
countH = 0
countI = 0
countK = 0
countL = 0
countM = 0
countN = 0
countP = 0
countQ = 0
countR = 0
countS = 0
countT = 0
countV = 0
countW = 0
countX = 0
countY = 0
countZ = 0

#Add each each sequence in the file into the array
for line in fin.readlines():
    temp.append(line)

#Delete the header from the input
del temp[0]

#Remove the newline char and make all sequences lowercase
    for p in range(0, len(temp)):
        temp[p] = temp[p].strip()

for i in range(0, len(temp)):
    for j in range(0,len(temp[i])):
        sequence1 = temp[i]
        for k in range(0, len(temp[j])):
            sequence2 = temp[j]
            if((sequence1[j] and sequence2[j]) = 'A'):
                countA += 2
            else if((sequence1[j] and sequence2[j]) = 'B'):
                countB += 2 


                
