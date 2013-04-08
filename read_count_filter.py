#this script takes a merged count csv file and two integers for filtering -
#the first integer determines the minimum number of reads per sample
#the second integer determines the minimum number of samples that need to
#contain the minimum number of reads
#
#this script is only set to handle a merged count csv file with exactly six samples
#this can be changed in the for loop reading in the csv file
#
#python read_count_filter.py [merged count csv file] [minimum read count] [minimum number of samples]
#python read_count_filter.py merged_counts.csv 10 2

import sys, csv

def gene_count_trim(input_counts, min_reads, min_samples):
  
	input_file = open(input_counts)

	output_name_blast = 'merged_counts_filtered.csv'
	output_file1 = open(output_name_blast,'w')
	output_file1.write("068-1-1.tsv, 077-1-2.tsv, 079-1-3.tsv, 336-1-2.tsv, 351-1-2.tsv, 358-1-3.tsv\n")

	count_removed = 0
	total_count = 0

	for (cur_sample, sam1, sam2, sam3, sam4, sam5, sam6) in csv.reader(open(input_counts), delimiter = '\t'):
		read_counts_list = [int(sam1), int(sam2), int(sam3), int(sam4), int(sam5), int(sam6)]
		min_read_count = 0

		for item in read_counts_list:
			if item >= min_reads:
				min_read_count += 1
		
		if min_read_count >= min_samples:
			output_line = cur_sample + "," + str(sam1) + "," + str(sam2) + "," + str(sam3) + "," + str(sam4) + "," + str(sam5) + "," + str(sam6) + "\n"
			output_file1.write(output_line)
			total_count += 1
		else:
			count_removed += 1
			total_count += 1

	input_file.close()
	output_file1.close()

	print str(count_removed) + " of " + str(total_count) + " sequences were removed.\n"

input_counts = sys.argv[1]
min_reads = int(sys.argv[2])
min_samples = int(sys.argv[3])

gene_count_trim(input_counts, min_reads, min_samples)

