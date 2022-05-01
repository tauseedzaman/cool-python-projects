	#Get all Databases from localhost using python beautifulsoup
from bs4 import BeautifulSoup
import requests

html_text=requests.get("http://localhost/phpmyadmin/server_databases.php").text

soup = BeautifulSoup(html_text, 'lxml')

all_tds = soup.find_all("td", class_="name")

i=1
for td in all_tds:
	target_as=td.find_all("a")

	for a in target_as:
		print(f"[{i}] Database Name: {a.text.strip()}")
		i=i+1
