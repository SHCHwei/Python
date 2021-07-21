import requests
import json
import csv
import os
import pandas as pd

html_doc = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210401&stockNo=5608&_=1623765171537").text #將此頁面的HTML GET下來
AllData = json.loads(html_doc)


targetData = [["日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"]]

#彙整資料
for row in range( len(AllData['data']) ):
    targetData.append(AllData['data'][row])


with open('5608.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  # 寫入二維表格
  writer.writerows(targetData)



# 檢查檔案是否存在
if os.path.isfile("5608.csv"):
  print("檔案已經建立")
else:
  print("失敗")