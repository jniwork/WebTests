import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = "http://ok.ru/help"


@allure.suite("Проверка работы страниц в разделе помощь")
@allure.title("Проверка раздела рекламный кабинет")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
