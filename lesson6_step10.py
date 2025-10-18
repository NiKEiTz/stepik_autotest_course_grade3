from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
fake = Faker()

try:
    firstNameInput = browser.find_element(By.TAG_NAME, "input").send_keys(f"{fake.first_name()}")
    lastNameInput = browser.find_element(By.CLASS_NAME, "form-control.second").send_keys(f"{fake.last_name()}")
    lastNameInput = browser.find_element(By.XPATH, "//div[3]/input").send_keys(f"{fake.email()}")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

