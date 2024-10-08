import pytest
from selenium import webdriver
from utils.config import Config

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver 
    driver.quit()

