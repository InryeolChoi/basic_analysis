#%% 페이지 만들기 2
%%writefile C:\Users\USER\Desktop\python_stat\data_ex2.html
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8"> 
            <title>Title</title>
        </head>
        <body>
            <h1>출간된 책 정보1</h1>
            <p id="book_title"> 이해가 쑥쑥 되는 파이썬 </p>
            <p id="author"> 홍길동 </p>
            <p id="publisher"> 위키북스 출판사 </p>
            <p id="year"> 2018 </p>
            <h1>출간된 책 정보2</h1>
            <p>파이썬 자연어 이론</p>
                <span>span1</span>
                <span>span2</span>
            <p>이순신</p>
            <ul>
                <li>1. 실무진 강추</li>
                <li>2. 후기 좋음</li>
            </ul>
        </body>
    </html>

#%% beatifulsoup과 그 응용
from bs4 import BeautifulSoup

# 테스트용 html 코드

html = """<html><body><div><span>\
            <a href=https://www.naver.com/>naver</a>
            <a href=https://www.google.com/>google</a>
            <a href=https://www.daum.net/>daum</a>
            <\span><\div><\body><\html>"""
            
# beautifusoup를 이용, html 소스를 파싱
soup = BeautifulSoup(html, 'lxml')
soup

print(soup.prettify())
soup.find('a')
soup.find('a').get_text()

sites = soup.find_all('a')
for site_name in sites:
    print(site_name.get_text())

#%% 2번째 테스트
html = """
    <html>
    <head>
        <title>작품과 작가 모음</title>
    </head>
    <body>
        <h1>책 정보</h1>
        <p id="book_title">토지</p>
        <p id="author">박경리</p>
        <p id="book_title">태백산맥</p>
        <p id="author">조정리</p>
        <p id="book_title">감옥으로부터의 사색</p>
        <p id="author">신영복</p>
    </body>
    </html>
"""
from bs4 import BeautifulSoup

soup2 = BeautifulSoup(html, "lxml")
print(soup2.prettify)
soup2.title
soup2.title.get_text()

soup2.body
soup2.body.h1.get_text()
soup2.find_all('p')

soup2.select('body h1')
soup2.select('head title')
soup2.select('body p')
soup2.select('p')
soup2.select('p#book_title')
soup2.select('p#author')

book_titles = soup.find_all('p', {"id": "book_title"})
authors = soup.find_all('p', {"id": "author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())


#%% css를 이용한 테스트
soup2 = BeautifulSoup(html, "lxml")
book_titles = soup2.select('p#book_title')
authors = soup2.select('p#author')

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())