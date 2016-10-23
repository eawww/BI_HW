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
fout = open(str(OutputFile), "w")

#List of possible characters
poss_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
             'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Dictionaries for substitution matrix and counts
AASM = {}
counts = {}
sequences = []

#Populate the dictionaries

for character in poss_char:
    counts[character] = 0
    AASM[character] = {}    #Nested dictionaries make up the matrix
    for character2 in poss_char:
        AASM[character][character2] = 0

#read in and parse sequences into usable data
#assumes all sequences are delimited by '>' line at top and empty line at bottom
tempstrings = []
for line in fin.readlines():
    if line[0] == '>':
        print("ignoring heading line")
    elif (line == "\n"):
        #denotes end of sequence
    else:
        tempstrings.append(line)