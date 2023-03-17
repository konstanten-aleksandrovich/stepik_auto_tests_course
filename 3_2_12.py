import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def f(n):
    o = '''Введите 1 или 2 для  проверки страницы
    1 - "http://suninjuly.github.io/registration1.html"
    2 - "http://suninjuly.github.io/registration2.html
    Ведите цифру  1 или 2 и нажмите ENTER :"'''
    link = f"http://suninjuly.github.io/registration{n}.html"
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
    t=welcome_text_elt.text
    print(t)
    return t


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        assert f(1)=='Congratulations! You have successfully registered!',''
    def test_abs2(self):
        assert f(2)=='Congratulations! You have successfully registered!',''



if __name__ == "__main__":
    pytest.main()
