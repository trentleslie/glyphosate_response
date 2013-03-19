#!/usr/bin/perl 
#
#trims the last two characters of paired-end read names in a sam file so
#they are recognized as paired-end by htseq-count
#
#in this case, first read names ended with "/1" and second read names
#ended with "/2", and htseq-count requires paired-end reads to have
#identical names, so this script removes the last two characters of each
#read name
#
#usage
#perl sam_readname_trim.pl <sam file>
use strict; use warnings;

open(IN, "<$ARGV[0]") or die "error reading $ARGV[0] for reading"; 
open(OUT, ">$ARGV[0].trimmed.sam") or die "error creating $ARGV[0].trimmed.sam";

my @name_fields = ();
my $updated_line;

while (<IN>) {
	if (substr($_, 0, 1) eq '@'){
		print OUT "$_";
	}
	else {
		@name_fields = split("\t", $_);
		$name_fields[0] = substr($name_fields[0], 0, length($name_fields[0])-2);
		$updated_line = join("\t", @name_fields);
		print OUT "$updated_line";
	}
} 
close IN;
