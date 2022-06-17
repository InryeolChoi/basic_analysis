# 텍스트 마이닝
import konlpy

msg = '한 학기 동안 수고 많으셨습니다. 모두 행복하십시오.'

from konlpy.tag import Hannanum

hannanum = Hannanum()

print(hannanum.morphs(msg))
print(hannanum.nouns(msg))
print(hannanum.pos(msg))
hannanum.tagset0

from konlpy.tag import Kkma
kkma=Kkma()
kkma.tagset
print(kkma.morphs(msg))
print(kkma.pos(msg))
print(kkma.sentences(msg))

from konlpy.tag import Komoran
komoran.tagset
komoran = Komoran()
print(komoran.morphs(msg))
print(komoran.nouns(msg))

from konlpy.tag import Okt
okt = Okt()
print(okt.morphs(msg))

#%% 자체함수
def get_pos(x):
    okt = Okt()
    post = okt.pos(x)
    
    result = []
    
    for a1 in post:
        result.append(f'{a1[0]}/{a1[1]}')
        
    return result

print(get_pos('한 학기 동안 수고 많으셨습니다.'))

#%% 정규화 및 필터링
okt.pos(msg)   
okt.pos(msg, norm=True, stem=True)
print(okt.pos)

okt_filtering = [x for x, y in okt_pos if y in ['Noun', 'Adjective', 'Verb']]
print(okt_filtering)

#%% 형태소 분석
import re
def text_cleaning(text):
    hangul = re.compile('[^ ㄱ- | 가-힣]+')
    return hangul.sub('', text)    

text_cleaning('<b> 오늘 드디어 코로나 종식')
