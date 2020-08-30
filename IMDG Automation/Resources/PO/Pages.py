from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import autoit
import datetime

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

from Locators import Locators
from TestData import TestData

class BasePage():
    """
    This class is the parent class for all the pages in IMDA iCheck.
    It contains all common elements and functionalities available to all pages.
    """

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # this function performs Back action by sending Escape key to locator is passed
    def back(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ESCAPE)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()


    # # this function perform upload document or file on web element whose locator and the file path is passed to it.
    # def upload(self, by_locator, by_path_file):
    #     self.wait_time(1)
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     AC(self.driver).move_to_element(element).click().perform()
    #     handle = "[CLASS:#32770; TITLE:Open]"
    #     autoit.win_wait(handle, 15)
    #     autoit.control_set_text(handle, "Edit1", by_path_file)
    #     autoit.control_click(handle, "Button1")

    # this function perform upload document or file on web element whose locator and the file path is passed to it.
    def upload(self, by_locator, by_path_file):
        self.wait_time(1)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        element.send_keys(by_path_file)

    # this function perform remove uploaded document and check the modal has been closed.
    def remove(self, by_locator):
        self.is_clickable(by_locator)
        self.click(by_locator)
        self.click(Locators.MODAL_DELETE_BUTTON)
        #Wait until Modal closed
        try:
            WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located(Locators.MODAL_DELETE_BUTTON))
        except TimeoutError:
            pass

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        try:
            web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            assert web_element.text == element_text
            return True
        except AssertionError:
            raise AssertionError(web_element.text + " is not equal as " + element_text)
            return False

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function get text from a web element whose locator is passed to it.
    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is clickable or not and returns
    # web element if it is enabled
    def is_clickable(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout trying to find {} element".format(by_locator))
            return False

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout trying to determine the visibility of {} element".format(by_locator))
            return False

    # this function similar to is_visible function but longer time is added since it should be used to check
    # the completion of uploading process. this function also returns true or false depending upon its visibility
    def is_visible_long(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 200).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout when trying to find {} element".format(by_locator))
            return False

    # this function would make the web wait for a specific time
    def wait_time(self, number):
        sleep(number)

    # this function capture a screenshot and save the file with date stamp as the file name
    def take_screenshot(self):
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = date_stamp + ".png"
        self.driver.save_screenshot(file_name)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        AC(self.driver).move_to_element(element).click().perform()

class LoginPage(BasePage):
    """IMDA iCheck Login Page"""

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self):
        # this function inputs user name and the respective password then click Login button
        self.enter_text(Locators.INPUT_USERNAME, TestData.USER_NAME)
        self.enter_text(Locators.INPUT_PASSWORD, TestData.USER_PASSWORD)
        self.click(Locators.LOGIN_BUTTON)

    def login_wrong_password(self):
        # this function inputs existing user name but wrong password then click Login button
        self.enter_text(Locators.INPUT_USERNAME, TestData.USER_NAME)
        self.enter_text(Locators.INPUT_PASSWORD, TestData.WRONG_USER_PASSWORD)
        self.click(Locators.LOGIN_BUTTON)

    def login_wrong_user(self):
        # this function inputs non-existing user name then click Login button
        self.enter_text(Locators.INPUT_USERNAME, TestData.WRONG_USER_NAME)
        self.enter_text(Locators.INPUT_PASSWORD, TestData.WRONG_USER_PASSWORD)
        self.click(Locators.LOGIN_BUTTON)

class HomePage(BasePage):
    """IMDA iCheck Home Page"""
    def __init__(self, driver):
        super().__init__(driver)

    def create_application(self):
        self.click(Locators.CREATE_NEW_APPLICATION)

    def claim_officer_role(self):
        self.click(Locators.CLAIM_OFFICER_ROLE)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

    def edit_application(self):
        self.is_clickable((Locators.CLAIM_APPLICATION_ROW_2))
        self.click(Locators.CLAIM_APPLICATION_ROW_2)

    def sort_by_latest(self):
        self.is_clickable(Locators.SORT_BY_INPUT)
        self.click(Locators.SORT_BY_INPUT)
        self.enter_text(Locators.SORT_BY_INPUT, TestData.LATEST)
        self.enter_text(Locators.SORT_BY_INPUT, Keys.ENTER)
        self.click(Locators.APPLY_FILTER_BUTTON)
        self.wait_time(1)

    def sort_by_oldest(self):
        self.is_clickable(Locators.SORT_BY_INPUT)
        self.click(Locators.SORT_BY_INPUT)
        self.enter_text(Locators.SORT_BY_INPUT, TestData.OLDEST)
        self.enter_text(Locators.SORT_BY_INPUT, Keys.ENTER)
        self.click(Locators.APPLY_FILTER_BUTTON)
        self.wait_time(1)

    def logout(self):
        self.click(Locators.LOGOUT_BUTTON)

    def verify_application(self):
        self.wait_time(1)
        self.click(Locators.CLAIM_APPLICATION_ROW_2)

