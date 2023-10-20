from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    
    #Отправляем резудьтат в поле вывода ответа
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    #Скроллим страницу на 100 пикселей вниз
    browser.execute_script("window.scrollBy(0, 100);")
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    