#PBS -l walltime=30:00:00
#PBS -l nodes=4:ppn=8
#PBS -N VXKB_blast
#PBS -j oe
#PBS -S /bin/bash
#PBS -m ae
date
trap "cd $PBS_O_WORKDIR;mkdir $PBS_JOBID;cp -R $TMPDIR/* $PBS_JOBID" TERM

cd $HOME

cp ./bowtie/VXKB-SOAPdenovo-Trans-assembly.fasta $TMPDIR

cd $TMPDIR

/usr/local/biosoftw/blast-2.2.17/bin/blastall -p blastx -m 7 -v 10 -a 8 -i VXKB-SOAPdenovo-Trans-assembly.fasta -d /nfs/proj01/PZS0002/biosoftw/db/nr -e .001 -o VXKB-SOAP-blast.xml

cp VXKB-SOAP-blast.xml $HOME/
