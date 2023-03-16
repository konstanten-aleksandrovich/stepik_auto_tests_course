from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time,math
with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    while browser.find_element('id','price').text!='$100':
        #print(browser.find_element('id','price').text)
        pass

    browser.find_element(By.ID, "book").click()


    # browser.find_element(By.TAG_NAME,'button').click()
    # browser.switch_to.window(browser.window_handles[1])
    x=browser.find_element('id','input_value').text
    browser.find_element('id','answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element('id','solve').click()

    time.sleep(100)
