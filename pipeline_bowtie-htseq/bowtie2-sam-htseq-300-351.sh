#PBS -N bowtie2_sam_htseq_351
#PBS -l walltime=30:00:00
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR
cd $TMPDIR
PATH=$PATH":/nfs/09/ucn1113/samtools-0.1.18/:/nfs/09/ucn1113/bowtie2-2.1.0/:/nfs/09/ucn1113/HTSeq-0.5.4p1/build/scripts-2.7/"

cp /nfs/11/ucn1221/illumina/002738_351-1-2_CCGTCC_R1_filtered.fastq .
cp /nfs/11/ucn1221/illumina/002738_351-1-2_CCGTCC_R2_filtered.fastq .
cp /nfs/09/ucn1113/VXKB-SOAPdenovo-Trans-assembly.fa_300_filtered.fasta .
cp /nfs/09/ucn1113/bowtie2_output/sam_readname_trim.pl .
cp /nfs/09/ucn1113/purpurea.gff .

bowtie2-build -f VXKB-SOAPdenovo-Trans-assembly.fa_300_filtered.fasta purpurea

bowtie2 -t -I 150 -p 4 -1 002738_351-1-2_CCGTCC_R1_filtered.fastq -2 002738_351-1-2_CCGTCC_R2_filtered.fastq purpurea -S 351-1-2.sam

export LC_ALL=POSIX
sort -s -k 1,1 351-1-2.sam > 351-1-2-sorted.sam
perl sam_readname_trim.pl 351-1-2-sorted.sam

htseq-count -t mRNA -s no 351-1-2-sorted.sam.trimmed.sam purpurea.gff > 351-1-2.count

cp 351-1-2-sorted.sam.trimmed.sam /nfs/09/ucn1113/bowtie2_output/trimmed_300_ref/
cp 351-1-2.count /nfs/09/ucn1113/bowtie2_output/trimmed_300_ref/
