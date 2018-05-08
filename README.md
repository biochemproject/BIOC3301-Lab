BIOC3301 - Advanced Practical in Molecular Biology

The influence of nutrient levels and pH on the soil microbiome composition of samples collected from Green spaces in central London

This repository consisits of all the batch scripts used to carry out data analysis on the paired end reads generated through Illumina MiSeq sequencing.
The 16s rRNA v4 hypervariable region was amplified from genomic DNA (gDNA) extracted from 30 different soil samples collected from a number of green spaces across central London.
Data analysis was carried out using high performace computer cluster (Cirrus) based in the University of Edinburgh. 

Data Analysis was carried out in the following order, using the described scripts:

1. Joining Paired Ends 
- join_paired_ends.py
2. Demultiplexing of Reads according to barcodes
- split_libraries_fastq.py
3. Counting Sequences 
- count_seqs.py
4. The picking of closed reference OTUs using the SILVA 128 database
- pick_closed_reference_otus.py
5. Core diversity analysis to establish alpha and beta diversity measures 
- core_diversity_analyses.py
6. The conversion of the 3D PCoA plots in to 2D PCoA plots 
- make_2d_plots.py

Satistical Analysis was carried out in the following order, using the described scripts:

1. comparing categories to analyse the statistical significance of sample groupings using distance matrices (ANOSIM method) 
- compare_categories.py Nitrogen
- compare_categories.py Phosphorus
- compare_categories.py Potassium
- compare_categories.py pH

2. Summarising the taxa table 
- summarize_taxa.py

3. group significance used to compare OTU frequencies across sample groups using the Kruskal-Wallis
- group_significance.py Nitrogen
- group_significance.py Phosphorus
- group_significance.py Potassium
- group_significance.py pH
