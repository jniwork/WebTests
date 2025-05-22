import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'http://ok.ru'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
LOGIN = 'test@test.ru'

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    LoginPage.attach_screenshot()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


def test_login_with_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login(LOGIN)
    LoginPage.click_login()
    LoginPage.attach_screenshot()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR
