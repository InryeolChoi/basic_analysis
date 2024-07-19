# 정규 표현식
import re

#%% 예제
# []
p = re.compile('[abc]')
m = p.findall('a cbcflks sdkflsalk ksadfkjkl asdfdfas')
print(m)

# dot(.)
p = re.compile('\d')
m = p.findall('a 2a 30 a9sdf 4 ca2b')
print(m)

# 사이 아무거나(...)
p = re.compile('a...b')
m = p.findall('aasdfb asdf asdf a1lfb')
print(m)

# 반복(*)
p = re.compile('go*gle')
m = p.findall('ggle gogle google goooogle goog')
print(m)

# 반복(+)
p = re.compile('go+gle')
m = p.findall('ggle gogle google goooogle goog')
print(m)

# 반복({m, n})
p = re.compile('go{1,4}gle')
m = p.findall('ggle gogle google goooogle goog')
print(m)

# 시작과 끝
p = re.compile('^book')
m = p.findall('book is')
print(m)

#%% 메타문자
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

p = re.compile('^Life')
m = p.search('Life is too short')
print(m)
print(re.search('^Life', 'Life is too short'))

#%% 그룹핑
p = re.compile('ABC')
m = p.search('ABCABCABC OK?')
print(m)

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

print(m.group())

#%% 컴파일 옵션
# DOTALL, S
p = re.compile('a.b')
m = p.search('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.search('a\nb')
print(m)

# ignorecase, I
p = re.compile('[a-z]+')
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

# MULTILINE, M
import string
string.whitespace

p = re.compile('^python\s\w+', re.MULTILINE)
data = """
python one 
life is too short
python two
you need python
python three """

print(p.findall(data))

#%% 컴파일 옵션2
# \A : 문자열 처음과 매치

p = re.compile('^\Apython\s\w+', re.MULTILINE)
data = """
python one 
life is too short
python two
you need python
python three """

print(p.findall(data))

# 백슬레시
p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile(r'\section')

print('a\nb')
print('\name')
print(r'\name')

print('C:\nome\nations')
print(r'C:\nome\nations')

# \b와 \B
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

#%% 문자열 바꾸기
p = re.compile('color', )
p.sub('color', 'blue socks adn red shoes', count=1)


p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search('Park 010-4564-1628')
print(m.group(2))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search('Park 010-4564-1628')

print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))

