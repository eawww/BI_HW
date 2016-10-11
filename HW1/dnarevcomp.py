#takes a file containing a DNA sequence in FASTA format as input and outputs its reverse complement
#"I put my thing down, flip it, and reverse it." -Missy Elliot
#Eric Wilson
#Partner: Bridget Mohn
#input file source: https://www.genomatix.de/online_help/help/sequence_formats.html
import sys

input_file_name = str(sys.argv[1])
output_file_name = str(sys.argv[2])
LINE_LENGTH = 80

input_file = open(str(input_file_name), "r")
line_array = []

master_string = ""

for line in input_file.readlines():
    line_array.append(line)
input_file.close()
#save the little header thing
description = line_array[0]
#delete header from line arr
del line_array[0]

#concatenate all lines into a single string
for line in line_array:
    #remove \n characters
    stripped_line = line.rstrip()
    master_string = master_string + stripped_line

#reverse it
master_string = master_string[::-1]

#invert it
temp_str = ""
for character in master_string:
    if character == 'A':
        temp_str = temp_str + 'T'
    elif character == 'T':
        temp_str = temp_str + 'A'
    elif character == 'G':
        temp_str = temp_str + 'C'
    elif character == 'C':
        temp_str = temp_str + 'G'
    else:
        temp_str = temp_str + character
master_string = temp_str

output_file = open(output_file_name, "w")
output_file.write(description)
while len(master_string) > 0:
    if len(master_string) >= 70:
        output_file.write(master_string[0:70] + "\n")
        master_string = master_string[70:]
    else:
        output_file.write(master_string)
        master_string = ""


output_file.close()
