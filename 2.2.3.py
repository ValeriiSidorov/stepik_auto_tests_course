from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    sum = (int(x)+int(y))
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(sum)) # ищем элемент с текстом из переменной Z
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    
    