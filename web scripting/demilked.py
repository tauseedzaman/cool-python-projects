#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
fs = open("data.js",'w')
fs.write("const news=[")

def Get_News():
    html_text=requests.get("https://www.demilked.com/funniest-it-programming-memes/").text
    soup = BeautifulSoup(html_text, 'lxml')
    images = soup.findAll("img",{"loading" : "lazy"})
    for image in images:
        heading = image.get("src")
        link = image.get("src")
        hashtage = "#programming #memes #funny #memes"
        fs.write('{heading:"'+heading+'",link:"'+link+'",hashtages:"'+hashtage+'"},\n')


Get_News()
fs.write("];")
fs.write("export default news")
fs.close()
