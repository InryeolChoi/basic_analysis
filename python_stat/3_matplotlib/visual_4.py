import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family']
import matplotlib.font_manager as plt_f

font_list = plt_f.get_fontconfig_fonts()
font_names = [plt_f.FontProperties(fname=fname).get_name() for fname in font_list]

f = open(r"C:\Users\USER\Desktop\python_stat\my_font_list.txt", "w")
for font_name in font_names:    f.write(font_name + "/n")
f.close()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

#%% 차트 그리기

""" 데이터의 종류
수치형 - 연속/이산; 히스토그램
범주형; 바차트, 파이차트
순위형, 명목형
"""

member_id = ['m_01', 'm_02', 'm_03', 'm_04']
before_ex = [27, 35, 40, 33]
after_ex = [30, 38, 42, 37]
c = ['red', 'green', 'blue', 'white']

my_string = "growth rate"
x = '\n'.join(my_string)
index = np.arange(len(member_id))

plt.bar(np.arange(len(member_id)), before_ex, tick_label = member_id,
        color = c, edgecolor = 'black')
plt.title("my data")
plt.xlabel("categories")
plt.ylabel(x, rotation = 0, loc='center')

plt.barh(index, before_ex, tick_label = member_id)

#%% 파이 그래프
student = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7,6,3,2,2]
plt.figure(figsize=(5,5)) # figure는 한번만 선언

plt.subplot(2, 2, 1)
plt.pie(result, labels=student, autopct="%.0f")

plt.subplot(2, 2, 2)
plt.pie(result, labels=student, autopct="%.1f")

plt.subplot(2, 2, 3)
plt.pie(result, labels=student, autopct="%.0f%%")

plt.subplot(2, 2, 4)
plt.pie(result, labels=student, autopct="%.1f%%")

plt.subplot(1,2,1)
plt.pie(result, labels=student, autopct="%.1f%%", counterclock=True)


#%% 파이 그래프 - 시계/반시계
plt.subplot(1,2,1)
plt.pie(result, labels=student, autopct="%.1f%%", counterclock=False)
plt.subplot(1,2,2)
plt.pie(result, labels=student, autopct="%.1f%%", counterclock=True)

#%% 파이 그래프 - explode(찢기), shadow(그림자)
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.pie(result, labels=student, autopct="%.1f%%", counterclock=False)

plt.subplot(1, 2, 2)
ev = [0.1, 0, 0, 0, 0]
plt.pie(result, labels=student, autopct="%.1f%%", explode=ev, shadow=True)

#%% 히스토그램; 데이터의 분포
np.random.seed(25)
math = np.random.randint(60, 100, size=25);
plt.hist(math, bins=8, color='pink')

np.random.seed(25)
math = np.random.randint(60, 100, size=25);
plt.hist(math, bins=8, color='red')
plt.title("수학시험의 히스토그램")
plt.ylabel("도수(frequency)")
plt.xlabel("시험 점수")
plt.ylim(0, 7)
plt.grid()


