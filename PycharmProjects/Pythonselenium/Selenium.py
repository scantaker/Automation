#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import  *
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://online.singaporepools.com/en/account#page_trx_history")
driver.maximize_window()

BUTTON_BUTTON = (By.LINK_TEXT, 'Login')

#driver.find_element_by_xpath('//*[@id="block-bean-mini-account"]/div/div/div/div/div/div/div/div/div/div/a[1]/button').click()
print(str(BUTTON_BUTTON))

'''
driver.maximize_window()
time.sleep(2)

#window handle
print(driver.current_window_handle)

newsButton = driver.find_element_by_link_text("hao123")
ActionChains(driver).click(newsButton).perform()

handles = driver.window_handles
print(driver.current_window_handle)
driver.switch_to.window(handles[1])
print(driver.current_window_handle)



#driver.find_element_by_id('kw').send_keys('sicai')

driver.find_element_by_css_selector('#kw').send_keys('sicai')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'v')

driver.find_element_by_css_selector('.s_ipt').send_keys('sicai2')
driver.find_element_by_css_selector('input').send_keys('sicai3')
driver.find_element_by_css_selector("input[id='kw'] [name = 'wd']")
driver.find_element_by_id('su').click()


settings = driver.find_element_by_link_text('更多')
print(settings)

#driver.get_screenshot_as_file("/Users/zhangsicai/Desktop/test.png")
ActionChains(driver).move_to_element(settings).perform()


driver.close()
'''

#webfront=driver.find_element_by_link_text('Web 前端开发')
#webUI=driver.find_element_by_css_selector('html body.YaHei.index div.main div.main-container div.main-con-inner div.course-container.marginB30 div.ui-container.marginB30 div.ui-inner.clearfix div.ui-left a img.ui-img')

#webfront.click()

#webUI.click()

#webSearch=driver.find_element_by_css_selector('input[id=\'data-search\']')
#webSearch.send_keys('aa')
'''
webPM=driver.find_element_by_css_selector('img[alt="产品经理-CEO的学前班"]')
webPM.click()

def get_element_time(driver, time, func):
    return WebDriverWait(driver,time).until(func)

webQH = get_element_time(driver, 5, \
    lambda d: driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]'))


#webQH=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]')
ActionChains(driver).move_to_element(webQH).perform()



#switch to window
driver.window_handles
driver.current_window_handle
driver.switch_to_window(driver.window_handles[1])

driver.implicitly_wait()




class ExampleCase1(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = 3

    def test_add(self):
        self.assertEqual(self.a+self.b, 7)

if __name__== '__main__':
    reportTitle = 'my report'
    reportFile = '/Users/zhangsicai/Desktop/cc.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(ExampleCase1('test_add'))

    with open(reportFile, 'w+') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=reportTitle,description='aa')
        runner.run(testsuite)
        
'''

