#Bioinformatics CS466 HW2
#Bridget Mohn and Eric Wilson
#Instructor: Dinakarpandian
#2016-10-12

#Problem2 (P2)
#Computes similarity of two sequences based on their 2-mer composition

import sys

def main():
    #get input
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    fin = open(str(input_file), "r")
    fout = open(str(output_file), "w")
    strings = []
    for line in fin.readlines():
        strings.append(line)

    #compile list of 2mers for each sequence
    sequence_kmers = []
    for i in range(0,len(strings)):
        sequence_kmers.append([])
        for j in range(0,len(strings[i])-2):
            sequence_kmers[i].append(strings[i][j:j+2])

    #map kmers into number of occurrences of each possible kmer
    #build 2 dictionaries of every possible combination of characters
    poss_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    PMF = {}
    for i in range(0, len(poss_char)-1):
        for j in range(0, len(poss_char)-1):
            key = str(poss_char[i] + poss_char[j])
            PMF[key] = [0.0, 0.0]

    #iterate over each set of kmers, incrementing corresponding value in corresponding dictionary for each kmer
    for sequence in range(0, len(sequence_kmers)):
        for kmer in sequence_kmers[sequence]:
            PMF[kmer][sequence] += 1.0

    #eliminate unneeded dictionary pairs that are not in either dictionary (optional)
        #both dictionaries should be the same length at this point
    delta_sum = 0.0
    for k, v in PMF.items():
        if(v != [0,0]):
            #normalize each PMF
            PMF[k][0] = PMF[k][0] / len(sequence_kmers[0])
            PMF[k][1] = PMF[k][1] / len(sequence_kmers[1])
            #find the baby deltas
            PMF[k] = abs(PMF[k][0] - PMF[k][1])
            #sum it as we go
            delta_sum += PMF[k]
    #print score
    print("Score: " +  "%.3f" % delta_sum)
    #for each key in either dictionary, change value to float(value/number of kmers in that sequence)
    #find sum for each key (valueA - B)^2  or ABS(valueA - valueB) -- this will be our score
    #output score

    fout.write("Input:\n" + strings[0] + "\n" + strings [1] + "\n")
    fout.write("Score: " + str.format("{0:.3f}", delta_sum))

    fout.close()
    fin.close()
main()
