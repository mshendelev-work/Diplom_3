import allure

from scr.constants import BaseUrl, Urls
from scr.pages.home_page import HomePage
from scr.pages.home_page_header import HeaderPage


class TestHomePage:
    @allure.title('Переход по клику на «Конструктор»')
    def test_follow_to_constructor_page(self, driver):
        header = HeaderPage(driver)
        home_page = HomePage(driver)
        home_page.move_to_personal_account_button_and_click()
        header.click_constructor_button()
        assert home_page.check_constructor_form() and home_page.get_current_url() == BaseUrl.BASE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_follow_to_orders_feed_page(self, driver):
        header = HeaderPage(driver)
        home_page = HomePage(driver)
        header.click_feed_button()
        assert home_page.check_orders_feed_form() and home_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_FEED)

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_check_fluorescent_bun_form(self, driver):
        home_page = HomePage(driver)
        home_page.click_fluorescent_bun_button()
        assert home_page.check_fluorescent_bun_form()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_fluorescent_bun_form(self, driver):
        home_page = HomePage(driver)
        home_page.click_fluorescent_bun_button()
        home_page.close_popup_form()
        assert home_page.check_close_fluorescent_bun_form()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_ingredient(self, driver):
        home_page = HomePage(driver)
        home_page.add_bun()
        assert int(home_page.check_counter_ingredient()) > 0

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        home_page = HomePage(driver)
        header.click_constructor_button()
        home_page.create_order()
        assert home_page.check_order_form()
