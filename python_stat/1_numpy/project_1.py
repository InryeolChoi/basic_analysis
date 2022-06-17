# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% array() 
import numpy as np

list1 = [i for i in range(1, 9)]
print(list1)
arr1 = np.array(list1)
print(arr1)

arr1.dtype

#%% 원소에 실수 및 정수 모두 포함
list2 = [0, 1, 2, 2.5, 3.5, 8, 19]
print(list2)
type(list2)

arr2 = np.array(list2)
print(arr2)
type(arr2)

arr2.dtype

#%% arange()

arr2 = np.arange(9)
print(arr2)
arr3 = np.arange(1, 9, 2)
print(arr3)
type(arr2)


np.arange(0, 10, 2)
np.arange(1, 10)
np.arange(1, 10, 2)

#%% 2차 배열
list4 = [[1,2,4],[2,3,5],[2,5,6]]
arr4 = np.array(list4)
print(arr4)
type(list4)
type(arr4)

#%% reshape()
arr2 = np.array([i for i in range(9)]).reshape(3,3)
print(arr2)
arr3 = np.arange(12).reshape(4,3)
print(arr3)

#%% 산술 연산
arr2+200
arr2-100
arr2//100
arr2/2


#%% 
A = np.array(['1.3', '0.62', '2', '3.14', '3.141592'])
print(A)
A.dtype

sung1 = np.array([1,2,3])
print(sung1.dtype)

sung2 = np.array(["1","3","5"])
print(sung2.dtype)

sung3 = np.array([1.1, 2.2, 3.3])
print(sung3.dtype)

#%% astype 데이터형식 변환
str_a1 = np.array(['1.4', '0.123', '5.123', '9', '8'])
str_a1.dtype
num_a1 = str_a1.astype(float)
print(num_a1)
num_a2 = num_a1.astype(int)
print(num_a2)

# 간결하게
str_a1.astype(float).astype(int)

str_a2 = np.array(['1', '2', '3', '4', '5'])
str_a2.dtype
num_a2 = str_a2.astype(int)
num_a2
