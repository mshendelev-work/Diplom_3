import allure

from scr.locators.recovery_page_locators import RecoveryPageLocators
from scr.pages.base_page import BasePage


class RecoveryPage(BasePage):
    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(RecoveryPageLocators.RECOVERY_TEXT_FORM)

    @allure.step('Заполнение формы «Email»')
    def send_email_to_email_field(self, email):
        self.send_keys_to_field(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_recovery_button(self):
        self.click_button(RecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Клик по кнопке «Войти»')
    def click_login_button(self):
        self.click_button(RecoveryPageLocators.LOGIN_BUTTON)

    @allure.step('Заполнение поля «Пароль»')
    def send_password_to_password_field(self, password):
        self.send_keys_to_field(RecoveryPageLocators.PASSWORD_INPUT, password)

    @allure.step('Заполнение поля «Код из письма»')
    def send_code_to_code_field(self, code):
        self.send_keys_to_field(RecoveryPageLocators.CODE_FROM_MAIL, code)

    @allure.step('Клик по кнопке «Сохранить»')
    def click_save_button(self):
        self.click_button(RecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Проверка подсветки поля «Пароль»')
    def check_active_password_field(self, password):
        self.send_password_to_password_field(password)
        self.click_button(RecoveryPageLocators.SHOW_BUTTON)
        return self.check_element(RecoveryPageLocators.INPUT_FIELD_ACTIVE)

    @allure.step('Проверка отображения кнопки «Сохранить»')
    def check_save_button(self):
        return self.check_element(RecoveryPageLocators.SAVE_BUTTON)
