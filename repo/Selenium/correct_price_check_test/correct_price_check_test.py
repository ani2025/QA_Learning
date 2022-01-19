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

browser.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
browser.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
browser.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt").click()
browser.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()
browser.find_element_by_id("add-to-cart-sauce-labs-onesie").click()
browser.find_element_by_id("add-to-cart-test.allthethings()-t-shirt-(red)").click()
browser.find_element_by_xpath("//*[@class='shopping_cart_link']").click()
browser.find_element_by_id("checkout").click()
browser.find_element_by_id("first-name").send_keys("Ani")
browser.find_element_by_id("last-name").send_keys("Ter-Markosyan")
browser.find_element_by_id("postal-code").send_keys("0033")
browser.find_element_by_id("continue").click()
inventory_prices = browser.find_elements_by_xpath("//*[@class = 'inventory_item_price']")
list_of_prices = []

for i in range (len(inventory_prices)):
    list_of_prices.append((float(inventory_prices[i].text[1:6])))
summary = sum(list_of_prices)
item_total_price = browser.find_element_by_xpath("//*[@class = 'summary_subtotal_label']").text[13:19]
if summary == float(item_total_price):
    print("Test case is passed.")

#Tax calculation
item_total_price = browser.find_element_by_xpath("//*[@class = 'summary_subtotal_label']").text[13:19]
tax = browser.find_element_by_xpath("//*[@class = 'summary_tax_label']").text[6:11]
total = browser.find_element_by_xpath("//*[@class = 'summary_total_label']").text[8:14]

if float(item_total_price) + float(tax) == float(total):
    print("Total price test is passed.")
