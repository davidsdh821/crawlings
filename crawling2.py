import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#크롤링이 가능한 이유, 이미 데이터를 받아왔기 때문이다
# 코딩 시작

trs = soup.select('#old_content > table > tbody > tr');
for tr in trs:
    a_tag= tr.select_one('td.title > div > a')
    if a_tag is not None:
        print(a_tag.text) #title = a_tag.text

#old_content > table > tbody > tr:nth-child(7)
#old_content > table > tbody > tr:nth-child(9)
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a