from BaseTestCase import PoolsBaseTest

class Login_Test(PoolsBaseTest):

    driver = webdriver.Chrome()
    driver.get("http://www.singaporepools.com.sg/landing/en/Pages/index.html")
    driver.maximize_window()

    landPage = LandingPage(driver)
    landPage.click_login_button()

    loginpage = LoginPage(driver)
    loginpage.input_username()
