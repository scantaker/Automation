from LandingPage import LandingPage
import unittest
from selenium import webdriver
from LoginPage import LoginPage


class PoolsBaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()