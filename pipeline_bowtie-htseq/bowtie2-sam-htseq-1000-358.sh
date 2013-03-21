#PBS -N bowtie2_sam_htseq_358
#PBS -l walltime=30:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/11/ucn1221/illumina/002739_358-1-3_GTCCGC_R1_filtered.fastq .
cp /nfs/11/ucn1221/illumina/002739_358-1-3_GTCCGC_R2_filtered.fastq .
cp /nfs/09/ucn1113/VXKB-SOAPdenovo-Trans-assembly.fa_1000_filtered.fasta .
cp /nfs/09/ucn1113/bowtie2_output/sam_readname_trim.pl .
cp /nfs/09/ucn1113/purpurea.gff .

bowtie2-build -f VXKB-SOAPdenovo-Trans-assembly.fa_1000_filtered.fasta purpurea

bowtie2 -t -I 150 -p 4 -1 002739_358-1-3_GTCCGC_R1_filtered.fastq -2 002739_358-1-3_GTCCGC_R2_filtered.fastq purpurea -S 358-1-3.sam

export LC_ALL=POSIX
sort -s -k 1,1 358-1-3.sam > 358-1-3-sorted.sam
perl sam_readname_trim.pl 358-1-3-sorted.sam

htseq-count -t mRNA -s no 358-1-3-sorted.sam.trimmed.sam purpurea.gff > 358-1-3.count

cp 358-1-3-sorted.sam.trimmed.sam /nfs/09/ucn1113/bowtie2_output/trimmed_1000_ref/
cp 358-1-3.count /nfs/09/ucn1113/bowtie2_output/trimmed_1000_ref/
