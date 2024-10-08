from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found.")
            return None

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            try:
                element.click()
            except ElementClickInterceptedException:
                print(f"Element with locator {locator} is not clickable.")
    
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()  
            element.send_keys(text)
