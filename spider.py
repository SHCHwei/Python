import requests
from bs4 import BeautifulSoup

r = requests.get("https://huaku.com.tw/governance_download?id=1") #將此頁面的HTML GET下來
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.find_all("a")
for s in sel:
    print( s.get('href')) 