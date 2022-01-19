#This test case was created by Ani Ter-Markosyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
browser = webdriver.Chrome(executable_path = r"C:\Users\VG\Desktop\webdriver\chromedriver_win32\\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
login = browser.find_element_by_xpath("//*[@id ='login_credentials']").text.split()[3]
browser.find_element_by_id("user-name").send_keys(login)
password = browser.find_element_by_css_selector(".login_password").text.split()[4]
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_id("login-button").click()
browser.implicitly_wait(3)

#Sort A-Z
browser.find_element_by_css_selector(".product_sort_container").click()
browser.find_element_by_xpath("//select[@class = 'product_sort_container']/option[1]").click()
inventory_items = browser.find_elements_by_xpath("//*[@class = 'inventory_item_name']")
list_of_products1 = []
for i in range (len(inventory_items)):
    list_of_products1.append(inventory_items[i].text)
if sorted(list_of_products1) == list_of_products1:
    print("First test case is passed.")
browser.implicitly_wait(10)

#Sort Z-A
browser.find_element_by_css_selector(".product_sort_container").click()
browser.find_element_by_xpath("//select[@class = 'product_sort_container']/option[2]").click()
inventory_items = browser.find_elements_by_xpath("//*[@class = 'inventory_item_name']")
list_of_products2 = []
for i in range (len(inventory_items)):
    list_of_products2.append(inventory_items[i].text)
if sorted(list_of_products2, reverse= True) == list_of_products2:
    print("Second test case is passed.")
browser.implicitly_wait(10)

# Sort(Price low to high)
browser.find_element_by_css_selector(".product_sort_container").click()
browser.find_element_by_xpath("//select[@class = 'product_sort_container']/option[3]").click()
inventory_prices_asc = browser.find_elements_by_xpath("//*[@class = 'inventory_item_price']")
list_of_prices1 = []
for i in range (len(inventory_prices_asc)):
    list_of_prices1.append(float(inventory_prices_asc[i].text[1:6]))
if sorted(list_of_prices1) == list_of_prices1:
    print("Third test case is passed.")
browser.implicitly_wait(10)

#Sort(Price high to low)
browser.find_element_by_css_selector(".product_sort_container").click()
browser.find_element_by_xpath("//select[@class = 'product_sort_container']/option[4]").click()
inventory_prices_desc = browser.find_elements_by_xpath("//*[@class = 'inventory_item_price']")
list_of_prices2 = []
for i in range (len(inventory_prices_desc)):
    list_of_prices2.append(float(inventory_prices_desc[i].text[1:6]))
if sorted(list_of_prices2, reverse = True) == list_of_prices2:
    print("Forth test case is passed.")
browser.implicitly_wait(10)
browser.quit()
