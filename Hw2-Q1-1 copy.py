# Bridget Mohn and Eric Wilson
# CS 466R
# Homework 2
# For a set of sequences for a motif, we will use the consensus
# approach to recover the motif.
# Input file source(SequenceInput.txt): http://jaspar.genereg.net/

import sys
from random import randint

def main():
    # Input filename and Output filename
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    num_iterations = sys.argv[3]

    # make sure we've got the right things
    print("Input: " + input_file + " Output: " + output_file + " \niter: " + str(num_iterations))
    print()
    # Opens the input and output files
    fin = open(str(input_file), "r")
    outfile = open(str(output_file), "w")

    # Declaration for Array, array length, and the comparison sequences
    temp = []
    motifSequence = ""
    bestMotifScore = 0
    bestMotif =""
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

    #Remove the newline char and make all sequences lowercase
    for p in range(0, len(temp)):
        temp[p] = temp[p].strip()
        temp[p] = temp[p].lower()
    # done processing input

    #OUTER LOOP WILL START HERE
    for iteration in range(0, int(num_iterations)):
        seed_string = ""
        currentMotifMaxScore = 0
        seedscore = 0
        indexA = randint(0, len(temp) - 1)
        indexB = randint(0, len(temp) - 1)
        # make sure indexes are different
        while (indexA == indexB):
            indexB = randint(0, len(temp) - 1)


        for i in range(0, 9):
            substringA = temp[indexA][i:i + 8]
            for j in range(0, 9):
                substringB = temp[indexB][j:j + 8]
                score = compareFunction(substringA, substringB)
                if (score > seedscore):
                    seedscore = score
                    seedA = substringA
                    seedB = substringB
        seed_string = findMedianString(seedA, seedB)


        # NOW we need to iterate over all the other strings and see what their best match is

        currentMotifMaxScore = 0

        for k in range(0, len(temp)):  # select row
            thisstrmaxscore = 0
            for m in range(0, 9):
                score = compareFunction(seed_string, temp[k][m:m + 8])
                if (score > thisstrmaxscore):
                    thisstrmaxscore = score
            currentMotifMaxScore += thisstrmaxscore
        if (currentMotifMaxScore > bestMotifScore):
            bestMotifScore = currentMotifMaxScore
            bestMotif = seed_string
        outfile.write("(" + str(indexA) + "," + str(indexB) + "):" + seed_string + ":--" + str(currentMotifMaxScore))

    outfile.write("BEST MOTIF: " + bestMotif)

    # Close the input and output files
    fin.close()
    outfile.close()


# Function that compares two 8mers
def compareFunction(a, b):
    i = 0
    score = 0
    while (i < len(a)):
        if (a[i] == b[i]):
            score = score + 1
            i += 1
        else:
            i += 1
            continue
    return score


def findMedianString(a, b):
    medianString = ""
    i = 0
    while (i < len(a)):
        if (a[i] == b[i]):
            medianString += str(a[i])
        else:
            medianString += "-"
        i += 1

    return medianString

main()
