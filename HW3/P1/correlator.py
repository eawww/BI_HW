#gonna read in stuff and find correlation, yo.
#specifically, finds correlation coefficient between output from Hw3_Q1.py
#and BLOSUM62 matrix and outputs it to CLI
#Eric Wilson 2016-10-25 eawww0@gmail.com

import sys
import math

poss_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
             'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    Input1 = sys.argv[1]
    Input2 = "BlosumMatrix.txt"

    fin1 = open(str(Input1), "r")
    fin2 = open(str(Input2), "r")

    blosum_matrix = readBlosumMatrix(fin2)

    user_matrix = readUserMatrix(fin1)

    #for this specific case
    del user_matrix['U']

    blosum_mean = matrixMean(blosum_matrix)
    user_mean = matrixMean(user_matrix)

    topsum = sumofproducts(blosum_matrix, blosum_mean, user_matrix, user_mean)
    blosum_bottom = rootofsumofsquaresofdifferences(blosum_matrix, blosum_mean)
    user_bottom = rootofsumofsquaresofdifferences(user_matrix, user_mean)

    result = topsum/(blosum_bottom * user_bottom)

    value = str.format("{0:.3f}", result)

    print("Correlation: " + value)


#accepts file in stream as parameter
def readBlosumMatrix(fin):
    lines = fin.readlines()
    indexOrder = lines[0]
    blosum_matrix = {}
    del lines[0]

    indexOrder = indexOrder.strip()
    indexOrder = indexOrder.replace("  ", " ")
    indexOrder = indexOrder.split(' ')

    #construct dict of dicts for this thang.

    for char in indexOrder:
        blosum_matrix[char] = {}
        for char2 in indexOrder:
            blosum_matrix[char][char2] = 0

    for i in range(0, len(lines)-1):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].replace("  ", " ")
        lines[i] = lines[i].split(' ')
        #assumes lines[i] and indexOrder are the same length
        for j in range(0, len(indexOrder)-1):
            blosum_matrix[indexOrder[i]][indexOrder[j]] = int(lines[i][j])

    return blosum_matrix
    #remove


def readUserMatrix(fin):
    lines = fin.readlines()
    indexOrder = lines[0]
    user_matrix = {}
    del lines[0]

    indexOrder = indexOrder.strip()
    indexOrder = indexOrder.replace("       ", " ")
    indexOrder = indexOrder.split(' ')

    #construct the dicts
    for char in indexOrder:
        user_matrix[char] = {}
        for char2 in indexOrder:
            user_matrix[char][char2] = 0

    for i in range(0, len(indexOrder)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].replace("   ", " ")
        lines[i] = lines[i].replace("  ", " ")
        lines[i] = lines[i].split(' ')
        del lines[i][0] #remove index character
        #assumes lines[i] is same length as indexOrder
        for j in range(0, len(indexOrder)-1):
            user_matrix[indexOrder[i]][indexOrder[j]] = float(lines[i][j])
    return user_matrix

def matrixMean(matrix):
    total = 0.0
    count = 0
    for key, val in matrix.items():
        for key2, val2 in matrix[key].items():
            total += val2
            count += 1
    return total / count


def sumofproducts(matrix1, mean1, matrix2, mean2):
    summysum = 0.0
    for key1, val2 in matrix1.items():
        for key2, val2 in matrix1[key1].items():
            summysum += (matrix1[key1][key2] - mean1) * (matrix2[key1][key2] - mean2)
    return summysum

def rootofsumofsquaresofdifferences(matrix, mean):
    total = 0.0

    for key1, val1 in matrix.items():
        for key2, val2 in matrix[key1].items():
            total += (matrix[key1][key2] - mean)**2
    return math.sqrt(total)

main()


