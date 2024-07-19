import pandas as pd
import numpy as np
""" 시험범위: 넘파이, 판다스, 시각화 """

# 데이터 만들기: 1차원(series), 2차원(dataframe)
# 판다스의 데이터 = 각 원소들의 데이터 타입이 달라도 괜찮다.
s1 = pd.Series([10, 20, 30, 40, 50]); s1
s2 = pd.DataFrame([[1,2,3],[4,5,6]]); s2
s3 = pd.Series([10, 20, np.NaN]); s3

# Series 활용: 날짜, 딕셔너리 응용, 시간
date = ['2022-04-24', '2022-04-25', '2022-04-26', '2022-04-27']
s4 = pd.Series([30, 24, np.NaN, 50], index = date); s4
s5 = pd.Series({'국': 100, '수': 98, '영': 100}); s5

date2 = pd.date_range(start='2022-04-24', end='2022-04-27')
date3 = pd.date_range(start='2022-01-05', end='2022-10-10', periods = 6); date3
date4 = pd.date_range(start='2022-01-01', end='2022-12-12', freq = 'D'); date4
date4 = pd.date_range(start='2022-01-01', end='2022-12-30', freq = '2D'); date4
date4 = pd.date_range(start='2022-01-01', periods = 4, freq = 'W'); date4
date4 = pd.date_range(start='2022-01-01', periods = 4, freq = 'QS'); date4
# start, end, periods, freq 중 오직 3개 이하만 입력!

# DataFrame 활용: 리스트, 딕셔너리, 연산
d = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
name = ['A', 'B', 'C']
date5 = pd.date_range('2022-09-01', '2022-09-03')
pd.DataFrame(data = d, index = date5, columns=name)

name = [0,1,2]
df = pd.DataFrame({'0': [1,4,7], '1': [2,5,8], '2': [3,6,9]}, index=name)
df.index
df.values

df1 = pd.Series([10, 20, np.NaN])
df2 = pd.Series([np.NaN, 30, 50])
df1.add(df2)

year = [str(i) for i in range(2012, 2017)] 
df3 = pd.DataFrame({'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
                  '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
                  '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
                  '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]},
                  index = year)
df3
df3.mean(axis=0)
df3.mean(axis=1)
df3.describe()

