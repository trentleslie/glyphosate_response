#this script takes a fasta file and an integer that determines
#the minimum length sequence to output
#
#python fasta_minseq.py [reference.fasta] [minimum sequence length]
#python fasta_minseq.py transcriptome.fasta 300

import sys, csv
from Bio import SeqIO

def fasta_minseq(input_fasta, min_seq):
  
	input_file = open(input_fasta)

	fasta_dict = {}
	count_removed = 0
	total_count = 0

	for cur_record in SeqIO.parse(input_fasta, "fasta") :
		if len(cur_record.seq) >= min_seq:		
			fasta_dict.update({cur_record.name:cur_record.seq})
			total_count += 1
		else:
			count_removed += 1
			total_count += 1

	input_file.close()

	output_name = input_fasta + '_' + str(min_seq) + '_filtered.fasta'
	output_file = open(output_name,'w')

	for SeqName in fasta_dict:
		fasta_line = '>' + SeqName + '\n' + str(fasta_dict[SeqName]) + '\n'
		output_file.write(fasta_line)

	output_file.close()
	input_file.close()

	print str(count_removed) + " of " + str(total_count) + " sequences under length of " + str(min_seq) + " were removed."


input_fasta = sys.argv[1]
min_seq = int(sys.argv[2])

fasta_minseq(input_fasta, min_seq)

