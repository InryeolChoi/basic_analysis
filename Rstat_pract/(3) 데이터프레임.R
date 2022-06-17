# 데이터프레임
num = c(1:5); num
cha = c("가","나","다","라","마"); cha
log1 = c(T,F,T,TRUE,FALSE); log1
df_1 = data.frame(num, cha, log1); df_1

str(df_1)

df_2 = data.frame(num, cha, log1, alp=c("a","b","c","d","e"))
df_2

dfdf = data.frame(col1=1:2, col2=3:4); dfdf
dfdf = data.frame(col1=1:2, col2=3:4, row.names=c("가","나")); dfdf

names(dfdf)
names(dfdf) = c("사과", "배")
dfdf

df_2[2,]
df_2[,2]
df_2[-1,]
df_2$cha
df_2[,-c(2,4)]

df_2$alp = NULL
df_2


df_2 = data.frame(num, cha, log1, alp=c("a","b","c","d","e"))
df_2[["cha"]]
df_2[,"cha"]
df_2[c("cha","alp")]
df_2[,c("cha","alp")]

# iris 데이터 이용
head(iris)
tail(iris)
mean(iris$Sepal.Length)
sd(iris$Sepal.Length)
hist(iris$Sepal.Length)

which(iris$Sepal.Length > 6)
iris$Sepal.Length > 6
iris$Sepal.Length[c(51,52,53,54)]
iris[which(iris$Sepal.Length > 6),"Species"]
iris[which(iris$Sepal.Length <= 6 & iris$Sepal.Width == 3),]

subset(iris, select=Species, subset=(iris$Sepal.Length > 6))
iris[which(iris$Sepal.Length > 7), c("Sepal.Length", "Species")]
subset(iris, select=c("Petal.Length", "Species"), subset=(iris$Petal.Length <= 3.5 & iris$Species!="setosa") )
subset(iris, select=c("Petal.Length", "Species"), subset=(iris$Petal.Length < 5.5 & iris$Species %in% c("versicolor", "virginica")))

# 변수추가/수정
df_p = data.frame(x1=c(1,2,3,4), x2=c(2,4,6,8)); df_p
df_p
df_p[,4] = df_p[,1] + df_p[,3]
df_p

df_p = transform(df_p, x3=c(0,0,0,0)); df_p
df_p = transform(df_p, x5=x2+x3, meanx12=(x1+x2)/2); df_p

df_p$ten[df_p$V4<10] = "down"
df_p$ten[df_p$V4>10] = "up"
df_p

class(df_p$ten)
df_p$ten = factor(df_p$ten)
class(df_p$ten)
str(df_p$ten)

# 결합1: rbind, cbind
fruit = c("apple", "berry", "cherry"); weight = c(30,5,7)
df_r = data.frame(fruit, weight); df_r

fruit = c("orange", "mango", "banana"); weight = c(40,50,60)
df_o = data.frame(fruit, weight); df_o

rbind(df_r, df_o)
cbind(df_r, df_o)

# 결합2: merge()
df_1 = data.frame(name=c("철수","영희","민수"), mid=c(45,74,23)); df_1
df_2 = data.frame(name=c("철수","수진","서연","민수"), mid=c(63,98,45,50)); df_2
df_3 = data.frame(name=c("수진","철수","준서","민수"), quiz=c(10,5,3,8)); df_3

merge(df_1, df_2, by="name") # inner join
merge(df_1, df_2, by="name", all=T) # outer join
merge(df_1, df_2, by="name", all.x=T) # left outer
merge(df_1, df_2, by="name", all.y=T) # right outer

score1 = read.table("C:/Users/dlsfu/Desktop/Rstat_pract/data/score1.txt", sep=";")
score1
score2 = read.table("C:/Users/dlsfu/Desktop/Rstat_pract/data/score2.csv",sep=" ")
score2

colnames(score1)
score = merge(score1, score2, by=c("name","age"),all=T);score
write.table = (score, "C:/Users/dlsfu/Desktop/Rstat_pract/data/score3.txt", sep="_")
write.table = (score, "C:/Users/dlsfu/Desktop/Rstat_pract/data/score3.txt", sep="_", quote=F)
write.csv = (score, "C:/Users/dlsfu/Desktop/Rstat_pract/data/score4.csv")
write.csv = (score, "C:/Users/dlsfu/Desktop/Rstat_pract/data/score4.csv", row.names=F)


# cars93
library("MASS")
help(Cars93)
str(Cars93)

summary(Cars93)
AA = c(1,2,NA,NaN,45); AA
anyNA(AA)
is.na(AA)

A = data.frame(AA); A
na.omit(A)
Car = Cars93
nrow(Car)
colSums(is.na(Car))

x = Car$Luggage.room
Car[which(is.na(x)), c("Model", "Rear.seat.room", "Luggage.room")]
Car = na.omit(Car)
nrow(Car)

zp = (Car$Price - mean(Car$Price))/sd(Car$Price)
zp

attach(Car)
zp_1 = (Price - mean(Price))/sd(Price)
zp_1


zp_2 = with(Car, Price-mean(Price)/sd(Price)); zp_2

aggregate(Price~Manufacturer,Car,mean)
aggregate(EngineSize~Manufacturer+Type,Car,sum)

Car_p = Car[c(2,4,6)]; Car_p
apply(Car_p[2:4],,sd)

tapply(Car$Price, Car$Manufacturer, mean)
air_p = split(Car$Price, Car$AirBags); air_p
str(air_p)
mean(air_p[[1]])
sum(air_p[[2]])
sd(air_p[[3]])
