import json
import pytest
from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(scope="class") 
    def get_test_data(self):
        with open("data/test_data.json") as file:
            return json.load(file)

    def test_valid_login(self, setup, get_test_data):
        test_data = get_test_data['valid_user']
        login_page = LoginPage(self.driver) 
        login_page.login(test_data['username'], test_data['password'])
       
    def test_invalid_login(self, setup, get_test_data):
        test_data = get_test_data['invalid_user']
        login_page = LoginPage(self.driver)
        login_page.login(test_data['username'], test_data['password'])
       
