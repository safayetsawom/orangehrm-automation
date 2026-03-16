import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver(request):
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    