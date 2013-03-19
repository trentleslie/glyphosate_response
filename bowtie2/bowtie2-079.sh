#PBS -N bowtie2_079
#PBS -l walltime=12:00:00
#PBS -l nodes=2:ppn=8

cd $PBS_O_WORKDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/illumina/002736_079-1-3_AGTTCC_R1_filtered.fastq .
cp /nfs/09/ucn1113/illumina/002736_079-1-3_AGTTCC_R2_filtered.fastq .
cp /nfs/09/ucn1113/bowtie2/purpurea.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.2.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.3.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.4.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.2.bt2 .

bowtie2 -t -I 150 -p 4 -1 002736_079-1-3_AGTTCC_R1_filtered.fastq -2 002736_079-1-3_AGTTCC_R2_filtered.fastq purpurea -S 079-1-3.sam

cp 079-1-3.sam /nfs/09/ucn1113/bowtie2_output/
