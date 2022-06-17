# За·Д

matrix(seq(1,9), nrow=3)
mat = matrix(c("a","b","c","d"), nrow=2);mat
dat = c(1,2,3,5,8,13,21,34,55,89,134,223)

array(dat,c(3,5))
a = c(1:5)
b = seq(2,10,2)
rbind(a,b)
cbind(a,b)

Dat = array(dat,c(3,5))
nrow(Dat)
x2 = matrix(x, byrow=T, ncol=3)
ncol(x2)
dim(x2)
Dat[1]
Dat[1,1] 
Dat[c(1,2),3]

A = matrix(1:16, byrow=T, nrow=4); A
B = matrix(1:16, nrow=4); B
C = A%*%B
q = matrix(seq(1,9), nrow=3)
t(q)
solve(q)
det(A)
diag(A)

rowSums(A)
colSums(B)

apply(A, 1, sum)
apply(A, 2, function(x){x^2 + 1})
rownames(A)=c("a","b","c","d")
colnames(A)=c("121","345","867","2345") 
A
dimnames(B)=list(c("a","b","c","d"), c("121","345","867","2345"))
B
