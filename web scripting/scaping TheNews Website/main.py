#!/usr/bin/env python

#Get Top Stories from TheNews website using python beautifulsoup
# Auther: Tauseed zaman

from bs4 import BeautifulSoup
import requests

def Get_News():
	html_text=requests.get("https://www.thenews.com.pk/latest-stories").text
	soup = BeautifulSoup(html_text, 'lxml')
	posts = soup.find_all("div",{'class':["writter-list-item-story"]})
	output =[]
	for i,post in enumerate(posts):
		heading = post.find("h2").text.strip()
		link = post.find("a").get("href")
		output.append({"No":i, "title":heading, "link": link})
	return output
print(Get_News())