class CreateEditApplicationPage(BasePage):
    """IMDA iCheck Create and Edit Application Page"""
    def __instancecheck__(self, driver):
        super().__init__(driver)

    def submit_application(self):
        self.click(Locators.SUBMIT_BUTTON)

    def back_to_application_list(self):
        self.click(Locators.BACK_TO_APPLICATION_BUTTON)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

    # --- Functions to upload document for each required document ---
    def upload_document(self):
        locators_path_and_success_icon = [[Locators.UPLOAD_NRIC_BUTTON, TestData.NRIC_PATH, Locators.NRIC_SUCCESS_ICON], [Locators.UPLOAD_INVOICE_BUTTON, TestData.INVOICE_PATH, Locators.INVOICE_SUCCESS_ICON],
                     [Locators.UPLOAD_ATTENDANCE_BUTTON, TestData.ATTENDANCE_PATH, Locators.ATTENDANCE_SUCCESS_ICON], [Locators.UPLOAD_SKILLSFUTURE_BUTTON, TestData.SKILLSFUTURE_PATH, Locators.SKILLSFUTURE_SUCCESS_ICON],
                     [Locators.UPLOAD_CERT_COMPLETION_BUTTON, TestData.CERT_COMPLETION_PATH, Locators.CERT_COMPLETION_SUCCESS_ICON], [Locators.UPLOAD_RECEIPT_BUTTON, TestData.RECEIPT_PATH, Locators.RECEIPT_SUCCESS_ICON],
                     [Locators.UPLOAD_DCA_BUTTON, TestData.DCA_PATH, Locators.DCA_SUCCESS_ICON], [Locators.UPLOAD_EXAM_RESULT_BUTTON, TestData.EXAM_RESULT_PATH, Locators.EXAM_RESULT_SUCCESS_ICON],
                     [Locators.UPLOAD_FORM_1_BUTTON, TestData.FORM_1_PATH, Locators.FORM_1_SUCCESS_ICON], [Locators.UPLOAD_FINAL_CERT_BUTTON, TestData.FINAL_CERT_PATH, Locators.FINAL_CERT_SUCCESS_ICON],
                     [Locators.UPLOAD_PROOF_MATRICULATION_BUTTON, TestData.PROOF_MATRICULATION_PATH, Locators.PROOF_MATRICULATION_SUCCESS_ICON]]

        for locators in locators_path_and_success_icon:
            self.upload(locators[0], locators[1])
            self.is_visible_long(locators[2])

    # --- Functions to remove document for each required documents ---
    def remove_document(self):
        locators_and_success_icon = [[Locators.REMOVE_NRIC_BUTTON, Locators.NRIC_SUCCESS_ICON], [Locators.REMOVE_INVOICE_BUTTON, Locators.INVOICE_SUCCESS_ICON],
                     [Locators.REMOVE_ATTENDANCE_BUTTON, Locators.ATTENDANCE_SUCCESS_ICON], [Locators.REMOVE_SKILLSFUTURE_BUTTON, Locators.SKILLSFUTURE_SUCCESS_ICON],
                     [Locators.REMOVE_CERT_COMPLETION_BUTTON, Locators.CERT_COMPLETION_SUCCESS_ICON], [Locators.REMOVE_RECEIPT_BUTTON, Locators.RECEIPT_SUCCESS_ICON],
                     [Locators.REMOVE_DCA_BUTTON, Locators.DCA_SUCCESS_ICON], [Locators.REMOVE_EXAM_RESULT_BUTTON, Locators.EXAM_RESULT_SUCCESS_ICON],
                     [Locators.REMOVE_FORM_1_BUTTON, Locators.FORM_1_SUCCESS_ICON], [Locators.REMOVE_FINAL_CERT_BUTTON, Locators.FINAL_CERT_SUCCESS_ICON],
                     [Locators.REMOVE_PROOF_MATRICULATION_BUTTON, Locators.PROOF_MATRICULATION_SUCCESS_ICON]]

        for locators in locators_and_success_icon:
            self.remove(locators[0])
            self.is_visible(locators[1])

    # this function opens document review and checks if both document title that clicked and viewed are same
    def view_document(self):
        uploaded_document_locator = [Locators.NRIC_VIEWER, Locators.INVOICE_VIEWER, Locators.ATTENDANCE_VIEWER,
                                     Locators.SKILLSFUTURE_VIEWER, Locators.CERT_COMPLETION_VIEWER, Locators.RECEIPT_VIEWER,
                                     Locators.DCA_VIEWER, Locators.EXAM_RESULT_VIEWER, Locators.FORM_1_VIEWER,
                                     Locators.FINAL_CERT_VIEWER, Locators.PROOF_MATRICULATION_VIEWER]

        for locator in uploaded_document_locator:
            self.is_clickable(locator)
            document_name = self.get_text(locator)
            self.click(locator)
            self.is_visible(Locators.PDF_VIEWER_SCROLL_CLASS)
            pdf_viewer_title = self.get_text(Locators.PDF_VIEWER_DOCUMENT_TITLE)
            try:
                assert document_name == pdf_viewer_title
            except AssertionError:
                print(document_name)
                print(pdf_viewer_title)
            self.hover_to_click(Locators.APP_NAME)
            # Wait until Modal closed
            try:
                WebDriverWait(self.driver, 2).until_not(EC.presence_of_element_located(Locators.PDF_VIEWER_SCROLL_CLASS))
            except TimeoutException:
                pass

class ApplicationDetailPage(BasePage):
    """IMDA iCheck Application Detail Page"""
    def __instancecheck__(self, driver):
        super().__init__(driver)

    def reject_application(self):
        self.wait_time(1)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_1)
        self.click(Locators.CLAIM_APPLICATION_ROW_1)
        self.is_visible(Locators.VERIFY_APPLICATION_BUTTON)
        self.is_clickable(Locators.REJECT_APPLICATION_BUTTON)
        self.click(Locators.REJECT_APPLICATION_BUTTON)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)

    def verify_application(self):
        self.wait_time(1)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_1)
        self.click(Locators.CLAIM_APPLICATION_ROW_1)
        self.is_visible(Locators.VERIFY_APPLICATION_BUTTON)
        self.is_clickable(Locators.REJECT_APPLICATION_BUTTON)
        self.click(Locators.VERIFY_APPLICATION_BUTTON)
        self.is_clickable(Locators.CLAIM_APPLICATION_ROW_2)
