#this script takes a fasta file and an annotation file (from blast2GO)
#to generate a gff file for subsequence count analysis
#
#csv file has format [SeqName, Hit_Desc, GO-Group, GO-ID, Term]
#
#python gff_generator.py [reference.fasta] [annotations.csv] [outputname.gff]

import sys, csv
from Bio import SeqIO

#function that generates gff file
def gff_generator(input_fasta, input_annotations, output_name):
  
	#Open a FASTA input file of gene nucleotides sequences:
	input_file = open(input_fasta)

	output_file = open(output_name,'w')

	fasta_dict = {}
	annot_dict = {}

	for cur_record in SeqIO.parse(input_fasta, "fasta") :
		new_record_name = str(cur_record.name)
		cur_sequence = str(cur_record.seq)
		fasta_dict.update({new_record_name:len(cur_sequence)})


	for (SeqName, Hit_Desc, GO_Group, GO_ID, Term) in csv.reader(open(input_annotations), delimiter='\t'):
		if SeqName not in annot_dict:
			annot_dict.update({SeqName:Hit_Desc})

	#write custom fasta file
	for SeqName in fasta_dict:
		if SeqName in annot_dict:
		#Fields are: <seqname> <source> <feature> <start> <end> <score> <strand> <frame> [attributes] [comments]
			gff_line = SeqName + '\tblastx\tmRNA\t1\t' + str(fasta_dict[SeqName]) + '\t.\t.\t.\tgene_id \"' + SeqName + '\" ; Hit_Desc \"' + str(annot_dict[SeqName]) + '\"\n'
			output_file.write(gff_line)
		else:
			gff_line = SeqName + '\tblastx\tmRNA\t1\t' + str(fasta_dict[SeqName]) + '\t.\t.\t.\tgene_id \"NA\" ; Hit_Desc \"NA\"\n'
			output_file.write(gff_line)

	output_file.close()
	input_file.close()


input_fasta = sys.argv[1]
input_annotations = sys.argv[2]
output_name = sys.argv[3]

gff_generator(input_fasta, input_annotations, output_name)





