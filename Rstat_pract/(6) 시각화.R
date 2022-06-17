# 산점도: plot(), pairs()
# 막대: barplot()
# 히스토그램: hist()
# 박스플롯: boxplot()
# 함수 그래프: curve()


cars
plot(cars$speed, cars$dist)
plot(cars$speed, cars$dist, main="speed & distance")
plot(cars$speed, cars$dist, main="speed & distance",
xlab='speed', ylab='distance')

BOD
x = BOD$Time
y = BOD$demand
par(mfrow=c(2,3))
plot(x, y, type="l", Ity=1)
plot(x, y, type="l", Ity=2)
plot(x, y, type="l", Ity=3)
plot(x, y, type="l", Ity=4)
plot(x, y, type="l", Ity=5)
plot(x, y, type="l", Ity=6)

pairs(iris[1:4])
pairs(iris[1:4], lower.panel=NULL)
pairs(iris[1:4], upper.panel=NULL)


fruits_count = c(4,3,5,8)
names(fruits_count) = c("A", "T", "G", "M"); fruits_count
barplot(height=fruits_count)
barplot(height=fruits_count, width=c(0,5,1,1,5,2))
barplot(height=fruits_count, space=2)
barplot(height=fruits_count, col=c("lightblue", "mistyrose", "lightcyan", "lavender"))
barplot(height=c(4,3,5,8), names.arg=c("A", "T", "G", "M"))
barplot(height=fruits_count, horiz=TRUE)


# 히스토그램
class_height = c(172, 184, 198, 175, 182, 190)
hist(x = class_height)
hist(x = class_height, breaks=c(160, 170, 180, 190))
hist(x = class_height, probabilty=TRUE)


x = rnorm(1000)
hist(x)
hist(x, prob=T)
lines(density(x))

x = rnorm(10000)
hist(x, breaks="Sturges")
hist(x, breaks="Scott")
hist(x, breaks="Freedman-Diaconis")


x = rnorm(100, 3, 2); x = round(x,2)
hist(x, nclass=10)
hist(x, nclass=30)

hist(x, axes=T, main="axes=T")
hist(x, axes=F, main="axes=F")