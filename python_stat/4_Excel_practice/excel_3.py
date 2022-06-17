import pandas as pd

#%% 특정 데이터 선택
# step 1
df = pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_통합.xlsx")
df

df [ ( df["제품명"] == "핸드백" ) & ( df['3분기'] >= 350 ) ]

# step 2 
df2 = pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_Andy사원.xlsx")
df2 = pd.DataFrame(df2)
df2

df2[['제품명','1분기', '2분기', '3분기', '4분기']]
df2.iloc[:, [0,3,4,5,6]]
df2.iloc[[0,2], :]


#%% 데이터 계산
# 행 데이터 계산: part.1
df3 = pd.DataFrame( pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_통합.xlsx") ); df3
handbag = df3[df3['제품명'] == '핸드백']
handbag

x = handbag.sum(axis=1)
handbag_sum = pd.DataFrame(x, columns=['연간판매량'])
handbag_sum

handbag = handbag.join(handbag_sum)
handbag

handbag.sort_values(by='연간판매량', ascending=False)
handbag

# 열 데이터 계산: part.2
handbag_sum = pd.DataFrame(handbag.sum(), columns = ['합계']); handbag_sum
handbag_total = handbag.append(handbag_sum.T);
handbag_total

handbag_total.loc['합계', '제품명'] = '핸드백'
handbag_total.loc['합계', '담당자'] = '전체'
handbag_total.loc['합계', '지역'] = '전체'
handbag_total

