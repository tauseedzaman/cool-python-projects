#!/usr/bin/env python
# Automating google maps with selenuim

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/dell/Desktop/py/Chromedriver.exe")

url="https://www.google.com/maps/"
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(10)

def wait():
	time.sleep(3)

def search_place(place="malakand"):
	search_place=driver.find_element_by_id("searchboxinput")
	search_place.send_keys(place)
	search_place.send_keys(Keys.ENTER)

# get directins and find lenght to at
def directions():
		direction=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span")
		direction.click()

def find():
		find=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
		find.send_keys("iran")
		find.send_keys(Keys.ENTER)
try:
	search_place("Afghanistan")
	wait()
	directions()
	wait()
	find()


	print("w")
except Exception as e:
	raise
finally:
	print("Exit...")

