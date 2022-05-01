#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
# saving data in js file for later use
fs = open("data.js",'w')
fs.write("const news=[")

# get data
def Get_News():
    html_text=requests.get("https://www.thecoderpedia.com/blog/programming-memes/").text
    soup = BeautifulSoup(html_text, 'lxml')
    images = soup.findAll("img",class_="attachment-large size-large lazyload")
    output=[]
    for image in images:
        heading = image.get("alt")
        link = image.get("data-src")
        print(heading)
        print(link)
        hashtage = (heading.replace('"',"")).replace(" "," #")
        fs.write('{heading:"'+heading+'",link:"'+link+'",hashtages:"'+hashtage+'"},\n')
    return output


Get_News()
fs.write("];")
fs.write("export default news")
fs.close()
