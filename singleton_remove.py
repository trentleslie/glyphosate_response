#this script removes singletons from a paired-end sam file
#
#this is necessary because bowtie2 does not generate sam files
#containing only uniquely mapped reads
#
#to remove those that are not uniquely mapped in sam files, use:
#sed '/XS:/d' your_alignment_file.sam > your_alignment_file_1alignmentonly.sam
#(from MGineste - http://seqanswers.com/forums/showthread.php?t=23389
#
#this removes all those that are not uniquely mapped, but doesn't remove
#paired-end mates that ARE uniquely mapped, which causes error messages
#from htseq-count
#
#like htseq-count, this script requires paired-end reads to have the 
#same name (but due to the use of a dictionary, does not require it to be sorted)
#
#USAGE
#python singleton_remove.py [messy_file.sam]

import sys

def singleton_remove(sam_input):

	input_file = open(sam_input)
	output_file_name = sam_input + ".cleaned.sam"
	output_file = open(output_file_name, 'w')

	read_dict = {}

	for line in input_file:
		if line[0] is "@":
			output_file.write(line)
		else:
			if line.split("\t")[0] in read_dict:
				output_file.write(read_dict[line.split("\t")[0]])
				output_file.write(line)
			else:
				read_dict[line.split("\t")[0]] = line

	input_file.close()
	output_file.close()

sam_input = sys.argv[1]

singleton_remove(sam_input)
