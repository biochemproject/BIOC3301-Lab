#!/bin/bash --login
#PBS -l walltime=03:00:00
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

# core diversity analysis
core_diversity_analyses.py -i ~/2018_02_smb/SILVA_otus/otu_table.biom -m ~/2018_02_smb/mapcomplete.tsv -t ~/SILVA_128_QIIME_release/trees/97/97_otus.tre -o ~/2018_02_smb/core_output -e 627

source deactivate
