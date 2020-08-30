from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HtmlTestRunner import HTMLTestRunner
from HtmlTestRunner.result import HtmlTestResult
import unittest
import datetime

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir+'\Resources')
sys.path.insert(0, parentdir+'\Resources\PO')

from Locators import Locators
from TestData import TestData
from PO import Pages
from Pages import LoginPage, HomePage, CreateEditApplicationPage, ApplicationDetailPage

checkmark_icon_locators = [Locators.NRIC_SUCCESS_ICON, Locators.INVOICE_SUCCESS_ICON, Locators.ATTENDANCE_SUCCESS_ICON,
                                   Locators.SKILLSFUTURE_SUCCESS_ICON, Locators.CERT_COMPLETION_SUCCESS_ICON, Locators.RECEIPT_SUCCESS_ICON,
                                   Locators.DCA_SUCCESS_ICON, Locators.EXAM_RESULT_SUCCESS_ICON, Locators.FORM_1_SUCCESS_ICON,
                                   Locators.FINAL_CERT_SUCCESS_ICON, Locators.PROOF_MATRICULATION_SUCCESS_ICON]

#Base class for the tests
class IMDGBaseTest(unittest.TestCase):
    """
    This class is the parent class for all the other tests
    It contains setUp and tearDown method that will be used for the other tests
    """

    def setUp(self):
        # Create a headless Chrome browser and disable security
        #op = webdriver.ChromeOptions()
        # op.add_argument('headless') --disabling it at this moment since it caused the test_login failed
        #op.add_argument('--allow-running-insecure-content')
        #op.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                date_stamp = str(datetime.datetime.now()).split('.')[0]
                date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
                name = "screenshot" + self.id() + date_stamp+ ".png"
                self.driver.get_screenshot_as_file(name)
                print(name)

        # close the browser window
        self.driver.quit()

class IMDGLoginTest(IMDGBaseTest):

    def setUp(self):
        super().setUp()

    def test_001_login_with_correct_credential(self):
        #Instantiate an object of LoginPage class. When the constructor of LoginPage
        #is called, it opens up the browser and navigates to Login Page of IMDA iCheck
        #then login using provided credential
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        #Assert that redirect to Home page with Extract name is visible at the page
        self.assertTrue(self.loginPage.is_visible(Locators.APP_NAME))

    @unittest.skip("Not first time login")
    def test_002a_first_time_login_then_logout(self):

        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        # Asserting that claim application list is not present
        self.homePage = HomePage(self.loginPage.driver)
        self.assertFalse(self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2))
        self.homePage.logout()

        #Asserting redirection to Login page with Login button is visible
        self.assertTrue(self.homePage.is_visible(Locators.LOGIN_PAGE_TITLE))

    def test_002b_login_then_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        self.homePage = HomePage(self.loginPage.driver)
        self.assertTrue(self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2))
        self.homePage.logout()

        #Asserting redirection to Login page with Login button is visible
        self.assertFalse(self.homePage.is_visible(Locators.LOGIN_PAGE_TITLE))

class IMDGNegativeLoginTest(IMDGBaseTest):

    def setUp(self):
        super().setUp()
            
    def test_001_login_with_wrong_password(self):
        # Instantiate an object of LoginPage class. When the constructor of LoginPage
        # is called, it opens up the browser and navigates to Login Page of IMDA iCheck
        # then login using provided credential but with wrong password
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_wrong_password()

        #Asserting the Login alert is visible and its text
        self.assertTrue(self.loginPage.is_visible(Locators.LOGIN_ALERT))
        self.assertTrue(self.loginPage.assert_element_text(Locators.LOGIN_ALERT, TestData.LOGIN_ALERT_TEXT))

    def test_002_login_with_not_existed_user(self):
        # Instantiate an object of LoginPage class. When the constructor of LoginPage
        # is called, it opens up the browser and navigates to Login Page of IMDA iCheck
        # then login using non existing credential but with wrong password
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_wrong_user()

        # Asserting the Login alert is visible and its text
        self.assertTrue(self.loginPage.is_visible(Locators.LOGIN_ALERT))
        self.assertFalse(self.loginPage.assert_element_text(Locators.LOGIN_ALERT, TestData.LOGIN_ALERT_TEXT))

if __name__ == "__main__":
    # # Run all the test cases
    # unittest.main(testRunner=HTMLTestRunner(
    #     template= "../Templates/template.html",
    #     report_title= "Chrome UI Test",
    #     combine_reports=True,
    #     report_name="iCheck_Automation_Report",
    #     open_in_browser=True,
    #     output=parentdir + '\Reports'))

    # Run for selected test cases only
    suite = unittest.TestSuite()
    suite.addTest(IMDGLoginTest("test_001_login_with_correct_credential"))
    suite.addTest(IMDGLoginTest("test_002b_login_then_logout"))
    suite.addTest(IMDGNegativeLoginTest("test_002_login_with_not_existed_user"))

    runner = HTMLTestRunner(
        template="../Templates/template.html",
        report_title="Chrome UI Test",
        combine_reports=True,
        report_name="iCheck_Automation_Report",
        open_in_browser=True,
        output=parentdir + '\Reports')

    runner.run(suite)
