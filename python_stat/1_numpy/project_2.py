# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:11:17 2022

@author: Peter
"""

#%% 메소드
import numpy as np

# linspace(): 원소의 타입은 float
np.linspace(1, 10, 10)
np.linspace(1, 10, 6)

# linspace(): 벡터 생성
np.pi
np.linspace(0, np.pi, 20)

# ones(): 1로 채워진 행렬
np.ones(5)
np.ones((3,3))

# zeros(): 영행렬
np.zeros(4)
np.zeros((3,3))

# in으로 값 확인
arr1 = np.arange(9)
print(arr1)
arr2 = arr1.reshape(3,3)
print(arr2)

1 in arr1
9 in arr2

# 위치값 찾기
np.where(arr1==1)
np.where(arr2==3)

# eye(): 대각행렬
np.eye(5)

# diag : 대각행렬
np.diag([i for i in range(1, 6)])
np.diag([i for i in range(10, 15)])

#%% 통계를 위한 연산
arr3 = np.arange(5)
print(arr3)

arr3.sum()
a = [arr3.sum(), arr3.mean()]
print(a)
[arr3.std(), arr3.var()]
[arr3.min(), arr3.max()]
arr3.cumsum() # 배열의 누적합
arr3.cumprod() # 배열의 누적곱

#%% 행렬연산 메서드
A = np.array([i for i in range(0, 4)]).reshape(2,2)
A

B = np.array([i for i in range(3, -1, -1)]).reshape(2,2)
B

A.dot(B) # 행렬 곱 case 1
A
B
B.dot(A) # 행렬 곱 case 2

np.transpose(A) # 행렬 A의 전치행렬 case 1 
A
A.transpose() # 행렬 A의 전치행렬 case 2

np.linalg.inv(A) # 행렬 A의 역행렬
np.linalg.det(A) # 행렬 A의 행렬식

#%% 배열의 인덱싱/슬라이싱
# 1차원
a1 = np.array([i for i in range(0, 60, 10)])
a1

a1[0]
a1[4]

a1[[1,3,4]]

# 2차원
a2 = np.arange(10, 100, 10).reshape(3, 3)
a2

a2[0,2] # 특정 행, 열 위치의 원소값

a2[2,2] = 95 # 특정 행, 열 위치의 원소값 변경
a2

a2[1] # 특정 행 전체를 불러들이기

# example
# case1
arr4 = np.arange(1, 11).reshape(2, 5)
arr4

arr4.dtype
arr4[1,2]
arr4[0,:]
arr4[:,0]

print(arr4.sum(axis=0))
print(arr4.sum(axis=1))
print(arr4[arr4 > 3])

print(arr4[ (arr4 % 2) == 0] )
print(arr4[ (arr4 % 2) == 1] )

# 슬라이싱
# 1차원
b1 = np.array([i for i in range(0, 60, 10)])
print(b1)
b1[1:4]
b1[-5:-2]
b1[:3] # 시작위치 지정 x
b1[2:] # 끝 위치 지정 x

b1[2:5] = np.array([25, 35, 45])
print(b1)

b1[3:6] = 60
print(b1)

# 2차원
b2 = np.arange(10, 100, 10).reshape(3, 3)
print(b2)
b2[1]
b2[0:2]
b2[1][0:2]
b2[1:3, 1:3]

b2[:3, 1:]
b2[0:2, 1:3]
b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
b2
