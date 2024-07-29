import matplotlib.pyplot as plt
import numpy as np
"""시험범위: 넘파이, 판다스, 시각화"""
x = np.arange(1, 20)
y = np.log(x)
y2 = 2*x**2
y3 = 10*x
d1 = ['m_0' + str(i) for i in range(1, 5)]
d2 = [27, 23, 45, 33]
d3 = [67, 78, 45, 34]
math = [98, 97, 96, 90, 100]
color_x = ['r', 'g', 'b', 'k']

%matplotlib inline

# 선 그래프
plt.plot(y)
plt.plot(y2)
clf() # 모두 닫기
close() # 현재 그래프만 닫기

#%% subplot
plt.subplot(3,2,1)
plt.plot(x, y, 'o', y2, '^')
plt.xlim(1, 17)
plt.ylim(1, 700)
plt.legend(['data' + str(i) for i in range(1, 5)], loc=0)

# 막대 그래프
plt.subplot(3,2,2)
plt.bar(d1, d2, color = 'r',
        tick_label= d1,
        width = 0.6)
plt.text(40, 2, "status")

plt.subplot(3,2,3)
plt.barh(d2, d3, color='b',
         tick_label = d1)

# 파이 그래프
plt.subplot(3,2,4)
plt.pie(d3, labels=d1, autopct='%.1f')

# 히스토그램
plt.subplot(3,2,5)
plt.hist(math)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# 산점도
plt.subplot(3,2,6)
plt.scatter(d2, d3, s=100,
            c=['r','g','b','y'], alpha=0.5)
plt.grid(True)


