#Bridget Mohn and Eric Wilson
#CS 466R
#Homework 1
#Reads an input filename from command line, opens the file, reads each character
#in the file to see whether the file contains a DNA, RNA, or Protein sequence 


import sys

#Input filename is taken from the command line which is the second argument
InputFile = sys.argv[1]

#Opens the file read from the command line
fin = open(str(InputFile), "r")

#Array and array length needed to turn the lines in the file one string
temp = []
sequence_length = 80
sequence = ""

#To take the header off of the biological sequence
for line in fin.readlines():
    #Add each line in the file into the array
    temp.append(line)

#Delete the first line since it's not apart of the sequence
del temp[0]

#Put all the lines of the file into one big string
for line in temp:
    modified_line = line.strip()
    sequence = sequence + modified_line

seq_type = ""

for char in sequence:
    #Checks if U is in the sequence since it is unique to RNA
    if('U' in line):
        #print("RNA")
        seq_type = "RNA"
        
    #Checks the file for all of the possible amino acid codes that make a protein
    elif('B' in line or 'D' in line or 'E' in line or 'F' in line or
         'H' in line or 'I' in line or 'K' in line or 'L' in line or
         'M' in line or 'N' in line or 'Q' in line or 'X' in line or
         'R' in line or 'S' in line or 'P' in line or 'V' in line or
         'W' in line or 'Y' in line or 'Z' in line):
        #print("Protein")
        seq_type = "Protein"
        
    #Checks if T is in the sequence since it is only found in DNA and Protein
    elif('T' in line):
        #print("DNA or Protein")
        seq_type = "DNA or Protein"
        
    #If just A, G, and C are found in the sequence then it could be any of the options
    elif('A' in line and 'G' in line and 'C' in line):
        #print("DNA or RNA or Protein")
        seq_type = "DNA or RNA or Protein"
        
    #If none of those are found in the sequence then it is none of the above
    else:
        #print("None")
        seq_type = "None"

print(seq_type)


#Close input file
fin.close()




