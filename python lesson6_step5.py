from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = " http://suninjuly.github.io/find_link_text"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()
    browser.find_element(By.NAME, 'first_name').send_keys("Ivan")
    browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    browser.find_element(By.NAME, 'firstname').send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(3000)
