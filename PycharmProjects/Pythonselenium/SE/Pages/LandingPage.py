from BasePage import BasePage
import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class LandingPage(BasePage):
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_BUTTON))
        self.driver.find_element_by_link_text(Locators.BUTTON_BUTTON[1]).click()
