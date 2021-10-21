#Get Top Stories from geo news websites using python beautifulsoup
# Auther: tauseed zaman
from bs4 import BeautifulSoup
import requests


def get_Geo_News():
	html_text=requests.get("https://www.geo.tv/").text
	soup = BeautifulSoup(html_text, 'lxml')
	posts = soup.find_all("article")
	output =[]
	for i,post in enumerate(posts):
		a_tage = post.find("a")
		output.append({"No":i ,"heading": a_tage.text.strip(),"link": a_tage.get('href')})
	return output

print(get_Geo_News())