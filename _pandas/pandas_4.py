# 언어 및 폰트 변경
import matplotlib.pyplot as plt
import matplotlib as mpt
mpt.rcParams['font.familiy']

#%% 언어 및 폰트 변경

import matplotlib as mat
mat.rcParams['font.family']

import matplotlib.font_manager as matf
font_list = matf.get_fontconfig_fonts()
font_names = [matf.FontProperties(fname=fname).get_name()
              for fname in font_list]

f = open(r"C:\Users\dlsfu\Desktop\python_stat\my_font_list.txt", "w")
for font_name in font_names: f.write(font_name + "\n")
f.close()

mat.rcParams['font.family'] = 'Malgun Gothic'
mat.rcParams['axes.unicode_minus'] = False

#%% 그래프 저장
names = ['a', 'b', 'c', 'd', 'e', 'f']
score= [90, 80, 40, 68, 93, 70]
plt.scatter(names, score, s=600)
for n, s in zip(names, score):
    plt.text(n, s)
    
plt.savefig(r"C:\Users\dlsfu\Desktop\python_stat\x.png", dpi=200)
plt.show()
