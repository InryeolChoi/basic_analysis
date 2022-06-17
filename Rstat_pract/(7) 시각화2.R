# 파이, 박스플롯, 줄기/잎, 커브
sales = seq(10, 30, 5)
region = c("제주", "대구", "대전", "경기", "서울")
pie(x=sales, labels=region)
pie(x=sales, labels=region, clockwise=T)
pie(x=sales, labels=region, col=c("red", "orange", "yellow", "green", "blue"))

iris
boxplot(Sepal.Length~Species, data=iris)
boxplot(Sepal.Length~Species, data=iris, col=c("red", "orange", "yellow", "green", "blue"))
boxplot(Sepal.Length~Species, data=iris, width=c(1,2,3))
boxplot(Sepal.Length~Species, data=iris, horizontal=T)

sam = sample(x=1:100, size=50, replace=T); sam
stem(sam)
stem(sam, scale=2)
stem(sam, scale=0.5)

curve(expr=x^2)
curve(expr=x^2, from=-2, to=2)
curve(expr=x^2, from=-2, to=2, type="l")
curve(expr=x^2, from=-2, to=2, col="blue")

# 저수준 함수: 완성된 그래프에 직선, 범례, 제목 추가
x = c(1:5)
y = c(1:5)
p = c(2,1,2,3,4)
par(mfrow=c(1,3))
plot(x,y,type="n")
points(p, pch=1, cex=1)
plot(x,y,type="n")
points(p, pch=2, cex=2)
plot(x,y,type="n")
points(p, pch=3, cex=3)

x = c(1:5)
y = c(1:5)
p = c(2, 1, 2, 3, 4)
plot(x, y, type="n")

plot(1:10)                                                   
abline(h=5)                                     
rect(1,6,4,9)                                      
arrows(1,1,4,4)               
text(8,9,"ABCD")                               
title("main", "sub")                           
legend(8,3, lty=1:3, c("P","Q","R"))           

x <- c(1:5)
y <- c(1:5)
p <- c(2, 1, 2, 3, 4)
par(mfrow=c(1,3))
plot(x,y, type="n")
points(p, pch=1, cex=1)
plot(x,y, type="n")
points(p, pch=2, cex=2)
plot(x,y, type="n")
points(p, pch=3, cex=3)

x <- c(1:5) ; y <- c(1:5)
plot(x, y, type="n")
lines(c(2,4),c(1,1), lty=1)
lines(c(2,4),c(2,2), lty=2)
lines(c(2,4),c(3,3), lty=3)
lines(c(2,4),c(4,4), lty=4)
lines(c(2,4),c(5,5), lty=5)

x <- c(1:5)
y <- c(1:5)
plot(x, y, type="n")
text(3,3, "text in plot",adj=0.5,cex=1.5)
text(3,3, "text in plot",col="red", adj=1)
text(3,3, "text in plot", col="blue",adj=0)

x <- c(1:10)
y <- c(1:10)
plot(x, y, type="n",xlim=c(-5,5))
abline(h=2, v=0, lty=3)
abline(a=2, b=4,lty=2)

x = c(1:10)
y = c(1:10)
plot(x, y, type="n", xlim=c(-5,5))
legend("center", legend=c("x","y"), pch=c(1,2), title="center")
legend("bottom", legend=c("x","y"), lty=c(1,2), title="bottom")
legend("left", legend=c("x","y"), pch=c(1,2), title="left")
legend("right", legend=c("x","y"), pch=c(1,2), col=c(1,2), title="right")

#그래프의 중첩
plot(sin, -pi, pi, xlab="", ylab="", lty=2)
par(new=T)
plot(cos, -pi, pi, xlab="x", ylab="y")
par(new=T)
plot(sin, -2*pi, 2*pi, xlab="X", ylab="Y",col="red")


#그래프의 저장
x <- c(1:5)
y <- c(1:5)
plot(x,y,type="n")
getwd()
setwd("C:/Users/dlsfu/Desktop/Rstat_pract/data")
savePlot(filename="Rplot", type="png")




