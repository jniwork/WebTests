from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@data-l="t,login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-l="t,password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//a[@data-l="t,get_qr"]')
    CANT_LOGIN_LINK = (By.XPATH, '//a[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//a[@data-l="t,register"]')
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass