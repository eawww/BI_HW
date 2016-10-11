import sys

def main():
    #get input
    input_file = sys.argv[1]
    fin = open(str(input_file), "r")
    strings = []
    for line in fin.readlines():
        strings.append(line)

    #compile list of 2mers for each sequence
    sequence_kmers = []
    for i in range(0,len(strings)-1):
        sequence_kmers.append([])
        for j in range(0,len(strings[i])-2):
            sequence_kmers[i].append(strings[i][j:j+2])

    #map kmers into number of occurrences of each possible kmer
    #build 2 dictionaries of every possible combination of characters
    #iterate over each set of kmers, incrementing corresponding value in corresponding dictionary for each kmer
    #eliminate unneeded dictionary pairs that are not in either dictionary
        #both dictionaries should be the same length at this point
    #for each key in either dictionary, change value to float(value/number of kmers in that sequence)
    #find sum for each key (valueA - B)^2  or ABS(valueA - valueB) -- this will be our score
    #output score

    fin.close()
