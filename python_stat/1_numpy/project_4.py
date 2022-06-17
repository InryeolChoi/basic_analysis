# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:12:12 2022

@author: Peter
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'class1': [95, 92, 98, 100],
                    'class2': [91, 93, 97, 99]})
df1

df2 = pd.DataFrame({'class1': [87, 89], 
                    'class2': [85, 90]})

df2
df1.append(df2)
df1.append(df2, ignore_index=True)

a1 = df2.append(df1)
a2 = df2.append(df1, ignore_index=True)

#%% 가로 방향으로 통합하기: join()
# 기본 구조
df4 = pd.DataFrame({'class3': [93, 91, 95, 98]})
df1.join(df4)
df1.join(df2)

# index가 같은 경우
index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame({'class1': [95,92,98,100],'class2': [91,93,97,99]}, index=index_label)
df1a

df4a = pd.DataFrame({'class3': [93,91,95,98]}, index=index_label)
df4a
df1a.join(df4a)


# index가 다른 경우
df5 = pd.DataFrame({'class':[82, 92]})
df5

#%% 특정 열을 기준으로 통합하기
# 기본 구조
df_A_B = pd.DataFrame({'판매량': ['1월', '2월', '3월', '4월'],
                       '제품A': [100, 150, 200, 130],
                       '제품B': [90, 110, 140, 170]})
df_A_B

df_C_D = pd.DataFrame({'판매량': ['1월', '2월', '3월', '4월'],
                       '제품C': [112, 141, 203, 134],
                       '제품D': [90, 110, 140, 170]})
df_C_D

df_A_B.merge(df_C_D)

df_left = pd.DataFrame({'key':['A','B','C'], 'left':[1,2,3]})
df_left
df_right = pd.DataFrame({'key':['A','B','D'], 'right':[4,5,6]})
df_right

df_left.merge(df_right, how='left', on='key')
df_left.merge(df_right, how='right', on='key')
df_left.merge(df_right, how='outer', on='key')
df_left.merge(df_right, how='inner', on='key')

#%% example
test = pd.DataFrame({'name': ['브라운', '레드', '그린', '옐로우'],
                     'kor': [90, 99, 60, 89],
                     'math' : [87, 83, 82, 93],
                     'eng' : [79, 80, 77, 62]})
test
score1 = pd.DataFrame({'name':  ['브라운', '레드', '그린', '옐로우'],
                     'sci': [62, 87, 69, 72]})
score1
test.merge(score1, how='left', on='name')

score2 = pd.DataFrame({'name': ['핑크', '블루', '그린', '옐로우'],
                      'soc' : [70, 66, 93, 72]})

test.merge(score2, how='left', on='name')

score1 = pd.DataFrame({'name':  ['브라운', '레드', '그레이', '블랙'],
                     'sci': [62, 87, 69, 72]})
score1.merge(test, how='right', on='name')

test.merge(score1, how='outer', on='name')