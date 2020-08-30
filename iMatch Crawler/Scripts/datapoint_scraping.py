import os, sys, inspect
import pandas as pd
import datetime
from selenium import webdriver



# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
resourcedir = parentdir + '/Resources'
print(resourcedir)

# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, resourcedir)
sys.path.insert(0, parentdir + '/Resources/PageObjects')



from Locators import Locators
from Pages import LoginPage, SearchPage
from ScriptData import ScriptData

# Setup
driver = webdriver.Chrome(executable_path=ScriptData.CHROME_EXECUTABLE_PATH)
driver.maximize_window()

# Login
loginPage = LoginPage(driver)
loginPage.login()
loginPage.is_clickable(Locator.SEARCH_PAGE_BUTTON)

# Go to Search page
loginPage.click(Locator.SEARCH_PAGE_BUTTON)
loginPage.is_visible_long(Locator.SEARCH_TABLE)

# Instantiate an object of SearchPage class
searchPage = SearchPage(loginPage.driver)

# Selecting Medical Invoice document subtype
searchPage.select_document_subtype(Locator.SUBTYPE_DROPDOWN_BUTTON, Locator.SUBTYPE_MEDICAL_INVOICE_CHECK)
searchPage.is_visible_long(Locator.SEARCH_TABLE)

# Selecting a Start Date filter
searchPage.select_start_date(Locator.START_DATEPICKER, ScriptData.START_DATE)
searchPage.wait_time(3)
searchPage.select_end_date(Locator.END_DATEPICKER, ScriptData.END_DATE)

# Obtain the documents number
result_number = searchPage.total_documents_number()
print("Get {} document(s) from {} to {}.".format(result_number, ScriptData.START_DATE, ScriptData.END_DATE))

# Scraping the data points
if int(result_number) == 0:
    print("No data points scraped for given date.")
else:
    # result_number > 0
    # variables and list
    j = 0
    k = 0
    full_pagination_page = int(result_number) // 15
    last_page_document_number = int(result_number) % 15

    # Create empty lists of required data points of a
    # document subtype
    document_list = []
    # Change this list into respected data points of
    # a document subtype
    receipt_number_list = []
    claim_amount_list = []
    receipt_date_list = []

    dp_list = [document_list, receipt_number_list, claim_amount_list, receipt_date_list]

    # 0 < result_number <= 15
    if int(result_number) <= 15:
        i = 0
        # click the first document
        searchPage.is_clickable(Locator.FIRST_DOCUMENT_LOCATOR)
        searchPage.click(Locator.FIRST_DOCUMENT_LOCATOR)
        while i < int(result_number):
            searchPage.is_clickable(Locator.VALIDATE_BUTTON)
            dp_scraping_list = searchPage.medical_invoices_dp_scraping()
            searchPage.append_list(dp_list, dp_scraping_list, 4)
            if i < int(result_number):
                searchPage.click(Locator.NEXT_DOCUMENT_BUTTON)
            i = i + 1
            searchPage.wait_time(5)

    # result_number > 15
    else:
        while j < full_pagination_page:
            i = 0
            # click the first document
            searchPage.is_clickable(Locator.FIRST_DOCUMENT_LOCATOR)
            searchPage.click(Locator.FIRST_DOCUMENT_LOCATOR)
            while i < 15:
                searchPage.is_clickable(Locator.VALIDATE_BUTTON)
                dp_scraping_list = searchPage.medical_invoices_dp_scraping()
                searchPage.append_list(dp_list, dp_scraping_list, 4)
                if i < 15:
                    searchPage.click(Locator.NEXT_DOCUMENT_BUTTON)
                i = i + 1
                searchPage.wait_time(5)
            searchPage.click(Locator.GO_BACK_BUTTON)

            # Selecting Medical Invoice document subtype
            searchPage.select_document_subtype(Locator.SUBTYPE_DROPDOWN_BUTTON, Locator.SUBTYPE_MEDICAL_INVOICE_CHECK)
            searchPage.is_visible_long(Locator.SEARCH_TABLE)

            # Selecting a Start Date filter
            searchPage.select_start_date(Locator.START_DATEPICKER, ScriptData.START_DATE)
            searchPage.wait_time(3)
            searchPage.select_end_date(Locator.END_DATEPICKER, ScriptData.END_DATE)
            j = j + 1

            l = 0
            while l < j:
                searchPage.scroll_to(Locator.NEXT_PAGE_BUTTON)
                searchPage.hover_to_click(Locator.NEXT_PAGE_BUTTON)
                searchPage.wait_time(2)
                l = l + 1

        # click the first document on the last pagination page
        searchPage.is_clickable(Locator.FIRST_DOCUMENT_LOCATOR)
        searchPage.click(Locator.FIRST_DOCUMENT_LOCATOR)
        while k < last_page_document_number:
            searchPage.is_clickable(Locator.VALIDATE_BUTTON)
            dp_scraping_list = searchPage.medical_invoices_dp_scraping()
            searchPage.append_list(dp_list, dp_scraping_list, 4)
            if k < last_page_document_number:
                searchPage.click(Locator.NEXT_DOCUMENT_BUTTON)
            k = k + 1
            searchPage.wait_time(5)

    # this data point can be adjusted to required data point for
    # a specific document subtype
    dp = {
        'document': document_list,
        'receipt_number': receipt_number_list,
        'claim_amount': claim_amount_list,
        'receipt_date': receipt_date_list
    }


    df = pd.DataFrame(dp, columns=list(dp.keys()))
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    name = "MI_Data_Points_" + date_stamp + ".csv"
    df.to_csv(name, index=False)

# Close the browser window
driver.quit()


