import datetime
import inspect
import os
import sys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Locators import Locators
from ScriptData import ScriptData


class BasePage():
    """
    This class is the parent class for all the pages in iMatch.
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

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        try:
            web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            assert web_element.text == element_text
            return True
        except AssertionError:
            raise AssertionError(web_element.text + " is not equal as " + element_text)

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

    # this function checks if the web element whose locator has been passed to it, is clickable and returns
    # web element if it is enabled
    def is_clickable(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout trying to find {} element".format(by_locator))

    # this function checks if the web element whose locator has been passed to it, is not clickable and returns
    # web element if it is enabled
    def is_not_clickable(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    # this function checks if the web element whose locator has been passed to it, is visible and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout trying to determine the visibility of {} element".format(by_locator))

    # this function checks if the web element whose locator has been passed to it, is not and returns
    # true or false depending upon its visibility.
    def is_not_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    # this function similar to is_visible function but longer time is added since it should be used to check
    # the completion of uploading process. this function also returns true or false depending upon its visibility
    def is_visible_long(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 200).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            raise TimeoutException(msg="Timeout when trying to find {} element".format(by_locator))

    # this function would make the web wait for a specific time
    def wait_time(self, number):
        sleep(number)

    # this function capture a screenshot and save the file with date stamp as the file name
    def take_screenshot(self):
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = date_stamp + ".png"
        self.driver.save_screenshot(file_name)

    # this function moves the mouse pointer over a web element whose locator has been passed to it
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        AC(self.driver).move_to_element(element).perform()

    # this function moves the mouse pointer over a web element whose locator has been passed to it and click the element.
    def hover_to_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        AC(self.driver).move_to_element(element).click().perform()

    # this function moves the mouse pointer over a web element whose locator has been passed to it
    # and further click an element that become visible
    def hover_to_click_element(self, by_locator, by_button_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        AC(self.driver).move_to_element(element).perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_button_locator)).click()

    # this function moves the mouse pointer over a specific coordinates and click it
    def hover_to_coordinates(self, coordinate_x, coordinate_y):
        AC(self.driver).move_by_offset(coordinate_x, coordinate_y).click().perform()

    # this function scroll the page to the passed element
    def scroll_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.location_once_scrolled_into_view


class LoginPage(BasePage):
    """iMatch Login Page"""

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(ScriptData.BASE_URL)

    def login(self):
        # this function inputs user name and the respective password then click Login button
        self.is_clickable(Locators.LOGIN_BUTTON_HEADER)
        self.click(Locators.LOGIN_BUTTON_HEADER)
        self.is_clickable(Locators.INPUT_USERNAME)
        self.enter_text(Locators.INPUT_USERNAME, ScriptData.USER_NAME)
        self.enter_text(Locators.INPUT_PASSWORD, ScriptData.USER_PASSWORD)
        self.click(Locators.LOGIN_BUTTON)
        self.is_visible(Locators.SEARCH_PAGE_BUTTON)


class SearchPage(BasePage):
    """iMatch Search Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def select_document_subtype(self, by_dropdown_locator, by_subtype):
        # this function select a document subtype inside a dropdown menu
        self.is_clickable(by_dropdown_locator)
        # self.scroll_to(by_dropdown_locator)
        self.click(by_dropdown_locator)
        # self.is_clickable(by_subtype)
        self.scroll_to(by_subtype)
        self.click(by_subtype)
        self.is_visible_long(Locators.SEARCH_TABLE)

    def total_documents_number(self):
        # this function get the total numbers of the document from search page size
        # and return the total number
        try:
            self.is_visible(Locators.SEARCH_PAGE_SIZE)
            search_result_text = self.get_text(Locators.SEARCH_PAGE_SIZE)
            text_split = search_result_text.split()
            return text_split[5]
        except TimeoutException:
            return 0

    def select_start_date(self, by_datepicker_locator, by_date):
        # this function select a given date from datepicker
        self.scroll_to(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)
        self.is_clickable(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)
        self.click(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)

        # click the date picker
        self.scroll_to(by_datepicker_locator)
        self.is_clickable(by_datepicker_locator)
        self.click(by_datepicker_locator)

        # selecting the date
        date_list = by_date.split('-')
        select_month = self.driver.find_element_by_xpath(Locators.MONTH_DATEPICKER)
        for option in select_month.find_elements_by_tag_name('option'):
            if option.text == date_list[1]:
                option.click()
                break

        select_year = self.driver.find_element_by_xpath(Locators.YEAR_DATEPICKER)
        for option in select_year.find_elements_by_tag_name('option'):
            if option.text == date_list[2]:
                option.click()
                break

        days = self.driver.find_elements_by_xpath(Locators.DAY_DATEPICKER)
        date = int(date_list[0]) - 1
        days[date].click()

    def select_end_date(self, by_datepicker_locator, by_date):
        # this function select a given date from datepicker
        self.scroll_to(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)
        self.is_clickable(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)
        self.click(Locators.DOCUMENT_DATE_DROPDOWN_BUTTON)

        # click the date picker
        self.scroll_to(by_datepicker_locator)
        self.is_clickable(by_datepicker_locator)
        self.click(by_datepicker_locator)

        # selecting the date
        date_list = by_date.split('-')
        select_month = self.driver.find_element_by_xpath(Locators.MONTH_DATEPICKER)
        for option in select_month.find_elements_by_tag_name('option'):
            if option.text == date_list[1]:
                option.click()
                break

        select_year = self.driver.find_element_by_xpath(Locators.YEAR_DATEPICKER)
        for option in select_year.find_elements_by_tag_name('option'):
            if option.text == date_list[2]:
                option.click()
                break

        days = self.driver.find_elements_by_xpath(Locators.DAY_DATEPICKER)
        days[0].click()

        self.wait_time(5)

    def medical_invoices_dp_scraping(self):
        # This function scraping necessary data point such as document name,
        # receipt number, claim amount, and receipt date then append it to
        # a list
        dp = []
        document_header = self.get_text(Locators.DOCUMENT_NAME_HEADER)
        # splitting the document header to obtain the document name
        document_name = document_header.split(": ")
        dp.append(document_name[1])
        # obtain the data points
        data_points = self.driver.find_elements_by_xpath(Locators.MED_INVOICES_DP)
        for data_point in data_points:
            dp.append(str(data_point.text))
        return dp

    @staticmethod
    def append_list(list_1, list_2, number):
        # This function append members from list_2 to each member of list_1
        i = 0
        while i < number:
            list_1[i].append(list_2[i])
            i = i + 1