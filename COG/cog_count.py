#this script parses cog info from the whog file and counts blast results
#whog file accessed 4/22/2013
#ftp://ftp.ncbi.nih.gov/pub/COG/COG/
#
#count results are exported in two files - one csv using the COG function
#letter symbols, and one csv using the term provided
#
#usage
#python cog_count.py [cog_data-whog_file] [top_blast_results (one per scaffold)]

import sys, csv

def cog_count(cog_data, blast_data):

	input_file = open(cog_data)
	output_file_name = "cog_count_data.csv"
	output_file = open(output_file_name, 'w')

	cog_dict = {}
	cogterm_dict = {}

	for line in input_file:
		if line[0] is "[":
			curr_cog_letter = line.split(" ")[0]
			curr_cog_id = line.split(" ")[1]
			curr_cog_name = line.split(" ")[2]
		else:
			for item in line.split():
				if ":" not in item:
					if item in cog_dict:
						print item + " is in more than one COG category!"
					else:
						cog_dict[item] = curr_cog_letter
						cogterm_dict[item] = curr_cog_name
	input_file.close()

	input_file2 = open(blast_data)
	cog_count_dict = {}
	cog_term_count_dict = {}
	missed_cog_count = 0
	missed_cog_term_count = 0

	for line in input_file2:
		blast_hit = line.split()[1]
		if blast_hit in cog_dict:
			if cog_dict[blast_hit] in cog_count_dict:
				cog_count_dict[cog_dict[blast_hit]] += 1
			else:
				cog_count_dict[cog_dict[blast_hit]] = 1
		else:
			print "Warning! " + blast_hit + " is not in COG dictionary!"
			missed_cog_count += 1

                if blast_hit in cogterm_dict:
                        if cogterm_dict[blast_hit] in cog_term_count_dict:
                                cog_term_count_dict[cogterm_dict[blast_hit]] += 1
                        else:
                                cog_term_count_dict[cogterm_dict[blast_hit]] = 1
                else:
                        print "Warning! " + blast_hit + " is not in COG dictionary!"
                        missed_cog_term_count += 1


	print "There were " + str(missed_cog_count) + " top blasts that did not have matching COGs.\n"
	print "There were " + str(missed_cog_term_count) + " top blasts that did not have matching COG terms.\n"

	for item in cog_count_dict:
		output_line = item + "\t" + str(cog_count_dict[item]) + "\n"
		output_file.write(output_line)

	output_file.close()

        output_file2_name = "cog_term_count_data.csv"
        output_file2 = open(output_file2_name, 'w')

	for item in cog_term_count_dict:
		output_line = item +"\t" + str(cog_term_count_dict[item]) + "\n"
		output_file2.write(output_line)

	output_file2.close()

cog_data = sys.argv[1]
blast_data = sys.argv[2]

cog_count(cog_data, blast_data)
