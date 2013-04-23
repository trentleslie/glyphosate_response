#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=8
#PBS -N VXKB_COG_blast2
#PBS -j oe
#PBS -S /bin/bash
#PBS -m ae
date
trap "cd $PBS_O_WORKDIR;mkdir $PBS_JOBID;cp -R $TMPDIR/* $PBS_JOBID" TERM

cd $HOME

cp myva* $TMPDIR
cp VXKB-S* $TMPDIR

cd $TMPDIR

/usr/local/biosoftw/blast-2.2.17/bin/blastall -p blastx -m 8 -v 10 -b 10 -K 0 -a 4 -i VXKB-SOAPdenovo-Trans-assembly.fa_300_filtered.fasta -d myva.fasta -e .001 -o VXKB-COG-blast-300.csv

cp VXKB-COG-blast-300.csv $HOME/

/usr/local/biosoftw/blast-2.2.17/bin/blastall -p blastx -m 8 -v 10 -b 10 -K 0 -a 4 -i VXKB-SOAPdenovo-Trans-assembly.fa_1000_filtered.fasta -d myva.fasta -e .001 -o VXKB-COG-blast-1000.csv

cp VXKB-COG-blast-1000.csv $HOME/

