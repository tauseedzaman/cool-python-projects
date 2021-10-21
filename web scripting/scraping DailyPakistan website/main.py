#!/usr/bin/env python

#Get Top Stories from daily Pakistan website using python beautifulsoup
# Auther: Tauseed zaman

from bs4 import BeautifulSoup
import requests

def Get_News():
    html_text=requests.get("https://en.dailypakistan.com.pk/latest").text
    soup = BeautifulSoup(html_text, 'lxml')
    main_container = soup.find_all("div",{'class':["col-xs-12 col-sm-4 col-lg-3 verticle-widget-col news3"]})
    output=[]
    for i,item in enumerate(main_container):
       heading = item.find("small").text
       link = item.find("a").get("href")
       output.append({heading,link})
    return output
print(Get_News())