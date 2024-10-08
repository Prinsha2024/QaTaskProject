from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")         
    PASSWORD_INPUT = (By.NAME, "password")       
    LOGIN_BUTTON = (By.ID, "kt_login_signin_submit") 
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".m-alert.m-alert--outline.alert.alert-danger.alert-dismissible")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://account.we-connect.io/login")

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
