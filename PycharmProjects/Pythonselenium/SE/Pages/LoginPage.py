from BasePage import BasePage
import Locators
import TestData
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def input_username(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Locators.TEXTBOX_USERNAME))
        print('webdriverwait not ok')
        self.driver.find_element_by_name(Locators.TEXTBOX_USERNAME[1]).send_keys(TestData.FIRST_USERNAME)
        print('sendkey ok')