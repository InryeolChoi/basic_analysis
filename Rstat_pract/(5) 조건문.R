# 조건문
# function()
new = function(x){print(x^2)}
new(3)

mypower02 = function(x,y){
x^y}
mypower02(3,4)

# if문
myindex = function(x){
if(x>1){print(1)}
else{print(0)}
}

myindex(10)

# for문
for(i in 1:5){
print(i)
}

myeven = function(x){
sum = 0
for(i in 1:x){
if(i%%2==0){sum = sum + i}
}
print(sum)
}

myeven(10)

#while문
fib = 0
last_fib = 1
while(last_fib<300){
fib = c(fib, last_fib)
last_fib = fib[length(fib)-1]+fib[length(fib)]
}
fib