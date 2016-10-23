#Bridget Mohn and Eric Wilson
#CS 466R
#Homework 3 - Question 1
#Takes a file containing multiple sequences and makes a amino acid substitution
#matrix and then compare our matrix to a known matrix.

import sys
import math
from collections import OrderedDict

#Input filename and output filename is taken from the command line
InputFile = "input2" #sys.argv[1]
OutputFile = "output2" #sys.argv[2]

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

# read in and parse sequences into usable data
# assumes all sequences are delimited by '>' line at top and empty line at bottom
def parseInput():
    tempstrings = []
    templine = ""
    for line in fin.readlines():
        if line[0] == '>':
            print("Reading aligned sequence " + line)
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
    for character in poss_char:
        counts[character] = 0
        AASM[character] = {}  # Nested dictionaries make up the matrix
        for character2 in poss_char:
            AASM[character][character2] = 0

#counts number of occurrences of each character in all sequences
def countAAinstances():
    global totalAA
    for sequence in sequences:
        for character in sequence:
            if character != '-':
                totalAA += 1
                counts[character] += 1


def countPairInstances():
    global totalPairs
    for i in range(0, len(sequences) - 1):
        for j in range (i, len(sequences) - 1):
            if i != j:
                for k in range (0, len(sequences[i])-1):
                    if (sequences[i][k] != '-') and (sequences[j][k] != '-'):
                        #increment both corresponding entries in matrix
                        AASM[sequences[i][k]][sequences[j][k]] += 1
                        AASM[sequences[j][k]][sequences[i][k]] += 1
                        totalPairs += 1


def calculateAAprobabilities():
    for key, value in counts.items():
        counts[key] = value/totalAA



def calculatePairProbabilities():
    for key1, val1 in AASM.items():
        for key2, val2 in val1.items():
            AASM[key1][key2] = val2/totalPairs


def calculateMatrixValues():
    for key1, val1 in AASM.items():
        for key2, val2 in val1.items():
            if (counts[key1] != 0.0) and (counts[key2] != 0.0):
                AASM[key1][key2] = math.log(val2/(counts[key1] * counts[key2]), 2)


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
#call main function to start program
main()
