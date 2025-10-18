from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "button")
    input1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x=browser.find_element(By.ID,"input_value").text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)


    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
