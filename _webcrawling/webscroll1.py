import webbrowser

#%% 웹 페이지 열기 
url = "www.naver.com"
webbrowser.open(url)

naver_search_url = "http://search.naver.com/search.naver?query="
search_word = '데이터 엔지니어'
url = naver_search_url + search_word
webbrowser.open(url)


ur2 = "https://www.google.com/search?q="
search_words = ['python web scrapping', 'python with data science']
for search_w in search_words:
    webbrowser.open(ur2 + search_w)


url3 = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q="
search_words = ['애플', '아이폰', '아이패드']
for search_w in search_words:
    webbrowser.open(url3 + search_w)
    
#%% 페이지 만들기 1

%%writefile C:\Users\USER\Desktop\python_stat\data_ex.html
    <style>
        body {
            background-color: white;
        }
        .main {
            border-radius: 50px;
            width: 500px;
            height: 200px;
            background-color: wheat;
            color: blue;
            text-align: center;
        }
        .x {
            width: 500px;
            height: 150px;
            background-color: white;
        }
    </style>
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8"> 
            <title>Title</title>
        </head>
        <body>
            <div class=main>
                <h2>introduction of data crawling</h2>
                <div>안녕하세요</div>
                <p>파이썬 크롤링 책 1
                <p>박정태 지음
                <div>
                    <input type="text">
                    <button>버튼1</button>
                </div>
            </div>
            <div class=x>
                <ul>
                    <li><input type="button" value="text1"></li>
                    <li>1</li>
                    <li>2</li>
                    <li>3</li>
                    <li><a href="https://www.youtube.com">유튜브</a></li>
                </ul>
            </div>
            <div class=x>
                <span>1<br></span>
                <span>2<br></span>
                <span>3<br></span>
            </div>
        </body>
    </html>

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


