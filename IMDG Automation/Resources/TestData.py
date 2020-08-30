class TestData():
    # --- Drivers Path ---
    CHROME_EXECUTABLE_PATH = "../Drivers/chrome/chromedriver81/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "../Drivers/firefox/geckodriver026/win64/geckodriver.exe"
    IE_EXECUTABLE_PATH = "../Drivers/iexplorer/iedriver3150/IEDriverServer.exe"

    # --- URL Info and Credential ---
    BASE_URL = "http://extract-dev.taiger.io:9023/#/"
    USER_NAME = "lilik"
    USER_PASSWORD = "SongJ00ngk!"
    WRONG_USER_NAME = "lilik2"
    WRONG_USER_PASSWORD = "abc123"

    # --- Page Title ---
    LOGIN_PAGE_TITLE = "IMDA Check"
    HOME_PAGE_TITLE = "Extract"

    # --- Text ---
    EMPTY_TEXT = ''
    CREATE_APPLICATION_TOASTER_TEXT = "Claim Application submitted"
    SUBMITTED_ATTACHMENT_NUMBER_MAX = "Attachments (11/11)"
    SUBMITTED_ATTACHMENT_NUMBER_START = "Attachments (0/11)"
    SUBMITTED_ATTACHMENT_NUMBER_DEMO = "Attachments (2/11)"
    LOGIN_ALERT_TEXT = "Wrong Credential"
    STATUS_REJECTED = "Rejected"
    STATUS_VERIFIED = "Verified"

    # --- File Path ---
    NRIC_PATH = "C:\\set1\\NRIC.tif"
    INVOICE_PATH = "C:\\set1\\invoice.pdf"
    ATTENDANCE_PATH = "C:\\set1\\attendance_sheet.jpg"
    SKILLSFUTURE_PATH = "C:\\set1\\skillsfuture.png"
    CERT_COMPLETION_PATH = "C:\\set1\\cert_of_completion.pdf"
    RECEIPT_PATH = "C:\\set1\\receipt.pdf"
    DCA_PATH = "C:\\set1\\DCA.pdf"
    EXAM_RESULT_PATH = "C:\\set1\\exam_result.pdf"
    FORM_1_PATH = "C:\\set1\\form_1.pdf"
    FINAL_CERT_PATH = "C:\\set1\\final_cert.pdf"
    PROOF_MATRICULATION_PATH = "C:\\set1\\proof_of_matriculation.pdf"

    # --- Sort By ---
    LATEST = "Latest-First"
    OLDEST = "Oldest-First"
