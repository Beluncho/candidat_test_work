
from pages.sbis_page import SbisPage
import pytest


class TestSabyTensor:

    @pytest.mark.first_scenario
    def test_find_elements_visible_clickable_on_sbisurl_switch_to_tensorurl_img(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.find_elements_visible_clickable_on_sbisurl_switch_to_tensorurl_img()

    @pytest.mark.second_scenario
    def test_check_region_change_region_check_url_title(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.check_region_change_region_check_url_title()

    @pytest.mark.third_scenario
    def test_sbis_download_local_version(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.sbis_download_local_version()
