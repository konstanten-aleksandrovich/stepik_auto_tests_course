from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    o='''Введите 1 или 2 для  проверки страницы
    1 - "http://suninjuly.github.io/registration1.html"
    2 - "http://suninjuly.github.io/registration2.html
    Ведите цифру  1 или 2 и нажмите ENTER :"'''
    link = f"http://suninjuly.github.io/registration{input(o)}.html"
    browser = webdriver.Chrome()
    browser.get(link)
    n = ['Input your first name', 'Input your last name', 'Input your email']
    [browser.find_element(By.XPATH, f"//input[@placeholder='{j}'  and @required]").send_keys("Мой ответ") for j in n]
    ...

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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()