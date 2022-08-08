#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

fs = open("data.json", 'w')
fs.write("[")


def main():
    html_text = requests.get(
        "https://depositphotos.com/vector-images/14-august.html", headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all("img", class_="file-container__image _file-image")
    output = []
    for post in posts:
        title = post.get("title")
        src = post.get("src")
        output.append({"title": title, "src": src})
        fs.write('{"title":"'+title+'","src":"'+src+'"},\n')
    return output


print(main())
fs.write("]")
fs.close()
