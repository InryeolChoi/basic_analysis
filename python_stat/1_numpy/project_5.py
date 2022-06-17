import numpy as np
import matplotlib.pyplot as plt
x = np.array(range(0, 10))
plt.rc('font', size=10)


#%% 폰트 변경
import matplotlib.font_manager as fm
from matplotlib import rc 
font_path = r"C:\Windows\Fonts\batang.ttc"
font_name = fm.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

x = np.array(range(-100, 100))
y = x**3 -3*x**2 + 2
plt.plot(x, y)
plt.xlabel("시간")
plt.ylabel("거리")
plt.xlim(-2, 10)
plt.ylim(-6, 10)
plt.show()

#%% 텍스트에 식 기입하기
x = np.array(range(0, 10))
plt.plot(x, 30*x+10, label='y = 30*x + 10')
plt.text(4, 190, "30*x+10")

#%% 텍스트에 수식 표현하기
# mat.rcParams.update({"text.usetex": True, "font.family": "Helvetica"})

y = 3*x**2 * np.sin(x)
plt.plot(x,y)
plt.text(4, 100, '${3}x^{2} + \sin{x}$')
plt.show()

