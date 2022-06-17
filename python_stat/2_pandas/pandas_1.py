import pandas as pd
""" 시험범위: 넘파이, 판다스, 시각화 """

year = [str(i) for i in range(2011, 2018)]
ktx_data = pd.DataFrame({'경부': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
                         '호남': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
                         '경전': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
                         '전라': [309, 1771, 1954, 2244, 3146, 3945, 5766],
                         '동해': [None, None, None, None, 2395, 3786, 6667]},
                        index = year)
df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]})
df2 = pd.DataFrame({'Class1': [87, 89],
                    'Class2': [89, 90]})
df3 = pd.DataFrame({'Class3': [96, 83, 77, 84]})
dfA = pd.DataFrame({'A': [32, 74, 90, 15], 'B': [62, 10, 25, 46]})
dfB = pd.DataFrame({'A': [51, 32, 90, 20], 'B':[10, 25, 46, 35]})
# DataFrame 활용: 데이터 선택
ktx_data.index
ktx_data.columns
ktx_data.values
ktx_data.head(3)
ktx_data.tail(3)
ktx_data[1:3]
ktx_data.loc['2011'] # loc[index]
ktx_data.iloc[1]
ktx_data['경부'] # 그냥[columns]
ktx_data.T
ktx_data['호남'].tolist()

# DataFrame 활용: 데이터 통합
df1.append(df2, ignore_index=True)
df1.join(df3)
dfA.merge(dfB, how='inner', on='A')
dfA.merge(dfB, how='outer', on='A')
dfA.merge(dfB, how='left', on='B')
dfA.merge(dfB, how='right', on='B')

# 데이터 생성, 읽기
%%writefile "C:\Users\dlsfu\Desktop\python_stat\sea_rain2.csv"
연도,동해,남해,서해,전체
2016,17.3,17.4,18.5,20.8,19.2
2017,17.7,16.5,17.8,21.9,20.7
2018,19.2,18.7,18.4,16.1,18.5
2019,18.4,18.9,19.2,12.8,20.1
2020,19.6,15.6,20.7,22.7,25.9

pd.read_csv(r"C:\Users\dlsfu\Desktop\python_stat\sea_rain2.csv", 
            sep=",", index_col="연도")
