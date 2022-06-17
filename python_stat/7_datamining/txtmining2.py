# 비정형 데이터: 구조화되지 않은 데이터
# 비정형 자료: unstructed data
# NLP, 워드클라우드: 비슷한 데이터 모아 생성

#%% 준비

import konlpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import *

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt()


with open('대한민국헌법.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#%% 형태소 분석
nouns = okt.nouns(text)
nouns

Counter(nouns)

#%% 빈도수 산출
Counter(nouns).most_common(20)

#%% 전처리 1 - 단어 글자수 필터링