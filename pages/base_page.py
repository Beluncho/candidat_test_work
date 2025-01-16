from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, url):
        """

        :param driver: conftest.py
        :param url: is assigned in test
        """
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=30):
        """
        :param locator: is assigned in locators.name_locator
        :param timeout: for stable operation I chose 30. To avoid TimeOutException
        :return:waits for the browser to load to search for element
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=30):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_presence(self,locator,timeout=30):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def true_text_title(self, text, timeout=30):
        Wait(self.driver, timeout).until(EC.title_is(f'{text}'))

    def quit_driver(self):
        self.driver.quit()



