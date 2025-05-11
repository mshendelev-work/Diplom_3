import allure

from scr.locators.personal_page_locators import PersonalPageLocators
from scr.pages.base_page import BasePage


class PersonalPage(BasePage):
    @allure.step('Проверка отображения формы «Личного кабинета»')
    def check_profile_area_form(self):
        return self.check_element(PersonalPageLocators.PROFILE_FORM)

    @allure.step('Клик по кнопке «Профиль»')
    def click_profile_button(self):
        self.click_button(PersonalPageLocators.PROFILE_BUTTON)

    @allure.step('Клик по кнопке «История заказов»')
    def click_history_orders_button(self):
        self.click_button(PersonalPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка отображения формы «История заказов»')
    def check_history_form(self):
        return self.check_element(PersonalPageLocators.HISTORY_ORDER_FORM)

    @allure.step('Клик по кнопке «Выход»')
    def click_exit_button(self):
        self.click_button(PersonalPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке «Отмена»')
    def click_cansel_button(self):
        self.click_button(PersonalPageLocators.CANCEL_BUTTON)

    @allure.step('Клик по кнопке «Сохранить»')
    def click_save_button(self):
        self.click_button(PersonalPageLocators.SAVE_BUTTON)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        return self.get_text_locator(PersonalPageLocators.NUMBER_ORDER)
