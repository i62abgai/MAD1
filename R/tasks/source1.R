# ------- 1. example ---------------------------

a <- 1:10   # integers from 1 to 10 (vector)
b <- letters[1:5]  # vector of characters (object letters is built-in vector of 26 characters of English alphabet)
save(a, b, file="./mydatafile.Rdata")
rm(a, b)  # remove (delete) 
load("./mydatafile.Rdata")
print(a)  # or simply type a
print(b)

# ------- 2. example ---------------------------
rm(list = ls())
var1 <- sample(5)  # integers from 1 to 5 insome random permutation
var2 <- var1 / 10
var3 <- c("R", "and", "Data Mining", "Examples", "Case Studies")
df1 <- data.frame(var1, var2, var3)  # to create data frame
names(df1) <- c("Var.Int", "Var.Num", "Var.Char")  # to set columns' name (attributes' names)
write.csv(df1, "./mydatafile3.csv", row.names = FALSE)
df2 <- read.csv("./mydatafile3.csv")
print(df2) 
df2$Var.Int # to print valuesof Var.Int atribute

# ------- 3. example ---------------------------

df<-as.data.frame(read.csv("./weather_nominal.csv", header = T, sep = ";")) # to read csv file, 
# it is possible to set the separator and to decide if the names of attributes are to be read
names(df) # attributes' names (columns' names)

df$Outlook # values of Outlook attribute
df$Temperature
df$Humidity
df$Windy
df$Play

dim(df) # dimension of data frame
str(df) # structure of data frame
attributes(df) # attributes
head(df, 5) # first 5 rows of data frames
tail(df, 2) # last tvo rows of data frames
summary(df) # returns the frequency of all values of the given attribute (for numeric even median, mean, ....)

t<-table(df$Outlook) # to create tabular results of categorical variables
t
barplot(t)
pie(t)
