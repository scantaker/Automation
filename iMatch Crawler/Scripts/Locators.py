from selenium.webdriver.common.by import By


class Locators:
    # --- Login Page Locators ---
    LOGIN_BUTTON_HEADER = (By.CSS_SELECTOR, "#login")
    INPUT_USERNAME = (By.CSS_SELECTOR, "input[id='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[id='pass']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[id='loginButton']")

    # --- Home Page Locators ---
    HOME_MESSAGE = (By.CSS_SELECTOR, "#homeMessage")
    SEARCH_PAGE_BUTTON = (By.CSS_SELECTOR, "#search")

    # --- Date Picker Locators ---
    START_DATEPICKER = (By.ID, "initDate")
    END_DATEPICKER = (By.ID, "endDate")
    DAY_DATEPICKER = "//a[@class='ui-state-default']"
    MONTH_DATEPICKER = "//select[@class='ui-datepicker-month']"
    YEAR_DATEPICKER = "//select[@class='ui-datepicker-year']"

    # --- Search Page Locators ---
    SEARCH_TABLE = (By.CSS_SELECTOR, "table.table.table-striped.table-hover.ng-scope")
    SUBTYPE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "div.isearch-filter.col-xs-2.ng-scope > div:nth-child(4) > div > div > div.isearch-filter-item.ng-scope > button")
    SUBTYPE_MEDICAL_CERTIFICATE_CHECK = (By.CSS_SELECTOR, "div.isearch-filter.col-xs-2.ng-scope > div:nth-child(4) > div > div > div.isearch-filter-scroll.ng-scope > div:nth-child(3) > div > input")
    SUBTYPE_MEDICAL_INVOICE_CHECK = (By.CSS_SELECTOR, "div.isearch-filter.col-xs-2.ng-scope > div:nth-child(4) > div > div > div.isearch-filter-scroll.ng-scope > div:nth-child(4) > div > input")
    DOCUMENT_DATE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "div.isearch-filter.col-xs-2.ng-scope > div:nth-child(8) > div > div.isearch-filter-item.ng-scope > button")
    SEARCH_PAGE_SIZE = (By.CSS_SELECTOR, "div.isearch-result > div.isearch-documents.col-xs-10.no-padding.ng-scope > div:nth-child(2) > div:nth-child(2) > div > div.total-results.ng-binding.ng-scope")
    NO_SEARCH_PAGE_SIZE = (By.CSS_SELECTOR, "div.isearch-result > div.isearch-documents.col-xs-10.no-padding.ng-scope > div.ng-binding.ng-scope")
    INIT_DATE_FILTER = (By.CSS_SELECTOR, "div.isearch-top.ng-scope > div.col-xs-6.ng-scope > div > div > span:nth-child(1)")
    END_DATE_FILTER = (By.CSS_SELECTOR, "div.isearch-top.ng-scope > div.col-xs-6.ng-scope > div > div > span:nth-child(2)")
    FIRST_DOCUMENT_LOCATOR = (By.CSS_SELECTOR, "div.isearch-result > div.isearch-documents.col-xs-10.no-padding.ng-scope > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
    SAVE_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.isearch-save > div:nth-child(1) > button")
    SAVE_SEARCH_OVERLAY_TITLE_INPUT = (By.CSS_SELECTOR, "div.isearch-save > div.isearch-overlay.ng-scope.open > div:nth-child(3) > input")
    SAVE_SEARCH_OVERLAY_SAVE_BUTTON = (By.CSS_SELECTOR, "div.isearch-save > div.isearch-overlay.ng-scope.open > div:nth-child(4) > button")
    MY_SAVED_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.isearch-save > div:nth-child(2) > button")

    # --- Document Viewer Button ---
    NEXT_DOCUMENT_BUTTON = (By.CSS_SELECTOR, "div.details-header > div.details-buttons.ng-scope > button:nth-child(3)")
    DOCUMENT_NAME_HEADER = (By.CSS_SELECTOR, "h4.panel-title.ng-binding")
    MED_INVOICES_DP = "//a[@class='ng-binding ng-scope']"
    VALIDATE_BUTTON = (By.CSS_SELECTOR, "#treeContainer > div.editon_buttons.ng-scope > button:nth-child(2)")
    GO_BACK_BUTTON = (By.CSS_SELECTOR, "div.details-buttons.ng-scope > button:nth-child(1)")
    NEXT_PAGE_BUTTON = (By.LINK_TEXT, "›")

