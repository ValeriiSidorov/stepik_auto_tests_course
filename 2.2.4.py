from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

alert = browser.switch_to.alert
time.sleep(10)
alert.accept()

browser.quit()

