from selenium.webdriver.common.by import By
from TestData import TestData

class Locators():
    # --- Page Locators ---
    BODY = (By.XPATH, '//body')

    # --- Login Page Locators ---
    INPUT_USERNAME = (By.CSS_SELECTOR, 'input[id="input-username"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[id="input-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary.px-5.mt-3')
    LOGIN_PAGE_TITLE = (By.CSS_SELECTOR, 'h3.text-black')
    LOGIN_ALERT = (By.CSS_SELECTOR, 'div.text-danger.ml-2')

    # --- Home Page Locators ---
    APP_NAME = (By.CSS_SELECTOR, 'div.app-name')
    APPLICATION_DETAIL_PAGE_TITLE_HEADER = (By.CSS_SELECTOR, 'div.main__header > span')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, 'div.main__filter > button')
    CLAIM_OFFICER_ROLE = (By.CSS_SELECTOR, 'div.tab > a:nth-child(2) > div')
    CLAIM_APPLICATION_ROW_1 = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(1) > td:nth-child(1)')
    CLAIM_APPLICATION_ROW_1_APPLICANT_NAME = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(1) > td:nth-child(2)')
    CLAIM_APPLICATION_ROW_1_STATUS = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(1) > td:nth-child(6)')
    CLAIM_APPLICATION_ROW_2 = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(2) > td:nth-child(1)')
    CLAIM_APPLICATION_ROW_2_APPLICANT_NAME = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(2) > td:nth-child(2)')
    CLAIM_APPLICATION_ROW_3 = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(3) > td:nth-child(1)')
    CLAIM_APPLICATION_ROW_3_APPLICANT_NAME = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(3) > td:nth-child(2)')
    CLAIM_APPLICATION_ROW_4 = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(4) > td:nth-child(1)')
    CLAIM_APPLICATION_ROW_4_APPLICANT_NAME = (By.CSS_SELECTOR, 'table > tbody > tr:nth-child(4) > td:nth-child(2)')
    CLAIM_APPLICATION_TABLE_HEADER = (By.CSS_SELECTOR, 'table > thead > tr')
    CREATE_NEW_APPLICATION = (By.CSS_SELECTOR, 'div.main__header > button.btn.btn-primary.mr-2')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#app > div.dashboard-bg > div.header > div.right-side > div:nth-child(3)')
    NOTIFICATION_TOASTER = (By.CSS_SELECTOR, 'div.notification-title')
    SORT_BY_INPUT = (By.CSS_SELECTOR, "input.vs__search")

    # --- Create & Edit Application Locators ---
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mr-2')
    BACK_TO_APPLICATION_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mr-2')
    MODAL_DELETE_BUTTON = (By.CSS_SELECTOR, '#modal-delete-individual___BV_modal_footer_ > button')
    ATTACHMENT_NUMBER = (By.CSS_SELECTOR, 'div.body__attachment')
    MODAL_PDF_VIEWER = (By.CSS_SELECTOR, 'div.pdf-viewer')
    PDF_VIEWER_ZOOM_OUT = (By.CSS_SELECTOR, 'a.icon.pdf-zoom__out')
    PDF_VIEWER_SCROLL_CLASS = (By.CSS_SELECTOR, 'div.scrolling-document.pdf-document.pdf-viewer__document')
    PDF_VIEWER_DOCUMENT_TITLE = (By.CSS_SELECTOR, '#modal-preview-individual___BV_modal_body_ > div > div > header > span')

    # ## -- Document upload button --
    # UPLOAD_NRIC_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(1) > div.box__action > button')
    # UPLOAD_INVOICE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(2) > div.box__action > button')
    # UPLOAD_ATTENDANCE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(3) > div.box__action > button')
    # UPLOAD_SKILLSFUTURE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(4) > div.box__action > button')
    # UPLOAD_CERT_COMPLETION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(5) > div.box__action > button')
    # UPLOAD_RECEIPT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(6) > div.box__action > button')
    # UPLOAD_DCA_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(7) > div.box__action > button')
    # UPLOAD_EXAM_RESULT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(8) > div.box__action > button')
    # UPLOAD_FORM_1_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(9) > div.box__action > button')
    # UPLOAD_FINAL_CERT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(10) > div.box__action > button')
    # UPLOAD_PROOF_MATRICULATION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(11) > div.box__action > button')

    ## -- Document upload button --
    UPLOAD_NRIC_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(1) > div.box__action > input[type=file]')
    UPLOAD_INVOICE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(2) > div.box__action > input[type=file]')
    UPLOAD_ATTENDANCE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(3) > div.box__action > input[type=file]')
    UPLOAD_SKILLSFUTURE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(4) > div.box__action > input[type=file]')
    UPLOAD_CERT_COMPLETION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(5) > div.box__action > input[type=file]')
    UPLOAD_RECEIPT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(6) > div.box__action > input[type=file]')
    UPLOAD_DCA_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(7) > div.box__action > input[type=file]')
    UPLOAD_EXAM_RESULT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(8) > div.box__action > input[type=file]')
    UPLOAD_FORM_1_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(9) > div.box__action > input[type=file]')
    UPLOAD_FINAL_CERT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(10) > div.box__action > input[type=file]')
    UPLOAD_PROOF_MATRICULATION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(11) > div.box__action > input[type=file]')

    ## -- Document checkmark icon --
    NRIC_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(1) > div.box__info > svg > g')
    INVOICE_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(2) > div.box__info > svg > g')
    ATTENDANCE_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(3) > div.box__info > svg > g')
    SKILLSFUTURE_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(4) > div.box__info > svg > g')
    CERT_COMPLETION_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(5) > div.box__info > svg > g')
    RECEIPT_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(6) > div.box__info > svg > g')
    DCA_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(7) > div.box__info > svg > g')
    EXAM_RESULT_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(8) > div.box__info > svg > g')
    FORM_1_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(9) > div.box__info > svg > g')
    FINAL_CERT_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(10) > div.box__info > svg > g')
    PROOF_MATRICULATION_SUCCESS_ICON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(11) > div.box__info > svg > g')

    ## -- Document remove button
    REMOVE_NRIC_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(1) > div.box__action > button:nth-child(1)')
    REMOVE_INVOICE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(2) > div.box__action > button:nth-child(1)')
    REMOVE_ATTENDANCE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(3) > div.box__action > button:nth-child(1)')
    REMOVE_SKILLSFUTURE_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(4) > div.box__action > button:nth-child(1)')
    REMOVE_CERT_COMPLETION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(5) > div.box__action > button:nth-child(1)')
    REMOVE_RECEIPT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(6) > div.box__action > button:nth-child(1)')
    REMOVE_DCA_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(7) > div.box__action > button:nth-child(1)')
    REMOVE_EXAM_RESULT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(8) > div.box__action > button:nth-child(1)')
    REMOVE_FORM_1_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(9) > div.box__action > button:nth-child(1)')
    REMOVE_FINAL_CERT_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(10) > div.box__action > button:nth-child(1)')
    REMOVE_PROOF_MATRICULATION_BUTTON = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(11) > div.box__action > button:nth-child(1)')

    ## -- Document Viewer --
    NRIC_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(1) > div.box__info > span.box__info__file')
    INVOICE_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(2) > div.box__info > span.box__info__file')
    ATTENDANCE_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(3) > div.box__info > span.box__info__file')
    SKILLSFUTURE_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(4) > div.box__info > span.box__info__file')
    CERT_COMPLETION_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(5) > div.box__info > span.box__info__file')
    RECEIPT_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(6) > div.box__info > span.box__info__file')
    DCA_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(7) > div.box__info > span.box__info__file')
    EXAM_RESULT_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(8) > div.box__info > span.box__info__file')
    FORM_1_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(9) > div.box__info > span.box__info__file')
    FINAL_CERT_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(10) > div.box__info > span.box__info__file')
    PROOF_MATRICULATION_VIEWER = (By.CSS_SELECTOR, 'div.body__individual > div:nth-child(11) > div.box__info > span.box__info__file')


    # --- Application Detail Page Locators ---
    REJECT_APPLICATION_BUTTON = (By.CSS_SELECTOR, 'div.main__header > div > button.btn.btn-no-outline-primary.mr-2')
    VERIFY_APPLICATION_BUTTON = (By.CSS_SELECTOR, 'div.main__header > div > button.btn.btn-primary.mr-2')
    SUPPORT_DOCUMENT_TAB = (By.CSS_SELECTOR, 'div.main__tab > span:nth-child(2)')