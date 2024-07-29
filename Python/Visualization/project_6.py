import matplotlib.pyplot as plt
import numpy as np

# 산점도 그리기
x = [165, 177, 160, 180, 185, 155, 172] 
y = [62, 67, 55, 74, 90, 43, 64]
plt.scatter(x, y, c='blue') # s = 36
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.show()

# 색상 조정
plt.subplot(1, 2, 1)
plt.scatter(x, y, c='blue') # s = 36
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(x, y, c='red') # s = 36
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.show()

# 사이즈 조정
plt.subplot(1, 2, 1)
plt.scatter(x, y, c='blue', s=36) # s = 36
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(x, y, c='blue', s = 300) # s = 36
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height & Weight')
plt.grid(True)
plt.show()

# 데이터마다 다른 사이즈
x_size = np.arange(1, 8) * 100
x_color = ['g', 'r', 'b', 'c', 'm', 'y', 'k']
plt.scatter(x, y, s = x_size, c = x_color)

# 인구밀도 시각화 예제
import matplotlib as mat
mat.rcParams['font.family']
import matplotlib.font_manager as matf
font_list = matf.get_fontconfig_fonts()
font_names = [matf.FontProperties(fname=fname).get_name() for fname in font_list]
f = open(r"C:\Users\dlsfu\Desktop\python_stat\my_font_list.txt", "w")
for font_name in font_names: f.write(font_name + "\n")
f.close()
mat.rcParams['font.family'] = 'Malgun Gothic'
mat.rcParams['axes.unicode_minus'] = False


city_name = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
long = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]

pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2955]
size = np.array(pop_den) * 0.2
city_color = ['r', 'g', 'b', 'c', 'm', 'k', 'y']

plt.scatter(long, lat, s=size, c=city_color, alpha=0.5)
plt.xlabel("경도(longtitude)")
plt.ylabel("위도(latitude")
plt.title("지역별 인구밀도(2019)")
for lng, lt, cn in zip(long, lat, city_name):
    plt.text(lng, lt, cn)
plt.show()

#%% zip()
# 1st method
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [94, 96, 97, 94]
for k in range(len(scores)):
    print(names[k], scores[k])
    
# 2nd method: zip()
for name, score in zip(names, scores):
    print(name, score)
    
#%% 그래프 저장하기
# 그래프 크기 / dpi 판단
import matplotlib as mpl
mpl.rcParams['figure.figsize']
mpl.rcParams['figure.dpi']

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]
explode_value = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 10))
plt.pie(result, labels= fruit, autopct="%.1f%%", explode = explode_value)

plt.savefig(r"C:\Users\dlsfu\Desktop\python_stat\figtest.png", dpi=200)
plt.show()
