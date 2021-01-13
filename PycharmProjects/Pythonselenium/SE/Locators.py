from selenium import webdriver
from selenium.webdriver.common.by import By

#from landing page
BUTTON_BUTTON = (By.LINK_TEXT, 'Login')

#from login page
TEXTBOX_USERNAME = (By.NAME, 'username')
TEXTBOX_PASSWORD = (By.NAME, 'password')
BUTTON_LOGIN = (By.TAG_NAME, 'login')
