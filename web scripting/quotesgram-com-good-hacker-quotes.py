#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
# saving data in js file for later use
fs = open("data.js",'w')
fs.write("const news=[")

# get data
def Get_News():
    html_text=requests.get("https://quotesgram.com/good-hacker-quotes/").text
    soup = BeautifulSoup(html_text, 'lxml')
    images = soup.findAll("span",class_="relimgwrap")
    for image in images:
        heading = image.find("img").get("alt")
        link = image.find("img").get("src")
        hashtage = (heading.replace('"',"")).replace(" "," #")
        print(heading,link)
        fs.write('{heading:"'+heading+'",link:"'+link+'",hashtages:"'+hashtage+'"},\n')


Get_News()
fs.write("];")
fs.write("export default news")
fs.close()
