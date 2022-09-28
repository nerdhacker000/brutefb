from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://facebook.com/login")
email = browser.find_element(By.NAME, "email")
password = browser.find_element(By.NAME, "pass")
button = browser.find_element(By.NAME, "submit")
email.send_keys("marccarthy3@gmail.com")
password.send_keys(". 1234@ duah.com")
button.click()
if assert browser.title == "Facebook":
	print("Yes")
