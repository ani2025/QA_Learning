#This test case was created by Ani Ter-Markosyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })

browser = webdriver.Chrome(executable_path = r"C:\Users\VG\Desktop\webdriver\chromedriver_win32\\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
browser.find_element_by_id("user-name").send_keys("standard_user")
browser.find_element_by_id("password").send_keys("secret_sauce")
browser.find_element_by_id("login-button").click()
browser.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
browser.find_element_by_css_selector(".shopping_cart_link").click()
browser.find_element_by_id("checkout").click()
browser.find_element_by_id("first-name").send_keys("Ani")
browser.find_element_by_id("last-name").send_keys("Ter-Markosyan")
browser.find_element_by_id("postal-code").send_keys("0033")
browser.find_element_by_id("continue").click()
browser.find_element_by_id("finish").click()
if browser.find_element_by_xpath("//*[contains(@id,complete)]"):
    print("Test case is passed.")
else:
    print("Test case is failed.")