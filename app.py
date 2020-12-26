from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.daejeon.go.kr/corona19/index.do?menuId=0008")

bsObject = BeautifulSoup(html, "html.parser")
#page = soup.find('p').getText()
for page in bsObject.find_all('tr'):
    pages=page.getText()
    print(pages)

#content > div > div > div:nth-child(1) > div > div.table_scroll > table > tbody > tr:nth-child(23) > td:nth-child(4)")