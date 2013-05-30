#this script takes output from edgeR and a two-column csv file
#containing the scaffold name and top blast
#it then adds a column to the edgeR output with the annotated top blast
#
#python blast_go_minseq.py [edgeR output] [top blast csv]
#python blast_go_minseq.py output.csv topblasts.csv

import sys, csv

def topblast_deg(input_deg, blast_file):
  
	blast_dict = {}
	count_removed = 0
	total_count = 0

	output_name1 = input_deg + "_annotated.csv"
	output_file1 = open(output_name1, 'w')
	output_file1.write("scaffold,topblast,logFC,logCPM,PValue\n")

	for (cur_record, top_blast) in csv.reader(open(blast_file), delimiter = ','):
		blast_dict.update({cur_record:top_blast})

	for (cur_record, logFC, logCPM, PValue) in csv.reader(open(input_deg), delimiter = '\t'):
		if cur_record in blast_dict:
			output_line = cur_record + ',' + blast_dict[cur_record] + ',' + str(logFC) + ',' + str(logCPM) + ',' + str(PValue) + '\n'
			output_file1.write(output_line)
		else:
                        output_line = cur_record + ',NA,' + str(logFC) + ',' + str(logCPM) + ',' + str(PValue) + '\n'
                        output_file1.write(output_line)

	output_file1.close()

	print "Toast is done!\n"


input_deg = sys.argv[1]
blast_file = sys.argv[2]

topblast_deg(input_deg, blast_file)

