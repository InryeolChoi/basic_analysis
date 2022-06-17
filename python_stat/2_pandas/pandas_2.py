import pandas as pd
"""시험범위: 넘파이, 판다스, 시각화"""

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

# index 이름 넣기
sold = pd.DataFrame({'판매가격': [2000, 3000, 5000, 10000],
                     '판매량': [32, 53, 40, 25]},
                    index = ['P' + str(i) for i in range(1001, 1005)])
sold.index.name = '제품번호'
sold
a = r"C:\Users\dlsfu\Desktop\python_stat\sold.csv"
sold.to_csv(a, sep=" ", encoding="cp949")
!type "C:\Users\dlsfu\Desktop\python_stat\sold.csv"

