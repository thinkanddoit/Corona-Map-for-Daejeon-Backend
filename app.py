import requests
from bs4 import BeautifulSoup
import json
import os

#app.py 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

webpage = requests.get("https://www.daejeon.go.kr/corona19/index.do?menuId=0008")
soup = BeautifulSoup(webpage.content,"html.parser")

# print(soup)

#태그 탐색하기
# print(soup.p) 첫번째 p태그
# print(soup.p.string) 텍스트 가져오기

#트리구조 사용하기
# for child in soup.ul.children:
#     print(child)
# for parent in soup.ul.parents:
#     print(parent)

#find_all
# print(soup.find_all("p"))

data={}

trs = soup.tbody.find_all('tr')
for i, tr in enumerate(trs):
    tds = tr.find_all('td')
    for j, td in enumerate(tds):
        ps = td.find_all('p')
        print(ps[0].text)
        data["d"] = ps[0].text


with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)