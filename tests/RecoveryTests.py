import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'http://ok.ru'
LOGIN_TEXT = 'test@test.ru'
PASSWORD_TEXT = '123'


@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода восстановления после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(LOGIN_TEXT)

    for i in range(3):
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
