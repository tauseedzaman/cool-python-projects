#!/usr/bin/env python
# Automating google search with selenuim

from selenium import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/dell/Desktop/py/Chromedriver.exe")

def wait():
	search_place=driver.find_element_by_id("searchboxinput")
	search_place.send_keys(Keys.ENTER)

	time.sleep(2)

url="https://www.google.com/"
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(5)

def search(string):
	try:
		search_box=driver.find_element_by_css_selector("input[name=q]")
		search_box.send_keys(string)
		search_box.send_keys(Keys.ENTER)
	except Exception as e:
		raise
	finally:
		print("Exit...")

# calll this
search("who am i")
