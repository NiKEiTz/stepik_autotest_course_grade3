from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
if button:
    butt = browser.find_element(By.CLASS_NAME,"btn")
    butt.click()

    x=browser.find_element(By.ID,"input_value").text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)


    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    print(browser.switch_to.alert.text.split(': ')[-1])