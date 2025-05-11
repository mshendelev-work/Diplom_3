import allure

from scr.locators.login_page_locators import LoginPageLocators
from scr.pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        return self.check_element(LoginPageLocators.AUTH_FORM)

    @allure.step('Заполнение поля «Email»')
    def send_email_to_email_field(self, email):
        self.send_keys_to_field(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнение поля «Password»')
    def send_password_to_password_field(self, password):
        self.send_keys_to_field(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на кнопку «Войти»')
    def click_login_button(self):
        self.move_to_element_and_click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_button()

    @allure.step('Клик на кнопку «Восстановить пароль»')
    def click_recovery_button(self):
        self.move_to_element_and_click(LoginPageLocators.RECOVERY_BUTTON)

    @allure.step('Клик на кнопку «Зарегистрироваться»')
    def click_register_button(self):
        self.move_to_element_and_click(LoginPageLocators.REGISTRATION_BUTTON)
