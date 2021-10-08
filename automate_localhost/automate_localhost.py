#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_db_name="pythonBD"

my_table_name="pythonTestTable"
number_of_columns_in_my_table=3

os.environ["PATH"] += r"C:/Users/dell/Desktop/py"

# choose webdrivr
driver = webdriver.Chrome()
driver.maximize_window()

# wait when the page is ready seconds.
driver.implicitly_wait(10)

# goto the webpage
driver.get("http://localhost/")

find_php_myadmin = driver.find_element_by_css_selector("a[href='/phpmyadmin/']")
find_php_myadmin.click()


# find new database btn and click
find_create_new_database= driver.find_element_by_css_selector("a[href='server_databases.php?server=1']")
find_create_new_database.click()

# find database name input field and insert database name
insert_db_name_field=driver.find_element_by_id("text_create_db")
insert_db_name_field.send_keys(my_db_name)

# find create btn and click
click_create_database_btn=driver.find_element_by_id("buttonGo");
click_create_database_btn.click()

# insert table name
insert_table_name=driver.find_element_by_name("table")
insert_table_name.send_keys(my_table_name)


# insert columns numbers
insert_number_of_columns=driver.find_element_by_name("num_fields")
insert_number_of_columns.clear()
insert_number_of_columns.send_keys(number_of_columns_in_my_table)

# find create btn and click
click_create_table_btn=driver.find_element_by_css_selector("input[type='submit']");
click_create_table_btn.click()


# insert id in the first field
insert_field_0_1=driver.find_element_by_id("field_0_1")
insert_field_0_1.clear()
insert_field_0_1.send_keys("id")


insert_field_type_field_0_1=driver.find_element_by_name("field_type[0]")
insert_field_type_field_0_1.send_keys("INT")

# insert id length
insert_field_0_3=driver.find_element_by_id("field_0_3")
insert_field_0_3.clear()
insert_field_0_3.send_keys(12)

# insert name in the second field
insert_field_1_1=driver.find_element_by_id("field_1_1")
insert_field_1_1.clear()
insert_field_1_1.send_keys("name")

# insert type of field
insert_field_type_field_1_1=driver.find_element_by_name("field_type[1]")
insert_field_type_field_1_1.send_keys("VARCHAR")

# # insert name length
insert_field_1_3=driver.find_element_by_id("field_1_3")
insert_field_1_3.clear()
insert_field_1_3.send_keys(100)



# # # insert phone in the third field
insert_field_3_1=driver.find_element_by_id("field_2_1")
insert_field_3_1.clear()
insert_field_3_1.send_keys("phone")


# # insert type of field
insert_field_type_field_2_1=driver.find_element_by_name("field_type[2]")
insert_field_type_field_2_1.send_keys("VARCHAR")

# # insert name length
insert_field_2_3=driver.find_element_by_id("field_2_3")
insert_field_2_3.clear()
insert_field_2_3.send_keys(25)


# # click on set is null btn which has  id field_2_7
insert_null_field_2_7=driver.find_element_by_id("field_2_7")
insert_null_field_2_7.click()
insert_null_field_2_7.send_keys(Keys.ENTER)


go_to_index_page= driver.find_element_by_css_selector("a[href='index.php']")
go_to_index_page.click()


