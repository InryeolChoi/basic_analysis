import matplotlib.pyplot as plt
import numpy as np
#%% 출력범위 지정
x = np.linspace(-4, 4, 100) # [-4. 4] 범위 내에서 100개 값 생성
x
y1 = x**3
y2 = 10*x**2 - 2 

%matplotlib inline
plt.plot(x, y1, x, y2)
plt.xlim(-5, 5)
plt.ylim(-100, 200)
plt.show()

#%% 그래프 꾸미기: 색과 아이콘
x = np.arange(0, 5, 1)
for i in range(1,5):
    globals()['y%d' % i] = x + (i-1)
    
plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.show()

plt.plot(x,y1,'m',x,y2,'y',x,y3,'k', x, y4, 'c')

plt.plot(x,y1,'-',x,y2,'--',x,y3,':', x, y4, '-,')

plt.plot(x,y1,'o',x,y2,'^',x,y3,'s', x, y4, 'd')

plt.plot(x,y1,'>--r', x,y2,'s-g',x,y3,'d:b', x, y4, '-')


#%% 그래프 꾸미기: 라벨, 제목, 격자, 범례, 문자열
x = np.arange(-4.5, 5, 0.5); x
y = 2*x**3

plt.plot(x, y)
plt.xlabel('invest')
plt.ylabel('output')
plt.title('Analysis of 2018 Q4')
plt.grid(True)
plt.show()

# 범례 지정
x = np.arange(0, 5, 1)
for i in range(1,5):
    globals()['y%d' % i] = x + (i-1)

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data%d'%i for i in range(1,5)])
plt.show()

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data%d'%i for i in range(1,5)], loc='upper left')
plt.show()

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data%d'%i for i in range(1,5)], loc='lower right')
plt.show()

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data%d'%i for i in range(1,5)], loc='center')
plt.show()

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['data%d'%i for i in range(1,5)], loc=4)
plt.xlabel('invest')
plt.ylabel('output')
plt.title("graph title")
plt.show()

# 한글 폰트 넣기
plt.rcParams['font.family']
import matplotlib.font_manager as plt_f

font_list = plt_f.get_fontconfig_fonts()
font_names = [plt_f.FontProperties(fname=fname)
              .get_name() for fname in font_list]

f = open(r"C:\Users\USER\Desktop\python_stat\my_font_list.txt", "w")
for font_name in font_names:
    f.write(font_name + "/n")
f.close()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 한글 폰트 그리기
plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['공장%d'%i for i in range(1,5)], loc=4)
plt.xlabel('투입 원자재 량')
plt.ylabel('총 생산량', rotation=90)
plt.title("`22 Q1 공장별 생산량")
plt.show()

#%% 문자열 표시
plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.text(0, 6, "문자열 출력 1")


