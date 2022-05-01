#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
fs = open("data.txt",'w')
def Get_News():
    html_text=requests.get("https://cybersophia.net/quotes/").text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.findAll("figure",class_="wp-block-image size-large has-filter-saturation")
    for i,post in enumerate(posts):
        link = (post.find("img").get("src")).replace("?resize=1000%2C563&ssl=1","")
        fs.write(link+'\n')

Get_News()
fs.close()
