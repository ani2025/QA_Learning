#This test case was created by Ani Ter-Markosyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

chrome_options = Options()
browser = webdriver.Chrome(executable_path = r"C:\Users\VG\Desktop\webdriver\chromedriver_win32\\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
browser.implicitly_wait(3)

def test_standard_user():
    login = browser.find_element_by_xpath("//*[@id ='login_credentials']").text.split()[3]
    browser.find_element_by_id("user-name").send_keys(login)
    password = browser.find_element_by_css_selector(".login_password").text.split()[4]
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login-button").click()
    browser.implicitly_wait(3)
    actualUrl = browser.current_url
    expectedUrl = "https://www.saucedemo.com/inventory.html"
    assert actualUrl == expectedUrl, ("Test case 1 is failed.")
    browser.quit()


def test_locked_out_user():
    login = browser.find_element_by_xpath("//*[@id ='login_credentials']").text.split()[4]
    browser.find_element_by_id("user-name").send_keys(login)
    password = browser.find_element_by_css_selector(".login_password").text.split()[4]
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login-button").click()
    browser.implicitly_wait(3)
    error = browser.find_element_by_xpath("//*[@data-test = 'error']").text
    assert error == "Epic sadface: Sorry, this user has been locked out.", ("Test case 2 is failed")
    browser.quit()

def test_problem_user():
  
    login = browser.find_element_by_xpath("//*[@id ='login_credentials']").text.split()[5]
    browser.find_element_by_id("user-name").send_keys(login)
    password = browser.find_element_by_css_selector(".login_password").text.split()[4]
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login-button").click()
    browser.implicitly_wait(3)
    same_img_quantity = len(browser.find_elements_by_xpath("//*[@src = '/static/media/sl-404.168b1cce.jpg']"))
    items_quantity = len(browser.find_elements_by_xpath("//*[@class = 'inventory_item_name']"))
    assert same_img_quantity == items_quantity, ("Test case 3 is failed ")
    browser.quit()

# def test_performance_glitch_user():
