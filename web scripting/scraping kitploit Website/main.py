#!/usr/bin/env python

#Get Top Stories  kitploit website using python beautifulsoup
# Auther: Tauseed zaman

from bs4 import BeautifulSoup
import requests

def Get_News():
    html_text=requests.get("https://www.kitploit.com/").text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.findAll("div",class_="post-outer")
    output=[]
    for post in posts:
        heading = post.find("span",class_="fn").decode_contents().strip()
        link = post.find("a").get("href")
        output.append({heading,link})
    return output


print(Get_News())
