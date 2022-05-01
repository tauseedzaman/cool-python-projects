#!/usr/bin/env python

#Get Top Stories from bbmlf.org website using python beautifulsoup
# Auther: Tauseed zaman



from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})



def get_bbmf_news():
    html_text=requests.get("https://bbmlf.org/top-tech-news/",headers = headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all("div",class_="wpra-grid-item")
    output=[]
    for post in posts:
        result = post.find_all("div", class_=["wpra-grid-item__item","wpra-grid-item__title"])
        title = result[0].text.strip()
        link = post.find("a").get("href").strip()
        output.append({"title":title,"link":link})
    return output


print(get_bbmf_news())