#takes two inputs: a small subsequence and a file containing a DNA sequence in FASTA format. It should then output all
# locations of the subsequence within the DNA sequence,including on the complementary strand.
#Eric Wilson
#Partner: Bridget Mohn

import sys


search_term = str(sys.argv[1])
file_name = str(sys.argv[2])

input_file = open(str(file_name), "r")
line_array = []

master_string = ""
complement_string =""
master_positions = []
complement_positions = []

for line in input_file.readlines():
    line_array.append(line)
input_file.close()

del line_array[0]

for line in line_array:
    #remove \n characters
    stripped_line = line.rstrip()
    master_string = master_string + stripped_line

#create complement string
for character in master_string:
    if character == 'A':
        complement_string = complement_string + 'T'
    elif character == 'T':
        complement_string = complement_string + 'A'
    elif character == 'G':
        complement_string = complement_string + 'C'
    elif character == 'C':
        complement_string = complement_string + 'G'
complement_string = complement_string[::-1]

#print("main: " + master_string)
#print("comp: " + complement_string)

#find subsequences in main string
pos = 0
while len(master_string) > 0:
    pos = master_string.find(search_term, pos)
    if pos != -1:
        master_positions.append(pos+1)
        pos += 1
        #print("main: " + str(pos))
    else:
        master_string = ""
pos = 0
while len(complement_string) > 0:
    pos = complement_string.find(search_term, pos)
    if pos != -1:
        complement_positions.append(pos+1)
        pos += 1
        #print("comp: " + str(pos))
    else:
        complement_string = ""

if len(master_positions) == 0 and len(complement_positions) == 0:
    print("Subsequence not found.")
if len(master_positions) > 0:
    print("Subsequence found in file at the following positions:")
    print('\t' + str(master_positions))
if len(complement_positions) > 0:
    print("Subsequence found in complement at the following positions:")
    print("\t" + str(complement_positions))

