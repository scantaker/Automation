from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
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
        self.assertTrue(self.homePage.is_visible(Locators.LOGIN_PAGE_TITLE))

    def test_003_login_with_wrong_password(self):
        # Instantiate an object of LoginPage class. When the constructor of LoginPage
        # is called, it opens up the browser and navigates to Login Page of IMDA iCheck
        # then login using provided credential but with wrong password
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_wrong_password()

        #Asserting the Login alert is visible and its text
        self.assertTrue(self.loginPage.is_visible(Locators.LOGIN_ALERT))
        self.assertTrue(self.loginPage.assert_element_text(Locators.LOGIN_ALERT, TestData.LOGIN_ALERT_TEXT))

    def test_004_login_with_not_existed_user(self):
        # Instantiate an object of LoginPage class. When the constructor of LoginPage
        # is called, it opens up the browser and navigates to Login Page of IMDA iCheck
        # then login using non existing credential but with wrong password
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_wrong_user()

        # Asserting the Login alert is visible and its text
        self.assertTrue(self.loginPage.is_visible(Locators.LOGIN_ALERT))
        self.loginPage.assert_element_text(Locators.LOGIN_ALERT, TestData.LOGIN_ALERT_TEXT)

class IMDGGrantApplicantTest(IMDGBaseTest):
    def setUp(self):
        super().setUp()

    def test_001_create_application_submit_uploaded_document(self):
        #Instantiate an object of LoginPage class and login using provided credential
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        #Instantiate an object of HomePage class and go to Create Application page
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.create_application()

        #Instantiate an object of CreateApplicationPage class and start to upload documents
        self.createApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload required documents and assert a checkmark when the upload process is finished
        self.createApplicationPage.upload_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.createApplicationPage.is_visible(locator))

        #Submit the application
        self.createApplicationPage.submit_application()

        #Instantiate an object of HomePage class and assert a toaster appear
        self.homePage = HomePage(self.createApplicationPage.driver)
        self.assertTrue(self.homePage.is_enabled(Locators.NOTIFICATION_TOASTER))

    def test_002_create_application_remove_uploaded_document(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.create_application()
        self.createApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload required documents and assert a checkmark when the upload process is finished
        self.createApplicationPage.upload_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.createApplicationPage.is_visible(locator))

        #Remove the uploaded documents & assert the checkmark disappear from its respective document
        self.createApplicationPage.remove_document()
        for locator in checkmark_icon_locators:
            self.assertFalse(self.createApplicationPage.is_visible(locator))

    def test_003_create_application_view_uploaded_document(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.create_application()
        self.createApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload required documents and assert a checkmark when the upload process is finished
        self.createApplicationPage.upload_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.createApplicationPage.is_visible(locator))

        # View uploaded documents and assert the checkmarks when all the view process is finished
        self.createApplicationPage.view_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.createApplicationPage.is_visible(locator))

    def test_004_edit_application_remove_document(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        # Instantiate an object of HomePage class and go to Edit Application page of the first application
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.edit_application()

        #Instantiate an object of CreateEditApplicationPage class and remove all the documents
        self.editApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Remove the uploaded documents & assert the checkmark disappear from its respective document
        self.editApplicationPage.remove_document()
        for locator in checkmark_icon_locators:
            self.assertFalse(self.editApplicationPage.is_visible(locator))

        #Return to Home page and assert the applicant name in the is empty
        self.editApplicationPage.back_to_application_list()
        self.assertTrue(self.editApplicationPage.assert_element_text(Locators.CLAIM_APPLICATION_ROW_2_APPLICANT_NAME, TestData.EMPTY_TEXT))

    def test_005_edit_application_upload_document(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        # Instantiate an object of HomePage class and go to Edit Application page of the first application
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.edit_application()

        #Instantiate an object of CreateEditApplicationPage class and remove all the documents
        self.editApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload reqired documents and assert a checkmark when the upload process is finished
        ## NRIC
        self.editApplicationPage.upload_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.editApplicationPage.is_visible(locator))

        #Return to Home page and assert the applicant name in the first row is not empty
        self.editApplicationPage.back_to_application_list()
        self.assertFalse(self.editApplicationPage.assert_element_text(Locators.CLAIM_APPLICATION_ROW_2_APPLICANT_NAME, TestData.EMPTY_TEXT))

    def test_006_edit_application_view_document(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        # Instantiate an object of HomePage class and go to Edit Application page of the first application
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.edit_application()

        #Instantiate an object of CreateEditApplicationPage class and remove all the documents
        self.editApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # View uploaded documents and assert the checkmarks when all the view process is finished
        self.editApplicationPage.view_document()
        for locator in checkmark_icon_locators:
            self.assertTrue(self.editApplicationPage.is_visible(locator))

class IMDGClaimOfficerTest(IMDGBaseTest):
    def setUp(self):
        super().setUp()

    def test_001_login_with_claim_officer_role(self):
        #Instantiate an object of LoginPage class and login using provided credential
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        #Instantiate an object of HomePage class and go to Claim Officer role
        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.claim_officer_role()

        # Assert Claim Applications table is visible and the applications with Pending Approval status
        # are clickable
        self.assertTrue(self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2_APPLICANT_NAME))
        #Assert Create New Application is not visible
        self.assertFalse(self.homePage.is_visible(Locators.CREATE_NEW_APPLICATION))

    def test_002_click_pending_application(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.claim_officer_role()
        self.assertTrue(self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2))

        #Click application with 'Pending Approval' status and assert redirection to Application Detail page
        self.homePage.verify_application()
        self.assertTrue(self.homePage.is_visible(Locators.VERIFY_APPLICATION_BUTTON))

    def test_003_reject_application(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.create_application()
        self.createApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload required documents and check a checkmark when the upload process is finished
        self.createApplicationPage.upload(Locators.UPLOAD_NRIC_BUTTON, TestData.NRIC_PATH)
        self.createApplicationPage.is_visible_long(Locators.NRIC_SUCCESS_ICON)

        #Submit the application
        self.createApplicationPage.submit_application()

        #Instantiate an object of HomePage class and check a toaster appear
        self.homePage = HomePage(self.createApplicationPage.driver)
        self.homePage.is_enabled(Locators.NOTIFICATION_TOASTER)
        self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

        #Go to Claim Officer role and sort the claim list by the latest entries
        self.homePage.claim_officer_role()
        self.homePage.sort_by_latest()
        self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_1)

        # Go to the latest application details, instantiate an object of
        # ApplicationPage class and reject the application then assert
        # it has been rejected
        self.applicationDetailPage = ApplicationDetailPage(self.homePage.driver)
        self.applicationDetailPage.reject_application()
        self.applicationDetailPage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

        self.homePage = HomePage(self.applicationDetailPage.driver)
        self.homePage.sort_by_latest()
        self.assertTrue(self.homePage.assert_element_text(Locators.CLAIM_APPLICATION_ROW_1_STATUS, TestData.STATUS_REJECTED))

    def test_004_verify_application(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

        self.homePage = HomePage(self.loginPage.driver)
        self.homePage.create_application()
        self.createApplicationPage = CreateEditApplicationPage(self.homePage.driver)

        # Upload required documents and check a checkmark when the upload process is finished
        self.createApplicationPage.upload(Locators.UPLOAD_NRIC_BUTTON, TestData.NRIC_PATH)
        self.createApplicationPage.is_visible_long(Locators.NRIC_SUCCESS_ICON)

        #Submit the application
        self.createApplicationPage.submit_application()

        #Instantiate an object of HomePage class and check a toaster appear
        self.homePage = HomePage(self.createApplicationPage.driver)
        self.homePage.is_enabled(Locators.NOTIFICATION_TOASTER)
        self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

        #Go to Claim Officer role and sort the claim list by the latest entries
        self.homePage.claim_officer_role()
        self.homePage.sort_by_latest()
        self.homePage.is_clickable(Locators.CLAIM_APPLICATION_ROW_1)

        # Go to the latest application details, instantiate an object of
        # ApplicationPage class and verify the application then assert
        # it has been verified
        self.applicationDetailPage = ApplicationDetailPage(self.homePage.driver)
        self.applicationDetailPage.verify_application()
        self.applicationDetailPage.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

        self.homePage = HomePage(self.applicationDetailPage.driver)
        self.homePage.sort_by_latest()
        self.assertTrue(self.homePage.assert_element_text(Locators.CLAIM_APPLICATION_ROW_1_STATUS, TestData.STATUS_VERIFIED))


if __name__ == "__main__":
    # --- Run all the test cases ---
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        template= "../Templates/template.html",
        report_title= "Chrome UI Test",
        combine_reports=True,
        report_name="iCheck_Automation_Report",
        open_in_browser=True,
        output=parentdir + '\Reports'))

    # # --- Run for selected test cases only ---
    # suite = unittest.TestSuite()
    # ## Add test cases which want to be run
    # suite.addTest(IMDGLoginTest("test_001_login_with_correct_credential"))
    # suite.addTest(IMDGLoginTest("test_002b_login_then_logout"))
    # suite.addTest(IMDGClaimOfficerTest("test_004_verify_application"))
    #
    # runner = HtmlTestRunner.HTMLTestRunner(
    #     template="../Templates/template.html",
    #     report_title="Chrome UI Test",
    #     combine_reports=True,
    #     report_name="iCheck_Automation_Report",
    #     open_in_browser=True,
    #     output=parentdir + '\Reports')
    #
    # runner.run(suite)
