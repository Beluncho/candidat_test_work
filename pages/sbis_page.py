from pages.base_page import BasePage
from locators.locators import SbisLocators as Locators
from locators.locators import TensorLocators as T_locators
import time
import os
import requests
import re


class SbisPage(BasePage):

    def find_elements_visible_clickable_on_sbisurl_switch_to_tensorurl_img(self):

        self.element_is_clickable(Locators.CONTACTS)
        assert self.element_is_visible(Locators.CONTACTS).text == 'Контакты'
        assert self.element_is_clickable(Locators.CONTACTS_LINK), 'ContactsNotFound'

        self.element_is_clickable(Locators.CONTACTS_LINK).click()

        assert self.element_is_clickable(Locators.TENSOR), 'NotFoundLinkTensorContact'
        self.element_is_clickable(Locators.TENSOR).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == 'https://tensor.ru/', 'ErrorURL'

        assert self.element_is_visible(T_locators.STRENGTH), 'NotFoundPowerInPeople'
        assert self.element_is_clickable(T_locators.ABOUT), 'NotFoundAbout'

        self.element_is_clickable(T_locators.ABOUT).click()

        assert self.elements_are_visible(T_locators.WORK), 'WidthHeightError'
        time.sleep(5)

    def check_region_change_region_check_url_title(self):
        assert self.element_is_clickable(Locators.CONTACTS), 'NotFoundContacts'

        assert self.element_is_visible(Locators.CONTACTS).text == 'Контакты', 'IncorrectTextContacts'

        self.element_is_clickable(Locators.CONTACTS_LINK).click()   #Для быстрого перехода. В задании не указанно откуда
                                                                    # делать переход

        assert self.element_is_visible(Locators.REGION),'NotFoundRegions'
        assert self.element_is_visible(Locators.PARTNERS_TABLE), 'NotFoundPartnersTable'
        assert self.element_is_visible(Locators.PARTNERS), 'NotFoundPartners'
        assert self.element_is_visible(Locators.PARTNERS).text == 'Ярославль', 'IncorrectTextPartners'
        assert self.element_is_visible(Locators.REGION).text == "Ярославская обл.", 'IncorrectTextRegion'

        self.element_is_clickable(Locators.REGION).click()

        self.element_is_visible(Locators.KAMCHATKA)
        assert self.element_is_visible(Locators.KAMCHATKA), 'NotFoundKamchatka'
        assert self.element_is_visible(Locators.KAMCHATKA).text == "41 Камчатский край", 'IncorrectTextKamchatka'

        self.element_is_clickable(Locators.KAMCHATKA).click()

# TODO: нестабильное место в тесте, как заменить time.sleep?..

        # time.sleep(15)
        self.element_is_clickable(Locators.REGION)

        assert self.element_is_visible(Locators.PARTNERS_TABLE), 'NotFoundPartnersTable'
        assert self.element_is_visible(Locators.PARTNERS).text == 'Петропавловск-Камчатский',\
                                                                                'IncorrectTextPartnersKamchatka'
        assert self.element_is_visible(Locators.REGION).text == 'Камчатский край', 'IncorrectTextRegionKamchatka'
        assert self.driver.current_url == 'https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients', 'NotCurrentUrl'

        assert self.element_is_presence(Locators.TITLE), 'TitleIsNotPresent'
        self.true_text_title("Saby Контакты — Камчатский край"), 'TitleTextError'

        time.sleep(5)

    def sbis_download_local_version(self):
        self.element_is_clickable(Locators.LOCAL)
        assert self.element_is_clickable(Locators.LOCAL)
        self.element_is_clickable(Locators.LOCAL).click()
        self.element_is_clickable(Locators.DOWNLOAD)
        assert self.element_is_clickable(Locators.DOWNLOAD)

        numbers = re.findall(r'\b\d+\b', self.element_is_clickable(Locators.DOWNLOAD).text)
        file_size_for_true = int(numbers[0] + numbers[-1]) / 100
        link_url = self.element_is_clickable(Locators.DOWNLOAD).get_attribute('href')

        self.quit_driver()

        data_link = requests.get(link_url)

        path = 'data.exe'
        with open(path, "wb") as file:
            file.write(data_link.content)

        file_size = round(os.path.getsize(path) / (pow(1024, 2)), 2)

        assert file_size == file_size_for_true, 'file is larger/less than 10.42 mb'

        os.remove(path)
