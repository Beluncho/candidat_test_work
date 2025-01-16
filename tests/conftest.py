import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())  # is in cache
    driver = webdriver.Chrome(service=driver_service)  # Chrome browser
    driver.maximize_window()    # open full screen
    yield driver
    driver.quit()   # close browser
