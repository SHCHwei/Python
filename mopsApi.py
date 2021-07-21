import requests
import datetime
from bs4 import BeautifulSoup

toDay = datetime.datetime.today()

#西元轉民國年分
miYear = toDay.year - 1911

for years in range(102, int(miYear)+1) :
    
    for mon in range(1 , 2):

        if( years == int(miYear) and mon == toDay.month ) :
             break
        my_data = {
        'encodeURIComponent': 1,
        'step': 1,
        'firsti n': 1,
        'off': 1,
        'keyword4': '',
        'code1': '',
        'TYPEK2': '',
        'checkbtn': '',
        'queryName': 'co_id',
        'inpuType': 'co_id',
        'TYPEK': 'all',
        'isnew': False,
        'co_id':'3037' , 
        'year': 102 , 
        'month' : 1, 
        }

        r = requests.post("https://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs" , data=my_data ) #將此頁面的HTML GET下來
        html_doc = BeautifulSoup(r.text,"html.parser")
        data = html_doc.find('td',"odd").text.strip().replace(',','')
        print(data)
        break
        
        #allData = {"月營收" :data}



