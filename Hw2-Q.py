# Bridget Mohn and Eric Wilson
# CS 466R
# Homework 2
#

import sys


def main():
    # Input filename and Output filename
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    num_iterations = sys.argv[3]

    #make sure we've got the right things
    print("Input:" + input_file + "\nOutput:" + output_file)

    # Opens the input and output files
    fin = open(str(input_file), "r")
    fout = open(str(output_file), "w")

    # Declaration for Array, array length, and the comparison sequences
    temp = []
    motifSequence = ""
    seedscore = 0
    score = 0
    seed_string = ""
    seedA = ""
    seedB = ""


    # Remove the header from the sequences
    for line in fin.readlines():
        # Add each line in the file (each sequence) into the array
        temp.append(line)

    # Delete the first line and strip newline characters off remaining strings
    del temp[0]

    for line in temp:
        line = line.strip();
    # done processing input

    #OUTER LOOP WILL START HERE
    
    indexA = 0 #will be random
    indexB = 1 #will be random

    for i in range(0, indexA - 8):
        substringA = temp[indexA][i:i+8]
        for j in range(0, indexB - 8):
            substringB = temp[indexB][j:j+8]
            score = compareFunction(substringA,substringB)
            if (score > seedscore):
                seedscore = score
                seedA = substringA
                seedB = substringB
    seed_string = findMedianString(seedA, seedB)

    #NOW we need to iterate over all the other strings and see what their best match is
    #so do that here.
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
