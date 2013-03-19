#PBS -l walltime=80:00:00
#PBS -l nodes=4:ppn=8
#PBS -N VXKB_blast_13
#PBS -j oe
#PBS -S /bin/bash
#PBS -m ae
date
trap "cd $PBS_O_WORKDIR;mkdir $PBS_JOBID;cp -R $TMPDIR/* $PBS_JOBID" TERM

cd $HOME

cp ./split_fasta/VXKB-SOAPdenovo-Trans-assembly-13.fasta $TMPDIR

cd $TMPDIR

/usr/local/biosoftw/blast-2.2.17/bin/blastall -p blastx -m 7 -v 10 -b 10  -K 0 -a 4 -i VXKB-SOAPdenovo-Trans-assembly-13.fasta -d /nfs/proj01/PZS0002/biosoftw/db/nr -e .001 -o VXKB-SOAP-blast-13.xml

cp VXKB-SOAP-blast-13.xml $HOME/
