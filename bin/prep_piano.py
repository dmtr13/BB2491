import glob, os
## Downloaded protein coding genes from Protein Atlas
## https://www.proteinatlas.org/about/download
### Step 1: Load the dictionary
gene_sym = dict()
with open('../reference/proteinatlas.tsv', 'r') as en:
    en = en.readlines()
    print ("Generating dictionary...")
    for line in en[1:]:
        line = line.split('\t')
        key, val = line[2], line[0]
        # print (key)
        gene_sym[key] = val
    print ("Done.")

### Step 2: Convert ENSG to gene_symbol
## Example results:
## 'ENSG' "baseMean"	"log2FoldChange"	"lfcSE"	"stat"	"pvalue"	"padj"
## "ENSG00000000457" 197.965428379746 -0.0103982321067529 0.126923155869286
## -0.0819254141258643 0.93470602481617 0.999690735919201
### FOR DESEQ/2
# os.popen("rm ../results/DESeq/*genesymb*")
# dir = "../results/DESeq/"
# for deseq2 in glob.glob((dir+"??_DESeq.tsv")):
#     print ("Processing {}...".format(deseq2))
#     newname = deseq2.replace(dir, "").replace("_DESeq.tsv","")
#     newname += "_DESeq_genesymb.tsv"
#     gs = open(dir+newname, 'w')
#     with open(deseq2, 'r') as ds:
#         ds = ds.readlines()
#         gs.write("\"gene_symbol\""+'\t'+'\t'.join((ds[0].split())[1:]))
#         for lines in ds[1:]:
#             lines = lines.split()
#             words = lines[1].replace("\"","")
#             print (words)
#             if words in gene_sym:
#                 gs.write(gene_sym[words]+'\t'+'\t'.join(lines[2:])+'\n')
#     gs.close()

### FOR LIMMA
# gs = open("../results/Limma/Limma_genesymb.tsv", 'w')
# with open("../results/Limma/Limma.tsv", 'r') as l:
#     l = l.readlines()
#     gs.write("\"gene_symbol\""+'\t'+l[0])
#     for lines in l:
#         lines = lines.split()
#
#         ensg = lines[0].replace("\"","")
#         # print (ensg)
#         if ensg in gene_sym:
#             gs.write(gene_sym[ensg]+'\t'+'\t'.join(lines[1:])+'\n')
# gs.close()

print ("Done!")
