from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#driver = webdriver.Chrome()


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver









'''
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

search_text = (By.ID, 'kw')
WebDriverWait(driver,10).until(EC.visibility_of_element_located (search_text))

driver.find_element(By.ID, 'kw').send_keys('aa')
print(search_text)


time.sleep(2)
driver.execute_script('window.open()')

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])

driver.get('http://www.zhifu.com')
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.get("http://www.weibo.com")
time.sleep(2)


driver.close()
driver.quit()
'''