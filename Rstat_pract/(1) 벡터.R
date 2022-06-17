# 벡터
# 벡터1 : 수치형
c(1,2,3)
1:10
rep(2,5)
seq(70,100,10)

vec = c("1","2","3","4","5")
vec[1]
vec[-1]
vec[vec<4]
names[vec] = c("se","gy","gn","Jb","jj")
vec["se"]
vec = c(vec, 10)

vec = c(1,2,3,4,5)
vec2 = rep(10, 5)
vec ^ vec2

# 벡터2: 문자형
word = "learning"; word
nchar(word)

word2 = c("R","Excel","python")
paste(word, word2)
paste(word, word2, collapse=" ")
paste(word, word2, sep=",")

substr("statistical approach", 6, 10)
berry = c("blueberry", "cranberry")
substr(berry,5,9)
substr(berry,c(1,5),c(4,9))

strsplit("statistical approach", split=" ")
x = c("statistical approach", "mathematical approach")
sub("approach", "mix", x)

y = c("a", "b", "c"); y
replace(y,1,"A"); y
append(y, "1.4", after=1); y
sort(y)
order(word)

# 요인
mat = matrix(c("a","b","c","d"), nrow=2);mat
mode(mat)
class(mat)

