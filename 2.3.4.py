from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    redir = webdriver.Chrome()
    redir.get("http://suninjuly.github.io/alert_redirect.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = redir.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    
    #Отправляем резудьтат в поле вывода ответа
    input1 = redir.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = redir.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    
    