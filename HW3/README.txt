Input:
    Plaintext FASTA format file that contains the multiple sequence alignment for
    for a certain domain.

How to run:
    - Must have Python 3.x installed on machine
    - In command line, navigate to directory containing script and input file
    - Use command:
	python Hw3_Q1.py [input file] [output file]
	or python3 Hw3_Q1.py [input file] [output file]
	if your machine defaults to python 2.x
    - The output file will contain a plaintext, whitespace formatted matrix of
	substitution values for the given domain.
    - The file ‘log.txt` will contain all intermediate data including each 
	individual calculated probability for all amino acids and pairs,
	individual calculated totals for all amino acids and pairs,
	the final table

Bonus!:
	Use correlator.py to find the correlation coefficient between any output
	from Hw3_Q1.py and the BLOSUM62 matrix.

	python correlation.py [output from Hw3_Q1]
	or
	python3 correlation.py [output from Hw3_Q1]