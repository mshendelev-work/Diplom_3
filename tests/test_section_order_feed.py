import allure
import pytest

from scr.helpers import Order
from scr.locators.order_feed_locators import OrderFeedLocators
from scr.pages.home_page_header import HeaderPage
from scr.pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_check_order_info_window(self, driver):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_button()
        feed_order.click_order_info()
        assert feed_order.check_order_info_window()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_button()
        user_order = str(order.get_user_orders(create_new_user))
        orders_history_in_feed = feed_order.get_orders_history()
        assert user_order in orders_history_in_feed

    @allure.title('При создании нового заказа счетчик Выполнено за всё время / Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.DAILY_ORDERS_COUNTER, OrderFeedLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_button()
        now_counter = int(feed_order.check_counter_orders(counter))
        order.create_order(create_new_user)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter > now_counter

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_check_user_order_in_job(self, driver, create_new_user, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_button()
        order.create_order(create_new_user)
        orders_in_jobs = feed_order.get_orders_in_jobs()
        user_order = str(order.get_user_orders(create_new_user))
        assert user_order in orders_in_jobs
