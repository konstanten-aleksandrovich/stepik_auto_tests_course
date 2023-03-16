from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/find_xpath_form')
    [i.send_keys("Мой ответ") for i in browser.find_elements(By.TAG_NAME, "input")]
    browser.find_element(By.XPATH, "//*/button[@type='submit']").click()
    time.sleep(3000)
