#this script takes two separated lists of 1-to-1 data and merges
#the two sets of data into a single file for further analysis
#
#it assumes the first input file [input1.csv] is the more comprehensive
#data set (it does not put "NA" into the output file - it only reports that
#the data in the first input file is not present)
#
#the two files are *TAB* csv files, each of which contain two columns-
#the first column containing the id to be associated with the data
#and the second column containing the data, such as:
#
#scaffold-id-123	24.3
#
#in one file and:
#
#scaffold-id-123	492
#
#would result in a three-column csv such as:
#
#scaffold-id-123	24.3	492
#
#USAGE
#python data_merge.py [input1.csv] [input2.csv] [output.csv]
#EXAMPLE
#python data_merge.py scaffold_lengths.csv scaffold_expression.csv len_exp_data.csv

import sys, csv

#custom fasta file from list
def custom_fasta(lengths, expressions, output_file_name):
  
	input_file = open(lengths)
	input_file2 = open(expressions)
	output_file = open(output_file_name ,'w')

	lengths_dict = {}
	expressions_dict = {}

	for (scaffold, length) in csv.reader(open(lengths), delimiter='\t'):
		if scaffold in lengths_dict:
			print scaffold + " occurs twice in " + lengths + "."
		else:
			lengths_dict.update({scaffold:length})

        for (scaffold, expression) in csv.reader(open(expressions), delimiter='\t'):
                if scaffold in expressions_dict:
                        print scaffold + " occurs twice in " + expressions + "."
                else:
                        expressions_dict.update({scaffold:expression})

	for scaffold in expressions_dict:
		if scaffold in lengths_dict:
			output_line = scaffold + '\t' + str(lengths_dict[scaffold]) + '\t' + str(expressions_dict[scaffold]) + '\n'
			output_file.write(output_line)
		else:
			print scaffold + " is not in " + lengths + " file!"

	output_file.close()
	input_file.close()


input_list1 = sys.argv[1]
input_list2 = sys.argv[2]
output_file_name = sys.argv[3]

custom_fasta(input_list1, input_list2, output_file_name)



