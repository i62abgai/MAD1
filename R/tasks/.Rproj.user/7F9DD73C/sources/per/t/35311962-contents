df<-read.csv("../iris.csv", header = T, sep = ";", dec = ".", stringsAsFactors=F)

# ------------- univariate analysis ------------------------

# but, variety will be a categorial variable for us 
df$variety <-factor(df$variety)
str(df) 
# table of frequencies
table(df$variety)
#  table of relative frequencies
table(df$variety)/length(df$variety)

pie(table(df$variety))
barplot(table(df$variety))

# mean
mean(df$sepal_length)
# total variance
var(df$sepal_length)
# standard deviation
sd(df$sepal_length)
# median
median(df$sepal_length)
range(df$sepal_length)
min(df$sepal_length)
max(df$sepal_length)

# table of frequencies
table(df$sepal_length)
#  table  of rel. frequencies
table(df$sepal_length)/length(df$sepal_length)

# histogram, takes it as a continuous variable
hist(df$sepal_length)
plot(density(df$sepal_length))  # probability density function

# I'd like to join it in one plot
hist(df$sepal_length, freq=F, col="grey")
lines(density(df$sepal_length), col="blue", lwd=2)

# finer binning (finer division of the x-axis interval)
hist(df$sepal_length, breaks = (max(df$sepal_length)-min(df$sepal_length))*5, probability = T, col="grey")
lines(density(df$sepal_length), col="blue", lwd=2)
# add normal distribution
curve(dnorm(x, mean=mean(df$sepal_length),sd=sd(df$sepal_length)), min(df$sepal_length), max(df$sepal_length), add=T, col="green")

## Install if missing
if (!require("fitdistrplus")) 
  install.packages("fitdistrplus")

library(fitdistrplus) 
# # empirical cumulative distribution function
plot(ecdf(df$sepal_length))

# using the plotdist() function from the fitdistrplus package
plotdist(df$sepal_length, histo = TRUE, demp = TRUE)

# can the sepal_length frequency be used as a discrete variable?
# use table()
fsl<-table(df$sepal_length)
# reltive frequency
prop.table(fsl)

plot(as.numeric(names(fsl)),as.numeric(fsl),xlab="hodnota", ylab="cetnost", main='hist sepal_length')
# the histogram or column chart is better
plot(fsl)
# or
barplot(fsl)

#  pmf, probabiltiy mass function
plot(prop.table(fsl))



#-----------------------------------------------------------------------------------------------
# we will make a matrix from the first two columns
# function cbind() 
dm<-cbind(df$sepal_length,df$Sepal.Width)
# or dm <-dist(df[,c("sepal_length","Sepal.Width")]
dm

# -------------------------------------------------

# Euclidean distance
dist(dm)

# we do not see much :-), so we will only count it for the first few instances
dm2<-head(dm)
dm2
dist(dm2)

min(dist(dm2))
max(dist(dm2))

# -------------------------------------------------

# cosine measure (similarity)
## Install if missing
if (!require("lsa")) 
  install.packages("lsa")
library(lsa) 

dm2 <- t(dm2) # transposed matrix, Why? test the cosine () function on an untransposed matrix
dm2
cosine(dm2)
min(cosine(dm2))
max(cosine(dm2))

