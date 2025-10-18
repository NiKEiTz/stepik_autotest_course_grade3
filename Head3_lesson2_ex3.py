import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):

        link1 = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div .first_block .first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div .first_block .second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div .first_block .third_class input")
        input3.send_keys("myemail@gmail.com")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "We can't register!")
        browser.quit()
        
    def test_abs2(self):
        link2 = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.CSS_SELECTOR, "div .first_block .first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div .first_block .second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div .first_block .third_class input")
        input3.send_keys("myemail@gmail.com")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "We can't register!")
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()