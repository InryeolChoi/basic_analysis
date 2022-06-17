import pandas as pd

#%% 엑셀 불러오기
df = pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\학생시험성적.xlsx")
df

pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\학생시험성적.xlsx", sheet_name = 1)

pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\학생시험성적.xlsx", sheet_name = "2차시험")

pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\학생시험성적.xlsx", sheet_name = "2차시험", index_col = 0)

pd.read_excel(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\학생시험성적.xlsx", sheet_name = "2차시험", index_col = '학생')

#%% 엑셀 쓰기
stu = [chr(i) for i in range(65, 71)]
kor = [80,90,95,70,75,85]
eng = [90,95,70,85,90,95]
math = [85,95,75,80,85,100]
df1 = pd.DataFrame({'학생' : stu, '국어': kor, '영어': eng, '수학': math})
df1

excel_writer = pd.ExcelWriter(r"C:\Users\USER\Desktop\python_stat\엑셀\학생시험성적2.xlsx", engine='xlsxwriter')
df1.to_excel(excel_writer, index = False, sheet_name = '중간고사')
excel_writer.save()

kor2 = [80,95,75,80,85,100]
eng2 = [80,90,95,70,75,85]
math2 = [90,95,70,85,90,95]
df2 = pd.DataFrame({'학생' : stu, '국어': kor2, '영어': eng2, '수학': math2})
df2

excel_writer2 = pd.ExcelWriter(r"C:\Users\USER\Desktop\python_stat\엑셀\학생시험성적3.xlsx", engine='xlsxwriter')
df1.to_excel(excel_writer2, index = False, sheet_name = '중간고사')
df2.to_excel(excel_writer2, index = False, sheet_name = '기말고사')
excel_writer2.save()

#%% 파일 읽기

excel_data_files = [r"C:\Users\USER\Desktop\python_stat\엑셀\담당자별_판매량_Andy사원.xlsx",
                    r"C:\Users\USER\Desktop\python_stat\엑셀\담당자별_판매량_Becky사원.xlsx",
                    r"C:\Users\USER\Desktop\python_stat\엑셀\담당자별_판매량_Chris사원.xlsx"]

total_data = pd.DataFrame()
for f in excel_data_files:
    df = pd.read_excel(f)
    total_data = total_data.append(df)
total_data

total_data2 = pd.DataFrame()
for f in excel_data_files:
    df = pd.read_excel(f)
    total_data2 = total_data.append(df, ignore_index=True)
total_data2
