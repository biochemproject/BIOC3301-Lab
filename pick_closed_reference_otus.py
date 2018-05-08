#!/bin/bash --login
#PBS -l walltime=03:00:00
#PBS -l select=1:ncpus=24
#PBS -N 2017_cr_nojoin_no_golay_serial
#PBS -A d411-training

cd $PBS_O_WORKDIR

#load modules and qiime
module load miniconda/python2

# setting temporary directory
export TMPDIR=~/qiime_tmp
mkdir -p ~/qiime_tmp

# loading virtualenv
echo "loading virtualenv"

source activate qiime1

pick_closed_reference_otus.py \
-i ~/2018_02_smb/slout/seqs.fna \
-r ~/SILVA_128_QIIME_release/rep_set/rep_set_all/97/97_otus.fasta \
-o ~/2018_02_smb/SILVA_otus \
-t ~/SILVA_128_QIIME_release/taxonomy/16S_only/97/majority_taxonomy_all_levels.txt \

source deactivate                 
