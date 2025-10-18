from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        # from selenium import webdriver
        # from selenium.webdriver.chrome.service import Service
        # # Укажи путь к драйверу
        # service = Service("C:/yandexdriver.exe")

        
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@example.com")
        
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

        return welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# Тестируем первую страницу (должна работать)
result1 = test_registration("http://suninjuly.github.io/registration2.html")
print(f"Result for registration1: {result1}")

# Тестируем вторую страницу (должна падать с ошибкой)
try:
    result2 = test_registration("http://suninjuly.github.io/registration2.html")
    print(f"Result for registration2: {result2}")
except Exception as e:
    print(f"Test for registration2 failed as expected: {e}")