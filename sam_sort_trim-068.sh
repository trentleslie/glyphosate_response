#PBS -N sam_sort_trim_068
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/bowtie2_output/068-1-1.sam .
cp /nfs/09/ucn1113/bowtie2_output/sam_readname_trim.pl .

export LC_ALL=POSIX
sort -s -k 1,1 068-1-1.sam > 068-1-1-sorted.sam
perl sam_readname_trim.pl 068-1-1-sorted.sam

cp * /nfs/09/ucn1113/bowtie2_output/
