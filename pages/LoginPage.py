import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@data-l="t,login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-l="t,password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//a[@data-l="t,get_qr"]')
    RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '(//a[@data-l="t,register"])[2]')
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '(//*[@class="tico"])[1]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_BUTTON)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Заполняем поле логин")
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Заполняем поле пароль")
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.find_element(LoginPageLocators.RESTORE_LINK).click()
        self.attach_screenshot()

    @allure.step("Переходим к регистрации")
    def click_registration(self):
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
        self.attach_screenshot()
