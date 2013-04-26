#PBS -N bowtie2_068
#PBS -l walltime=12:00:00
#PBS -l nodes=2:ppn=8

cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/illumina/002734_068-1-1_CTTGTA_R1_filtered.fastq .
cp /nfs/09/ucn1113/illumina/002734_068-1-1_CTTGTA_R2_filtered.fastq .
cp /nfs/09/ucn1113/bowtie2/purpurea.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.2.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.3.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.4.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.2.bt2 .
bowtie2 -t -I 150 -X 350 --no-discordant -p 4 -1 002734_068-1-1_CTTGTA_R1_filtered.fastq -2 002734_068-1-1_CTTGTA_R2_filtered.fastq purpurea -S 068-1-1.sam
cp *.sam /nfs/09/ucn1113/bowtie2_output/
