#!/PUBLIC/software/HW/R/R-3.3.3/bin/Rscript
library(argparser)
library(reshape2)
library(ggplot2)

argv <- arg_parser("")
argv <- add_argument(argv,"--fpkm_sample", help="")
argv <- add_argument(argv,"--group_file", help="")
argv <- add_argument(argv,"--root_dir", help="")
argv <- parse_args(argv)

fpkm_sample <- argv$fpkm_sample
group_file <- argv$group_file
root_dir <- argv$root_dir

out_dir <- paste(root_dir,"/correlation",sep="")
system(paste("mkdir ",out_dir,sep=""))
#============================== read files ==============================

fpkm_sample <- read.delim(fpkm_sample,header=TRUE,row.names=1)
group_file <- read.delim(group_file,header=TRUE,row.names=1)

#============================== corr_sample ==============================

fpkm_log <- log(fpkm_sample+1,10)
sample_num <- ncol(fpkm_sample)
#sample numbers
corr_matrix <- matrix(1,sample_num,sample_num)
#create matrix (sample_num * sample_num)
for (i in 1:(sample_num-1)){
        for (j in (i+1):sample_num){
        #traverse all comparison
                fpkm_tem = data.frame(fpkm_log[,c(i,j)])
                #two samples' fpkm
                loc <- max(fpkm_tem[,2])
                model <- coef(lm(fpkm_tem[[2]]~fpkm_tem[[1]],data=fpkm_tem))
                intercept_val <- as.numeric(model)[1]
                slope_val <- as.numeric(model)[2]
                R2 <- round((cor(fpkm_tem[,1],fpkm_tem[,2],method="pearson"))^2,3)
                corr_matrix[i,j]=R2
                corr_matrix[j,i]=R2
                a<-group_file[colnames(fpkm_log)[i],]
                b<-group_file[colnames(fpkm_log)[j],]
                if(a != b && nrow(group_file) > 4){
                        next;
                }
                y1=loc
                p <- ggplot(fpkm_tem,aes_string(x=colnames(fpkm_tem)[1],y=colnames(fpkm_tem)[2]))+
                        geom_point(size=1.2,alpha=I(1/3),colour="#4876FF")+
                        geom_abline(intercept=intercept_val,slope=slope_val,linetype=2,colour="#FF7F50")+
                        geom_rug(size=0.5,alpha=0.01,colour="#4876FF")+
                        labs(title=paste(colnames(fpkm_log)[i]," vs ",colnames(fpkm_log)[j]))+
                        xlab(paste("log10(FPKM+1),"," (",colnames(fpkm_log)[i],")"))+
                        ylab(paste("log10(FPKM+1),"," (",colnames(fpkm_log)[j],")"))+
                        annotate("text",x=0.4,y=y1, label=paste("R^2==",R2),parse=TRUE)+
                        theme(panel.background = element_rect(fill="transparent",colour =NA))+
                        theme(panel.grid.minor = element_blank())+
                        theme(panel.grid.major = element_blank())+
                        theme(plot.background = element_rect(fill="transparent",colour =NA))+
                        theme(axis.line=element_line())+
                        theme(plot.title = element_text(hjust = 0.5))

                fpdf=paste(out_dir,'/',colnames(fpkm_log)[i],'_vs_',colnames(fpkm_log)[j],'.scatter.pdf',sep='')
                fpng=paste(out_dir,'/',colnames(fpkm_log)[i],'_vs_',colnames(fpkm_log)[j],'.scatter.png',sep='')
                ggsave(filename=fpdf, plot=p, height=6, width=6)
                ggsave(filename=fpng,type="cairo-png", plot=p, height=6, width=6)
        }
}

#============================== cor_all ==============================

corr_matrix <- data.frame(corr_matrix)

colnames(corr_matrix) <- colnames(fpkm_log)
corr_matrix$coefficient <- colnames(fpkm_log)

corr_matrix <- corr_matrix[,c(sample_num+1,1:sample_num)]
names(corr_matrix)[1] <- "R^2"
ft=paste(out_dir,'/cor_pearson.xls',sep='')
write.table(corr_matrix,file=ft,quote=F,row.name=F, sep="\t")

if(sample_num<5){
	size_number=5
}else if(sample_num<10){
	size_number=4
}else if(sample_num<15){
	size_number=3
}else if(sample_num<18){
	size_number=2
}else{
	size_number=1.5
}

heat <- corr_matrix
order <- heat[,1]
order <- as.vector(as.character(order))
df <- melt(heat)
colnames(df) <- c("sample1","sample2","correlation")

p <- ggplot(df,aes(sample1,sample2,label=correlation))+
	geom_tile(aes(fill = correlation),colour="white") +
	scale_fill_gradient(name=expression(R^2),low="white",high="#4876FF")+
	theme(panel.background = element_rect(fill='white', colour='white')) +
	theme(plot.title = element_text(hjust = 0.5))+
	labs(x="",y="", title="Pearson correlation between samples")+
	theme(legend.position="right",axis.text.x=element_text(angle=45,vjust=1,hjust=1))+coord_fixed()+
	geom_text(size=size_number)+xlim(order)+ylim(order)

ggsave(filename=paste(out_dir,'/cor_pearson.pdf',sep=''),plot=p, height=max(6,round(nrow(group_file)/3)), width=max(6,round(nrow(group_file)/3)))
ggsave(filename=paste(out_dir,'/cor_pearson.png',sep=''),type="cairo-png", plot=p, height=max(6,round(nrow(group_file)/3)), width=max(6,round(nrow(group_file)/3)))

