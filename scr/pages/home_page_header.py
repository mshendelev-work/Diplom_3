import allure

from scr.locators.header_locators import HeaderPageLocators
from scr.pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Клик по кнопке «Конструктор»')
    def click_constructor_button(self):
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_feed_button(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_profile_area_button(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT_BUTTON)
