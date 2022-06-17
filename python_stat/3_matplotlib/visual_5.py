import pandas as pd
import matplotlib.pyplot as plt

#%% 한글 글꼴 설정
plt.rcParams['font.family']
import matplotlib.font_manager as fm

font_list = fm.get_fontconfig_fonts()
font_names = [fm.FontProperties(fname=fname).get_name() for fname in font_list]

f = open(r"C:\Users\USER\Desktop\python_stat\my_font_list.txt", "w")
for font_name in font_names:f.write(font_name + "/n")
f.close()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

#%% 1차원 데이터 >> 그래프
s1 = pd.Series([i for i in range(1, 11)])
s1

s1.plot()
plt.show()

s2 = pd.Series([i for i in range(1, 11)], index = pd.date_range('2019-01-01', periods=10))
s2.plot(grid=True)

s3 = pd.read_csv(r"C:\Users\USER\Downloads\sea_rain1_space.txt", sep = " ", index_col = "연도")
s3


#%% 2차원 데이터 >> 그래프
rain_plot = s3.plot(grid = True, style = ['r--*', 'g-o', 'b:x', 'm-.p'])
rain_plot.set_xlabel("연도")
rain_plot.set_ylabel("강수", rotation = 'horizontal')
rain_plot.set_title("연간 강수량")
plt.show()

year = [i for i in range(2006, 2018, 2)]
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2]
table = {'연도': year, '주거면적': area}
df_area = pd.DataFrame(table, columns = ['연도', '주거면적'])
df_area

df_area.plot(x = '연도', y = '주거면적', grid = True, title = '1인당 주거면적')
plt.show()

df_grade = pd.DataFrame({'student' : [5,14,12,3]}, index=['A','B','C','D'])
df_grade

grade_bar = df_grade.plot.bar(grid = True)
grade_bar.set_xlabel("학점")
grade_bar.set_ylabel("학생수")
grade_bar.set_title("학점별 학생 수 막대 그래프")
grade_bar.set_ylim(0, 20)
grade_bar.set_title("학점별 학생 수 막대 그래프")

fruit = pd.Series([7,6,3,2,2], name = '선택한 학생 수', index=['사과','바나나','딸기','오렌지','포도'])
fruit.plot.pie()

scores = [76, 75, 100, 84, 99, 86, 85, 92, 93, 91, 80]
df_math = pd.DataFrame({'student': scores}); df_math
df_math.plot.hist(grid = True, bins = 8)
df_math.set_xlabel("학점")
df_math.set_ylabel("학생수")
df_math.set_title("학점별 학생 수 막대 그래프")

temp = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
ic = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
df_summer = pd.DataFrame({'기온': temp, '아이스크림 판매량': ic})
df_summer.plot.scatter(x = '기온', y ='아이스크림 판매량', grid=True,
                       title='최고기온과 아이스크림 판매량')
plt.show()
df_summer['아이스크림 판매량']
df_summer['기온']
df_summer['기온'].describe()


