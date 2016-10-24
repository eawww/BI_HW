Input:
    Plaintext FASTA format file that contains the multiple sequence alignment for
    for a certain domain.

How to run:
    - Must have Python 3.x installed on machine
    - In command line, navigate to directory containing script and input file
    - Use command:
	python Hw3-Q1-1 [input file] [output file]
    - The output file will contain each individual calculated probability, the
	probability for each pair of amino acids that could be found, the amino
	acid subsititution matrix made from these calculations, and the 
	correlation coefficient between our matrix and the well known BLOSUM 62
	matrix. 