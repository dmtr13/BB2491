directory <- "../data/processed_raw_counts.tsv"
data <- read.table(directory, sep='\t', header=TRUE, row.names=1)
N <- nrow(data)

library("limma")
library("edgeR")

h_len <- length(data[,grepl("H",names(data))])
s_len <- length(data[,grepl("S",names(data))])
n_len <- length(data[,grepl("N",names(data))])
c_len <- length(data[,grepl("C",names(data))])
s <- factor(c(rep("H", h_len), rep("S", s_len), rep("N", n_len), rep("C", c_len)))
design <- model.matrix(~0+s)
colnames(design) <- levels(s)
fit <- lmFit(data, design)
contr <- makeContrasts(H-S, S-N, N-C, levels = design)
fit.contr <- eBayes(contrasts.fit(fit,contr))

len <- nrow(data)
HS <- data.frame(topTable(fit.contr, coef = 1, number=len))
SN <- data.frame(topTable(fit.contr, coef = 2, number=len))
NC <- data.frame(topTable(fit.contr, coef = 3, number=len))

write.table(HS, file="../results/HS_limma.tsv", sep='\t')
write.table(SN, file="../results/SN_limma.tsv", sep='\t')
write.table(NC, file="../results/NC_limma.tsv", sep='\t')
###ARCHIVED 2018.01.15
