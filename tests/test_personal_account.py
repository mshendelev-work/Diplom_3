import allure

from scr.constants import BaseUrl, Urls
from scr.pages.home_page_header import HeaderPage
from scr.pages.login_page import LoginPage
from scr.pages.personal_page import PersonalPage


class TestPersonalPage:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_follow_to_personal_page(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        personal_page = PersonalPage(driver)
        header.click_profile_area_button()
        assert personal_page.check_profile_area_form() and personal_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_PROFILE)

    @allure.title('Переход в раздел «История заказов»')
    def test_follow_to_feed_orders(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        personal_page = PersonalPage(driver)
        header.click_profile_area_button()
        personal_page.click_history_orders_button()
        assert personal_page.check_profile_area_form() and personal_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_HISTORY_ORDER)

    @allure.title('Выход из аккаунта')
    def test_exit_personal_page(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        personal_page = PersonalPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_button()
        personal_page.click_exit_button()
        print(login_page.get_current_url())
        assert login_page.check_authorization_form_verification() and login_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_LOGIN)
