#!/bin/bash --login
#PBS -l walltime=01:00:00
#PBS -l select=1:ncpus=2
#PBS -N 2017_cr_nojoin_no_golay_serial
#PBS -A d411-training

cd $PBS_O_WORqKDIR

module load miniconda/python2

# setting temporary directory
mkdir -p ~/qiime_tmp
export TMPDIR=~/qiime_tmp

# loading virtualenv
echo "loading virtualenv" 

source activate qiime1

# counting sequences
count_seqs.py 
-i ~/2018_02_smb/slout/seqs.fna
-o countseqs

source deactivate
