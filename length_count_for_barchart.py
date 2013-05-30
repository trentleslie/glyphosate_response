#this script counts for a histogram
#assumes a tab-delimited fild that has a number field in
#the second column (this was intended for scaffold lengths)
#
#python length_count_for_barchart.py [lengths.csv]

import sys, csv

#custom fasta file from list
def custom_fasta(lengths):
  
	input_file = open(lengths)
	output_name = lengths + "_counted.csv"
	output_file = open(output_name ,'w')
	count_dict = {}
	
	for line in input_file:
		curr_length = int(line.split()[1])
		if curr_length < 200:
			if str(200) in count_dict:
				count_dict[str(200)] += 1
			else:
				count_dict[str(200)] = 1
		if curr_length < 400 and curr_length >= 200:
                        if str(400) in count_dict:
                                count_dict[str(400)] += 1
                        else:
                                count_dict[str(400)] = 1
                if curr_length < 600 and curr_length >= 400:
                        if str(600) in count_dict:
                                count_dict[str(600)] += 1
                        else:
                                count_dict[str(600)] = 1
                if curr_length < 800 and curr_length >= 600:
                        if str(800) in count_dict:
                                count_dict[str(800)] += 1
                        else:
                                count_dict[str(800)] = 1
                if curr_length < 1000 and curr_length >= 800:
                        if str(1000) in count_dict:
                                count_dict[str(1000)] += 1
                        else:
                                count_dict[str(1000)] = 1
                if curr_length < 1200 and curr_length >= 1000:
                        if str(1200) in count_dict:
                                count_dict[str(1200)] += 1
                        else:
                                count_dict[str(1200)] = 1
                if curr_length < 1400 and curr_length >= 1200:
                        if str(1400) in count_dict:
                                count_dict[str(1400)] += 1
                        else:
                                count_dict[str(1400)] = 1
                if curr_length < 1600 and curr_length >= 1400:
                        if str(1600) in count_dict:
                                count_dict[str(1600)] += 1
                        else:
                                count_dict[str(1600)] = 1
                if curr_length < 1800 and curr_length >= 1600:
                        if str(1800) in count_dict:
                                count_dict[str(1800)] += 1
                        else:
                                count_dict[str(1800)] = 1
                if curr_length < 2000 and curr_length >= 1800:
                        if str(2000) in count_dict:
                                count_dict[str(2000)] += 1
                        else:
                                count_dict[str(2000)] = 1
                if curr_length < 2200 and curr_length >= 2000:
                        if str(2200) in count_dict:
                                count_dict[str(2200)] += 1
                        else:
                                count_dict[str(2200)] = 1
                if curr_length < 2400 and curr_length >= 2200:
                        if str(2400) in count_dict:
                                count_dict[str(2400)] += 1
                        else:
                                count_dict[str(2400)] = 1
                if curr_length < 2600 and curr_length >= 2400:
                        if str(2600) in count_dict:
                                count_dict[str(2600)] += 1
                        else:
                                count_dict[str(2600)] = 1
                if curr_length < 2800 and curr_length >= 2600:
                        if str(2800) in count_dict:
                                count_dict[str(2800)] += 1
                        else:
                                count_dict[str(2800)] = 1
                if curr_length >= 3000:
                        if ">3000" in count_dict:
                                count_dict[">3000"] += 1
                        else:
                                count_dict[">3000"] = 1

      	for item in count_dict:
		output_line = item + '\t' + str(count_dict[item]) + '\n'
		output_file.write(output_line)

	output_file.close()
	input_file.close()


input_list = sys.argv[1]

custom_fasta(input_list)



