import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link1 = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    tres = browser.find_element(By.ID, "treasure")
    x = tres.get_attribute("valuex")
    y=calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR,'[value="robots"]')
    radiobutton.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()