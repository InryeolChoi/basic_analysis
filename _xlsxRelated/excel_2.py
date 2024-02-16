import glob
import pandas as pd

#%% glob()를 이용한 정규 표현식
# 3가지 엑셀 파일을 하나로 합치기
excel_lists = glob.glob(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_*사원.xlsx")
total_data = pd.DataFrame()

for f in excel_lists:
    df = pd.read_excel(f)
    total_data = total_data.append(df, ignore_index=True)
    
total_data

# 통합결과를 엑셀파일로
f_name = r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_통합.xlsx"
writer = pd.ExcelWriter(f_name, engine='xlsxwriter')
total_data.to_excel(writer, index=False, sheet_name = '담당자별_판매량_통합')
writer.save()

glob.glob(f_name)

#%% 데이터 다루기
# 1단계
df = pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_Andy사원.xlsx")
df1 = df; df1

# 2단계
df1.loc[2, '4분기'] = 0
df1

# 3단계: 3행 추가
label = ['제품명', '담당자', '지역', '1분기', '2분기', '3분기', '4분기']
value = ['벨트', 'A', '가', 100, 150, 200, 250]
for i in range(len(label)):
    df1.loc[3, label[i]] = value[i]
df1

# 4단계
df1['담당자'] = 'Andy'
df1

# 5단계
f_name = r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_Andy사원2.xlsx"
writer2 = pd.ExcelWriter(f_name, engine='xlsxwriter')
df1.to_excel(writer2, index = False, sheet_name = '')
writer2.save()
glob.glob(f_name)


#%% 필터 기능
# 접근 1 (특정 열 값 이용 / isin() 이용)
df = pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\담당자별_판매량_통합.xlsx")
handbag1 = df [df['제품명'] == '핸드백']
handbag1

handbag2 = df[ df['제품명'].isin(['핸드백']) ]
handbag2

# 접근 2
df [ (df['제품명'] == '구두') | (df['제품명'] == '핸드백') ]
df [ df['제품명'].isin(['구두', '핸드백'])]

# 원하는 행 선택
df [ ( df['3분기'] >= 250 )]
df [ ( df['제품명'] == '핸드백') & ( df['3분기'] >= 350 ) ]


