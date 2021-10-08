#!/usr/bin/env python
# Automating PHP PDO CRID with selenuim

from selenium import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def wait():
	time.sleep(2)
# get the url
driver.get("http://localhost/php/PDO/index.php")

driver.maximize_window()
driver.implicitly_wait(5)

try:
	# insert an item
	name_input_field = driver.find_element_by_css_selector("input[name='name']")
	name_input_field.send_keys("tauseed")
	wait() # wait for 2 second
	email_input_field = driver.find_element_by_css_selector("input[name='email']")
	email_input_field.send_keys("tauseed@gmail.com")
	wait()
	find_submit_btn = driver.find_element_by_id("submit_btn")
	find_submit_btn.click()
	wait()
	# delete an item
	first_row = driver.find_element_by_id("delete_btn")
	first_row.click()
	wait()
	# edit row
	edit_btn=driver.find_element_by_id("edit_btn")
	edit_btn.click()
	wait()
	# update fields row
	update_name_field= driver.find_element_by_css_selector("input[name='e_name']")
	update_name_field.send_keys("zaman")
	wait()
	update_email_field= driver.find_element_by_css_selector("input[name='e_email']")
	update_email_field.send_keys(Keys.ARROW_RIGHT,Keys.ARROW_RIGHT,Keys.ARROW_RIGHT,Keys.ARROW_RIGHT,Keys.ARROW_RIGHT,Keys.ARROW_RIGHT,Keys.ARROW_RIGHT)
	update_email_field.send_keys("zaman") 
	wait()
	find_update_btn=driver.find_element_by_css_selector("button[type='submit']")
	find_update_btn.click()
except Exception as e:
	raise
finally:
	print("Exit...")
