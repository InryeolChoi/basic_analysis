import pandas as pd
import matplotlib as mpt
import matplotlib.pyplot as plt
#%% 엑셀 데이터 시각화

report = pd.DataFrame({'제품1': [10, 15, 12, 11, 12, 14, 13],
                       '제품2': [9, 11, 14, 12, 13, 10, 12]},
                      index = [str(i) for i in range(9, 16)],
                      )
report.index.name = '시간'
report

# 글꼴 설정

mpt.rcParams['font.family']
import matplotlib.font_manager as fm

font_list = fm.get_fontconfig_fonts()
font_names = [fm.FontProperties(fname=fname).get_name() for fname in font_list]

f = open(r"C:\Users\dlsfu\Desktop\python_stat\data\my_font_list.txt", "w")
for font_name in font_names:f.write(font_name + "/n")
f.close()

mpt.rcParams['font.family'] = 'Malgun Gothic'
mpt.rcParams['axes.unicode_minus'] = False

# 그래프 그리기 & 저장

product_plot = report.plot(grid = True, style=['-*', '-o'], title='시간대별 생산량')
product_plot.set_ylabel("생산량")

image_file = r'C:\Users\USER\Desktop\python_stat\Excel_file\fig_for_excel.png'
plt.savefig(image_file, dpi = 400)
plt.show()

#%% 엑셀 파일에 이미지 집어놓기
excel_file = r'C:\Users\dlsfu\Desktop\python_stat\Excel_file\data_img.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
report.to_excel(excel_writer, index=True, sheet_name='Sheet1')

worksheet = excel_writer.sheets['Sheet1']
worksheet.insert_image('D2', image_file, {'x_scale' : 1.4, 'y_scale' : 1.4})
excel_writer.save()

#%% 엑셀 파일에 차트 만들기
# ExcelWriter로 차트 제작
excel_chart = pd.ExcelWriter(r"C:\Users\dlsfu\Desktop\python_stat\Excel_file\data_chart.xlsx", engine='xlsxwriter')
report.to_excel(excel_chart, index=True, sheet_name = 'Sheet1')

# 워크북, 워크시트
workbook = excel_chart.book
worksheet = excel_chart.sheets['Sheet1']

# 차트 종류 지정
chart = workbook.add_chart({'type' : 'line'})

# 범위지정
chart.add_series({'values': '=Sheet1!$B$2:$B$8',
                  'categories': '=Sheet1!$A$2:$A$8',
                  'name': '=Sheet1!$B$1'})

chart.add_series({'values': '=Sheet1!$C$2:$C$8',
                  'categories': '=Sheet1!$A$2:$A$8',
                  'name': '=Sheet1!$C$1'})

# 제목, 라벨
chart.set_title({'name' : '시간대별 생산량'})
chart.set_x_axis({'name' : '시간'})
chart.set_y_axis({'name' : '생산량'})

worksheet.insert_chart('D2', chart)

excel_chart.save()




