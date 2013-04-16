#!/usr/bin/perl 
#
#extracts qname, rname, pos, and mapq from sam file and puts them into a csv file
#also makes a second csv file with only pos and mapq info
#
#usage
#perl sam_data_extract.pl <sam file>
use strict; use warnings;

open(IN, "<$ARGV[0]") or die "error reading $ARGV[0] for reading"; 
open(OUT, ">$ARGV[0].csv") or die "error creating $ARGV[0].csv";
open(OUT2, ">$ARGV[0]_nonames.csv") or die "error creating $ARGV[0]_nonames.csv";

#header?
#print OUT "QNAME\tRNAME\tPOS\tMAPQ\n";
#print OUT2 "POS\tMAPQ\n";

my @name_fields;
my @out_fields;
my $updated_line;

while (<IN>) {
	if (substr($_, 0, 1) eq '@'){
	}
	else {
		@name_fields = split("\t", $_);

		@out_fields = ($name_fields[0], $name_fields[2], $name_fields[3], $name_fields[4]);
		$updated_line = join("\t", @out_fields);
		print OUT "$updated_line\n";

		@out_fields = ($name_fields[3], $name_fields[4]);
                $updated_line = join("\t", @out_fields);
		print OUT2 "$updated_line\n";
	}
} 
close IN;
