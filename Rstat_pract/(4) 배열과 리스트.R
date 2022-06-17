# 리스트와 배열
# 배열: 원소가 무조건 숫자
arr1 = array(1:9); arr1
arr2 = array(LETTERS, dim=c(2,13)); arr2
arr3 = array(month.abb, dim=c(2,2,3)); arr3

arr4 = array(c(1:12), dim=c(3,2,2), dimnames=list("행"=paste("행",c(1:3)), "열"=paste("열",c(1:2)), "열"=paste("열",c(1:2))))
arr4

dimnames(arr3) = list(paste("행",c(1,2)), paste("열",c(1,2)), paste("연",c(1,3)))
arr3

arr.x = array(1:18, dim=c(3,3,2));
arr.y = array(18:1, dim=c(3,3,2));
arr.x + arr.y
arr.x * arr.y
arr.x %*% arr.y

arr.x[1]
arr.y[2][1]
arr.x[ ,1, ]

arr.y[1,-1,]

# 리스트: 원소의 종류가 다양
obj = list()
obj[[1]] = 21
obj[[2]] = 23
obj[[3]] = F
obj[[4]] = seq(70, 100, 10)
obj

list.user1 = list("user1", 23, "M", c(80,85,90,95,100))
list.user1
list.user2 = list(ID="user1", age=23, gender="M", grade=c(80,85,90,95,100))
list.user2

obj[[1]] = NULL
obj
obj[[1]][3] = 86
obj[[2]] = matrix(1:12, 3, 4)
obj





