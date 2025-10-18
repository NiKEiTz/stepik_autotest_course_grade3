from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);")

x = browser.find_element(By.ID,"input_value").text
y=calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
option1.click()

radiobutton = browser.find_element(By.CSS_SELECTOR,'[value="robots"]')
radiobutton.click()

button.click()
time.sleep(30)