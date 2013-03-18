#PBS -N htseq-count_336
#PBS -l walltime=12:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/bowtie2_output/336-1-2-sorted.sam.trimmed.sam .
cp /nfs/09/ucn1113/purpurea.gff .

htseq-count -t mRNA -s no 336-1-2-sorted.sam.trimmed.sam purpurea.gff > 336-1-2.count

cp * /nfs/09/ucn1113/bowtie2_output/
