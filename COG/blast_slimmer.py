#this script takes the top (first) blast hit for each query input
#and wites them to a new file
#
#made for blastall -m 8 output
#
#usage
#python blast_slimmer.py [blast_output_file]


import sys, csv

def blast_slimmer(blast_data):

	input_file = open(blast_data)
	output_file_name = blast_data + "_topblast_data.csv"
	output_file = open(output_file_name, 'w')

	cog_dict = {}
	skip_count = 0
	saved_count = 0
	total_count = 0

	for line in input_file:
		if line.split()[0] in cog_dict:
			skip_count += 1
			total_count += 1
		else:
			cog_dict[line.split()[0]] = line.split()[1]
			output_file.write(line)
			saved_count += 1
			total_count += 1

	input_file.close()
	output_file.close()

	print str(total_count) + " blast results processed.  " + str(saved_count) + " blast results were saved and " + str(skip_count) + " blast results were discarded.\n"

blast_data = sys.argv[1]

blast_slimmer(blast_data)
