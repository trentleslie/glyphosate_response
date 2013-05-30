#this script takes a list of desired sequence names and the reference
#fasta file to create a custom fasta file and raw primer3 input
#(primer3 input is then used for primer3_core input on the command line,
#if it is installed)
#
#list of sequence names is a single-column csv file
#reference file is the fasta file from which the sequences will be pulled
#output name is the name you want the output files to be named

#python custom_fasta.py [list.csv] [reference.fasta] [outputname]

import sys, csv
from Bio import SeqIO

#custom fasta file from list
def custom_fasta(fasta_list, input_fasta, output_fasta):
  
	#Open a FASTA input file of gene nucleotides sequences:
	input_file = open(input_fasta)

	output_file = open(output_fasta,'w')

	#load custom list from file and remove duplicates
	scaffold_list = [custom_list_id for custom_list_id in csv.reader(open(fasta_list))]
	scaffold_list = [item for sublist in scaffold_list for item in sublist]
	scaffold_list = list(set(scaffold_list))

	#start loading reference fasta into dictionary

	fasta_dict = {}

	#Get SeqIO to read this file in fasta format
	for cur_record in SeqIO.parse(input_file, "fasta") :
		fasta_dict.update({cur_record.name:cur_record.seq})

	#write custom fasta file
	for item in scaffold_list:
		if item in fasta_dict:
			fasta_line = '>' + item + '\n' + str(fasta_dict[item]) + '\n'
			output_file.write(fasta_line)
		else:
			print item + " is not in reference fasta file!"

	output_file.close()
	input_file.close()

#fasta file to raw primer3 input
def custom_primer3(custom_fasta):

	input_file = open(custom_fasta)

	output_name = custom_fasta + ".p3"
	output_file = open(output_name,'w')
	
	for cur_record in SeqIO.parse(input_file, "fasta") :

		output_line = "SEQUENCE_ID=%s\nSEQUENCE_TEMPLATE=%s\nPRIMER_TASK=pick_detection_primers\nPRIMER_PICK_LEFT_PRIMER=1\nPRIMER_PICK_INTERNAL_OLIGO=0\nPRIMER_PICK_RIGHT_PRIMER=1\nPRIMER_OPT_SIZE=20\nPRIMER_MIN_SIZE=18\nPRIMER_MAX_SIZE=27\nPRIMER_MAX_NS_ACCEPTED=1\nPRIMER_PRODUCT_SIZE_RANGE=150-215\nP3_FILE_FLAG=1\nPRIMER_EXPLAIN_FLAG=1\nPRIMER_NUM_RETURN=10\n=\n" %(cur_record.name, cur_record.seq)
		output_file.write(output_line)

	output_file.close()
	input_file.close()



input_list = sys.argv[1]
fasta_reference = sys.argv[2]
output_name = sys.argv[3]

custom_fasta(input_list, fasta_reference, output_name)
custom_primer3(output_name)




