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
    def __init__(self,ticker,risk,reward,buyRating):
        self.ticker = ticker
        self.risk = risk
        self.reward = reward
        self.buyRating = buyRating

nasdaqList = []

nasdaq = open("nasdaq.txt","r")
for line in nasdaq:
    tick = nasdaq.readline()
    tick = tick.replace("\n","")
    nasdaqList.append(Stock(tick,"","",""))
    
del nasdaqList[-1]
for obj in nasdaqList:
    print(obj.ticker)
    url = "https://finance.yahoo.com/quote/{}?p={}"
    url = url.format(obj.ticker,obj.ticker)
    soup = BeautifulSoup(requests.get(url).content,features="lxml")
    Val = soup.find("div",attrs={'class':"Fw(b) Fl(end)--m Fz(s) C($primaryColor"})
    if Val:
        obj.buyRating = Val.txt
    else: 
        obj.buyRating = "No Text"
    print(obj.buyRating)
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
