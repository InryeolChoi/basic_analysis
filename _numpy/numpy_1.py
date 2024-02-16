import numpy as np
""" 시험범위: 넘파이, 판다스, 시각화 """

# 넘파이: 1차원 데이터 만들기
arr1 = np.arange(0, 9); arr1
arr1.dtype # 데이터 타입 확인
arr1.astype(float) # 데이터 변환

np.linspace(1, 10, 10) # 등간격
np.ones(5)
np.zeros(5)

# 넘파이: 2차원 데이터 만들기
arr2 = arr1.reshape(3,3)
np.eye(5)
np.diag([i for i in range(1, 5)])
arr2.sum(); arr2.mean(); arr2.std(); arr2.var()
arr2.min(); arr2.max(); arr2.cumsum(); arr2.cumprod()

# 넘파이 : 행렬과 그 계산
arr3 = np.array([0, 5, 4, 2, 3, 12, 11, -1, 6])
arr3 = arr3.reshape(3,3)
arr2.dot(arr3)
arr3.transpose()
np.linalg.inv(arr3)
np.linalg.det(arr3)

# 넘파이: 데이터 검색, 인덱싱, 슬라이싱
np.where(arr1==2)
np.where(arr2==3)
arr1[[1,3,4]]
arr3[0,1]

arr4 = np.arange(1, 11).reshape(2, 5)
arr4[1, 2]
arr4[:3, 1:]
arr4.sum(axis = 0)