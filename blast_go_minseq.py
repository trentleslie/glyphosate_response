#this script takes a fasta file, an integer that determines
#the minimum length sequence, a csv file with blast info, and a
#csv file with go info (csv files are two column - first column
#is sequence name that matches fasta file and second file is top
#blast hit or go info)
#
#python blast_go_minseq.py [reference.fasta] [minimum sequence length] [blast_file] [go_file]
#python blast_go_minseq.py transcriptome.fasta 300 topblasts.csv gocats.csv

import sys, csv
from Bio import SeqIO

def blast_go_minseq(input_fasta, min_seq, blast_file, go_file):
  
	input_file = open(input_fasta)

	fasta_dict = {}
	blast_dict = {}
	go_dict = {}
	count_removed = 0
	total_count = 0

	for cur_record in SeqIO.parse(input_fasta, "fasta") :
		if len(cur_record.seq) >= min_seq:		
			fasta_dict.update({cur_record.name:cur_record.seq})
			total_count += 1
		else:
			count_removed += 1
			total_count += 1

	for (cur_record, top_blast) in csv.reader(open(blast_file), delimiter = ','):
		blast_dict.update({cur_record:top_blast})

	for (cur_record, go_info) in csv.reader(open(go_file), delimiter = ','):
		if cur_record in go_dict:
			go_dict[cur_record].append(go_info)
		else:
			go_dict_list = []
			go_dict_list.append(go_info)
			go_dict.update({cur_record:go_dict_list})

	input_file.close()

	output_name_blast = blast_file + '_' + str(min_seq) + '_filtered.csv'
	output_file1 = open(output_name_blast,'w')

	output_name_go = go_file + '_' + str(min_seq) + '_filtered.csv'
	output_file2 = open(output_name_go, 'w')

	count_blast = 0

	for SeqName in fasta_dict:
		if SeqName in blast_dict:
			blast_line = SeqName + ',' + blast_dict[SeqName] + '\n'
			output_file1.write(blast_line)
		else:
			count_blast += 1

	output_file1.close()

	count_go = 0

	for SeqName in fasta_dict:
		if SeqName in go_dict:
			for item in go_dict[SeqName]:
				go_line = SeqName + ',' + item + '\n'
				output_file2.write(go_line)
		else:
			count_go += 1
			
	output_file2.close()

	print str(count_removed) + " of " + str(total_count) + " sequences under length of " + str(min_seq) + " were removed.\n"
	print "According to these results, " + str(count_blast) + " sequences did not have blast results and " + str(count_go) + " sequences did not have GO info.\n"


input_fasta = sys.argv[1]
min_seq = int(sys.argv[2])
blast_file = sys.argv[3]
go_file = sys.argv[4]

blast_go_minseq(input_fasta, min_seq, blast_file, go_file)

