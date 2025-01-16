from selenium.webdriver.common.by import By

class SbisLocators:

    CONTACTS = (By.CSS_SELECTOR, "div.sbisru-Header__menu-link")
    CONTACTS_LINK = (By.XPATH, "//a[@href= '/contacts']")
    REGION = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser.ml-16.ml-xm-0")
    REGION_K = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser.ml-16.ml-xm-0"
                                 " span.sbis_ru-Region-Chooser__text.sbis_ru-link")

    PARTNERS = (By.ID, "city-id-2")
    PARTNERS_TABLE = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1')
    KAMCHATKA = (By.XPATH, "//span[@title= 'Камчатский край']")
    CLOSE_TABLE = (By.CSS_SELECTOR, 'div.sbis_ru-Region-Panel__header-close')
    TITLE = (By.TAG_NAME, "title")
    LOCAL = (By.XPATH, "//div[@class = 'sbisru-Footer__cell pb-16 pb-sm-8']//a[@href='/download']")
    DOWNLOAD = (By.XPATH, "//a[@href= 'https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")

    TENSOR = (By.XPATH, "//a[@href= 'https://tensor.ru/']")



class TensorLocators:

    STRENGTH = (By.XPATH, "//p[@class= 'tensor_ru-Index__card-title tensor_ru-pb-16']")
    ABOUT = (By.XPATH, "//a[@href='/about']")
    WORK = (By.XPATH, "//img[@width='270'][@height='192']")