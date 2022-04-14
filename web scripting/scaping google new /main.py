#!/usr/bin/env python

#Get Top Stories  new.google using python beautifulsoup
# Auther: Tauseed zaman

from bs4 import BeautifulSoup
import requests
url="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKUVN5Z0FQAQ/sections/CAQiR0NCQVNMd29JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pRU3lJTkNBUWFDUW9ITDIwdk1HMXJlaW9KRWdjdmJTOHdiV3Q2S0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pRU3lnQVABUAE?hl=en-PK&gl=PK&ceid=PK:en"
def Get_News():
    html_text=requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.findAll("article")
    output=[]
    for post in posts:
        link = post.find("a",class_="RZIKme").get('href').replace("?hl=en-PK&gl=PK&ceid=PK%3Aen","")
        link = "https://news.google.com"+link.replace("./","/")
        heading = post.find("a",class_="RZIKme").decode_contents().strip()
        output.append({heading,link})
    return output


print(Get_News())