#this script takes output from DESeq and a two-column csv file
#containing the scaffold name and top blast
#it then adds a column to the edgeR output with the annotated top blast
#
#python blast_go_minseq.py [DESeq output] [top blast csv]
#python blast_go_minseq.py output.csv topblasts.csv 

import sys, csv

def topblast_deg(input_deg, blast_file):
  
	blast_dict = {}
	count_removed = 0
	total_count = 0

	output_name1 = input_deg + "_annotated.csv"
	output_file1 = open(output_name1, 'w')
	output_file1.write("scaffold,top_blast,baseMean,baseMeanA,baseMeanB,foldChange,log2FoldChange,pval,padj\n")

	for (cur_record, top_blast) in csv.reader(open(blast_file), delimiter = ','):
		blast_dict.update({cur_record:top_blast})

	for (cur_record, baseMean, baseMeanA, baseMeanB, foldChange, log2FoldChange, pval, padj) in csv.reader(open(input_deg), delimiter = '\t'):
		if cur_record in blast_dict:
			output_line = cur_record + ',' + blast_dict[cur_record] + ',' + str(baseMean) + ',' + str(baseMeanA) + ',' + str(baseMeanB) + ',' + str(foldChange) + ',' + str(log2FoldChange) + ',' + str(pval) + ',' + str(padj) + '\n'
			output_file1.write(output_line)
		else:
                        output_line = cur_record + ',NA,' + str(baseMean) + ',' + str(baseMeanA) + ',' + str(baseMeanB) + ',' + str(foldChange) + ',' + str(log2FoldChange) + ',' + str(pval) + ',' + str(padj) + '\n'
                        output_file1.write(output_line)

	output_file1.close()

	print "Toast is done!\n"


input_deg = sys.argv[1]
blast_file = sys.argv[2]

topblast_deg(input_deg, blast_file)

