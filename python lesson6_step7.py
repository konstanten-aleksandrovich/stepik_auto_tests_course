from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    [i.send_keys("Мой ответ") for i in browser.find_elements(By.TAG_NAME, "input")]
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(3000)
