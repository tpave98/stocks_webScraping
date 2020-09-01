# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:32:49 2020

@author: Thomas
"""

from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def selective_str(myString):
    if (myString.find('>') > 0): # only runs if the start character is found in the string
        myString = myString[(myString.find('>')+1):] # sets the string back ingto
        myString = myString[:myString.find('<')]
    return myString

class Stock:
    def __init__(self,ticker,insiderTrans,pOverS,instTrans,targetPrice,yearRange,dividend,RSI,price,recommend):
        self.ticker = ticker
        self.insiderTrans = insiderTrans
        self.pOverS = pOverS
        self.instTrans = instTrans
        self.targetPrice = targetPrice
        self.yearRange = yearRange
        self.dividend = dividend
        self.RSI = RSI
        self.price = price
        self.recommend = recommend

nasdaqList = []

nasdaq = open("nasdaq.txt","r")
for line in nasdaq:
    tick = nasdaq.readline()
    tick = tick.replace("\n","")
    nasdaqList.append(Stock(tick,"","","","","","","","",""))

del nasdaqList[-1]
for obj in nasdaqList:
    url = "https://finviz.com/quote.ashx?t={}"
    url = url.format(obj.ticker)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    soup = BeautifulSoup(requests.get(url,headers = header).content,features="lxml")

    val = soup.find("table", attrs={'width': '100%', 'cellpadding': '3', 'cellspacing': '0', 'border': '0','class': 'snapshot-table2'})

    data = soup.findAll("td", attrs={'class': 'snapshot-td2'})
    if val:
        info = []
        for item in data:
            info.append(item.text)
        obj.insiderTrans = info[9]
        obj.pOverS = info[19]
        obj.instTrans = info[21]
        obj.targetPrice = info[28]
        obj.yearRange = info[34]
        obj.dividend = info[42]
        obj.RSI = info[52]
        obj.price = info[65]
        obj.recommend = info[66]
    else:
        obj.insiderTrans = "ERROR"
        obj.pOverS = "ERROR"
        obj.instTrans = "ERROR"
        obj.targetPrice = "ERROR"
        obj.yearRange = "ERROR"
        obj.dividend = "ERROR"
        obj.RSI = "ERROR"
        obj.price = "ERROR"
        obj.recommend = "ERROR"
        
        
    print("\nTicker: {}\nInsider Trading: {}\nP/S: {}\nInstitutional Trading: {}\nTarget Price: {}\n52 Week Range: {}\nDividend: {}\nRSI: {}\nPrice: {}\nRecommendation: {}\n".format(obj.ticker,obj.insiderTrans,obj.pOverS,obj.instTrans,obj.targetPrice,obj.yearRange,obj.dividend,obj.RSI,obj.price,obj.recommend))

nasdaq.close




#while True:

#
#
#
#    soup = BeautifulSoup(requests.get("https://darksky.net/forecast/41.4936,-71.3087/us12/en").content,features="lxml")
#    out_feels_like_F = soup.find("span", attrs={'class': 'feels-like-text'}).text
#    out_humid = soup.find("span", attrs={'class': 'num swip humidity__value'}).text
#    Num_out_feels_like_F = out_feels_like_F[:-1]
#    Num_out_feels_like_F = int(Num_out_feels_like_F,10)
#    Num_out_humid = int(out_humid,10)
#    now = datetime.now()
#    current_time = now.strftime("%H:%M:%S")
#    print("\nCurrent Time =", current_time)
#    print("Outdoor Temp:", out_feels_like_F,"F","\nOutdoor Humidity:",out_humid,"%\n")
#    time.sleep(5)
