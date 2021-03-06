# List of Scripts and What They Do  
1. Data Pre-processing  
* *SampleID_mapping.py*: Creates dictionary from the metadata to assign sample ID to
 the NASH identifiers. Regenerates as output raw counts with the NASH ID.  
* *ensembl_reference_dict.py*: Generates a file for downstream dictionary use.  
* *sum_transcripts_to_genes.py*: Excludes low-quality samples, sums technical replicates,
and sums the transcripts that map to the same gene. Output file ready for DE analysis.

2. Differential Expression Analysis
* *DESeq2.Rmd/DESeq2.R*: Takes in the processed raw_count files, appropriate the
input for DESeq2 in R then generate .tsv files containing the statistical analyses
across the different disease states.   
* *DESeq.Rmd/DESeq.R*: Similar to DESeq2, but appropriates it for DESeq instead.   
* *Limma.Rmd/limma.R*: Loads the processed raw_count files and conduct DE analysis using
the limma package.  

3. Post-DESeq2  
* *prep_piano.py*: Converts the Ensembl gene IDs to HPA gene symbols. Also
filters down the results to only the protein-coding genes.
* *filter_deseq2.py*: Collects all the genes that are differentially expressed
(FDR threshold: 5%) then append information of the type of RNA expression and the
TPM value from the Human Protein Atlas.  
* *Piano.Rmd/Piano.R*: Runs the R-package Piano for pathway analysis.  
* *visualisation.Rmd*: Takes in DESeq2 results and generate volcano plots!


Other:  
* *generate_transcript.sh*: subsets Ensembl reference GFF based on transcripts.
* *qval_check.Rmd*: miniscript to check for DE-genes at FDR 5%.  
* *qval_histogram.py*: a script to generate a histogram of the q-values from DESeq2.  
* *complexity_reduction*: an attempt to do some clustering within a sample group.  
