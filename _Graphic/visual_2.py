import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%% matplotlib로 그래프 그리기
data1 = [10, 14, 9, 20, 25]
%matplotlib qt
plt.plot(data1)
plt.close()

%matplotlib inline
plt.plot(data1)
plt.show()

#%% x,y 모두 들어간 2차원 그래프
x = np.arange(-4.5, 5, 0.5)
y = 2*x**2

plt.plot(x, y)
plt.show()

#%% 여러 그래프 선택

x = np.arange(-4.5, 5, 0.5); x
y1 = 2*x**2; y1
y2 = 5*x + 30; y2
y3 = 4*x**2 + 10; y3

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()

#%% figure() : 창 쪼개기 가능
# clf(n) : n번 창의 그래프 지우기
# clf() : figure()와 같이 묶어서 쓰면 바로 위에 창 지우기 가능

x = np.arange(-5, 5, 0.1); x
y1 = x*2 - 2; y1
y2 = 20 * np.cos(x) ** 2; y2

plt.figure(1)
plt.plot(x, y1)
plt.figure(1)
plt.plot(x, y2)

plt.figure(2)
plt.plot(x, y1)
plt.figure(2)
plt.plot(x, y2)
plt.clf()

# close() : 팝업된 그래프 창 닫기
plt.close()

# %matplotlib qt 사용
%matplotlib qt
plt.figure(1)
plt.plot(x, y1)

plt.figure(2)
plt.plot(x, y2)

plt.figure(1)
plt.plot(x, y2)

plt.figure(2)

plt.clf()
plt.plot(x, y1)

plt.show()
plt.close()

# inline()
%matplotlib inline
plt.figure(1)
plt.plot(x, y1)

plt.figure(2)
plt.plot(x, y2)

plt.figure(1)
plt.plot(x, y2)

plt.figure(2)

plt.clf()
plt.plot(x, y1)

plt.show()


#%% subplot()
x = np.arange(0, 10, 1)
y1 = 0.3*(x-5)**2
y2 = (-1.5)*x + 3
y3 = np.sin(x) ** 2
y4 = 10 * np.exp((-x) + 1)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.show()

plt.subplot(2,2,1)
plt.plot(x, y1)

plt.subplot(2,2,2)
plt.plot(x, y2)

plt.subplot(2,2,3)
plt.plot(x, y3)

plt.subplot(2,2,4)
plt.plot(x, y4)

plt.show()
