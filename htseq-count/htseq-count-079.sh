#PBS -N htseq-count_079
#PBS -l walltime=12:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/bowtie2_output/079-1-3-sorted.sam.trimmed.sam .
cp /nfs/09/ucn1113/purpurea.gff .

htseq-count -t mRNA -s no 079-1-3-sorted.sam.trimmed.sam purpurea.gff > 079-1-3.count

cp * /nfs/09/ucn1113/bowtie2_output/
