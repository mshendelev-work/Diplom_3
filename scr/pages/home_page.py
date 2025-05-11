import allure

from scr.locators.home_page_locators import HomePageLocators
from scr.pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('Переход к кнопке «Личный Кабинет» и клик на нее')
    def move_to_personal_account_button_and_click(self):
        self.move_to_element_and_click(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form(self):
        return self.check_element(HomePageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(HomePageLocators.ORDER_FEED_FORM)

    @allure.step('Клик по Флюорисцентной булке RD-D3')
    def click_fluorescent_bun_button(self):
        self.click_button(HomePageLocators.FLUORESCENT_BUN_BUTTON)

    @allure.step('Проверка отображения формы «Информации о булке»')
    def check_fluorescent_bun_form(self):
        return self.check_element(HomePageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Проверка закрытия формы «Информация о булке»')
    def check_close_fluorescent_bun_form(self):
        return self.check_element_is_not_visible(HomePageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_popup_form(self):
        self.move_to_element_and_click(HomePageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        self.drag_and_drop(HomePageLocators.FLUORESCENT_BUN_BUTTON, HomePageLocators.ORDER_BASKET)

    @allure.step('Клик по кнопке «Оформить заказ»')
    def click_place_order_button(self):
        self.click_button(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return self.get_text_locator(HomePageLocators.COUNTER_INGREDIENT)

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        return self.check_element(HomePageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        return self.get_text_locator(HomePageLocators.ORDER_NUM)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_home_page(self):
        self.wait_for_load_element(HomePageLocators.PLACE_ORDER_BUTTON)
