#PBS -N bowtie2_358
#PBS -l walltime=12:00:00
#PBS -l nodes=2:ppn=8

cd $TMPDIR

PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/09/ucn1113/illumina/002739_358-1-3_GTCCGC_R1_filtered.fastq .
cp /nfs/09/ucn1113/illumina/002739_358-1-3_GTCCGC_R2_filtered.fastq .
cp /nfs/09/ucn1113/bowtie2/purpurea.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.2.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.3.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.4.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.1.bt2 .
cp /nfs/09/ucn1113/bowtie2/purpurea.rev.2.bt2 .

bowtie2 -t -I 150 -X 350 --no-discordant -p 4 -1 002739_358-1-3_GTCCGC_R1_filtered.fastq -2 002739_358-1-3_GTCCGC_R2_filtered.fastq purpurea -S 358-1-3.sam

cp 358-1-3.sam /nfs/09/ucn1113/bowtie2_output/
