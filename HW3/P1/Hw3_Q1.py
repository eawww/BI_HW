#Bridget Mohn and Eric Wilson
#CS 466R
#Homework 3 - Question 1
#Takes a file containing multiple sequences and makes a amino acid substitution
#matrix and then compare our matrix to a known matrix.

import sys
import math
from collections import OrderedDict

#Input filename and output filename is taken from the command line
InputFile = sys.argv[1]
OutputFile = sys.argv[2]

#Opens the input and output file
fin = open(str(InputFile), "r")
fout = open(str(OutputFile), "w")
logfile = open("log.txt", "w")

#List of possible characters
poss_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
             'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Dictionaries for substitution matrix, counts, and sequences
AASM = OrderedDict()
counts = OrderedDict()
sequences = []

totalAA = 0

totalPairs = 0


def main():
    populateDictionaries()
    parseInput()
    countAAinstances()
    countPairInstances()
    calculateAAprobabilities()
    calculatePairProbabilities()
    calculateMatrixValues()
    outputMatrix()

    fout.close()
    fin.close()
    logfile.close()

# read in and parse sequences into usable data
# assumes all sequences are delimited by '>' line at top and empty line at bottom
def parseInput():
    tempstrings = []
    templine = ""
    for line in fin.readlines():
        if line[0] == '>':
            logfile.write("Reading aligned sequence " + line + "\n")
        elif (line == "\n"):
            # denotes end of sequence
            # mash them all into one string and add it to sequences
            assembledsequence = ""
            for substring in tempstrings:
                assembledsequence += substring
            sequences.append(assembledsequence)
            # set tempstrings back to []
            tempstrings = []
        else:
            templine = line.strip()
            templine = templine.replace(" ", "")
            tempstrings.append(templine)


def populateDictionaries():
    # Populate the dictionaries
    logfile.write("Populating Dictionaries\n")
    for character in poss_char:
        counts[character] = 0
        AASM[character] = OrderedDict()  # Nested dictionaries make up the matrix
        for character2 in poss_char:
            AASM[character][character2] = 0

#counts number of occurrences of each character in all sequences
def countAAinstances():
    logfile.write("\nCounting amino acid occurrences:\n")
    global totalAA
    for sequence in sequences:
        for character in sequence:
            if character != '-':
                totalAA += 1
                counts[character] += 1
    #logging
    for key, value in counts.items():
        logfile.write("(" + str(key) + "," + str(value) + ")")
    logfile.write("\nTotal Amino Acids: " + str(totalAA) + "\n\n")


def countPairInstances():
    global totalPairs
    logfile.write("Counting pair occurrences:\n")
    for i in range(0, len(sequences) - 1):
        for j in range (i + 1, len(sequences) - 1):
            if i != j:
                for k in range (0, len(sequences[i])-1):
                    if (sequences[i][k] != '-') and (sequences[j][k] != '-'):
                        #increment both corresponding entries in matrix
                        AASM[sequences[i][k]][sequences[j][k]] += 1
                        if sequences[i][k] != sequences[j][k]:
                            AASM[sequences[j][k]][sequences[i][k]] += 1
                        totalPairs += 1
    #logging
    logintMatrix()
    logfile.write("Total pairs:" + str(totalPairs) + "\n")


def calculateAAprobabilities():
    logfile.write("\nCalculating amino Acid Probabilities:\n")
    for key, value in counts.items():
        counts[key] = value/totalAA
    #logging
    for key, value in counts.items():
        formattedValue = str.format("{0:.3f}", value)
        logfile.write("(" + str(key) + "," + formattedValue + ")")
    logfile.write("\n\n")



def calculatePairProbabilities():
    logfile.write("\nCalculating pair probabilities:\n")
    for key1, val1 in AASM.items():
        for key2, val2 in val1.items():
            AASM[key1][key2] = val2/totalPairs
    #logging
    logfloatMatrix()
    logfile.write("\n\n")


def calculateMatrixValues():
    logfile.write("\nCalculating matrix values: ( lg(p(A,B)/(p(A)p(B))) )\n")
    for key1, val1 in AASM.items():
        for key2, val2 in val1.items():
            if (counts[key1] > 0.0) and (counts[key2] > 0.0) and (val2 > 0.0):
                probA = counts[key1]
                probB = counts[key2]
                pABoverpApB = val2/(probA * probB)
                AASM[key1][key2] = math.log(pABoverpApB, 2)
    #logging
    logfloatMatrix()
    logfile.write("\n\n")


def outputMatrix():
    fout.write("   ")
    for character in poss_char:
        fout.write("   " + character + "    ")
    fout.write("\n")
    for key1, val1 in AASM.items():
        fout.write(str(key1) + "  ")
        for key2, val2 in val1.items():
            value = str.format("{0:.3f}", AASM[key1][key2])
            if (value[0] == '-'):
                fout.write(value)
                fout.write("  ")
            else:
                fout.write(" ")
                fout.write(value)
                fout.write("  ")
        fout.write("\n")
    logfile.write("Result substitution matrix output to file \"" + OutputFile + "\"\nHave a nice day!")


def logintMatrix():
    logfile.write("   ")
    for character in poss_char:
        logfile.write("   " + character + "    ")
    logfile.write("\n")
    for key1, val1 in AASM.items():
        logfile.write(str(key1) + "  ")
        for key2, val2 in val1.items():
            value = '{0: <5}'.format(str(val2))
            if (value[0] == '-'):
                logfile.write(value)
                fout.write("  ")
            else:
                logfile.write(" ")
                logfile.write(value)
                logfile.write("  ")
        logfile.write("\n")


def logfloatMatrix():
    logfile.write("   ")
    for character in poss_char:
        logfile.write("   " + character + "    ")
    logfile.write("\n")
    for key1, val1 in AASM.items():
        logfile.write(str(key1) + "  ")
        for key2, val2 in val1.items():
            value = str.format("{0:.3f}", AASM[key1][key2])
            if (value[0] == '-'):
                logfile.write(value)
                logfile.write("  ")
            else:
                logfile.write(" ")
                logfile.write(value)
                logfile.write("  ")
        logfile.write("\n")
#call main function to start program
main()
