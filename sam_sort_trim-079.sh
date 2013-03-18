#PBS -N sam_sort_trim_079
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/bowtie2_output/079-1-3.sam .
cp /nfs/09/ucn1113/bowtie2_output/sam_readname_trim.pl .

export LC_ALL=POSIX
sort -s -k 1,1 079-1-3.sam > 079-1-3-sorted.sam
perl sam_readname_trim.pl 079-1-3-sorted.sam

cp * /nfs/09/ucn1113/bowtie2_output/
