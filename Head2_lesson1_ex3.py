import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link1 = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    find_x = browser.find_element(By.ID, "num1")
    x = find_x.text
    find_y = browser.find_element(By.ID, "num2")
    y = find_y.text
    ans=int(x)+int(y)


    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{ans}"]').click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()