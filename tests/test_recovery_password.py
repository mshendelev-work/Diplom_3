import allure

from scr.constants import BaseUrl, Urls
from scr.helpers import User
from scr.pages.home_page import HomePage
from scr.pages.login_page import LoginPage
from scr.pages.recovery_page import RecoveryPage


class TestRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_follow_to_the_password_recovery_page(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        home_page.move_to_personal_account_button_and_click()
        login_page.click_recovery_button()
        assert recovery_page.check_recovery_form() and recovery_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_RECOVERY)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_password_and_click_recovery_button(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        home_page.move_to_personal_account_button_and_click()
        login_page.click_recovery_button()
        recovery_page.send_email_to_email_field(User.create_user()["email"])
        recovery_page.click_recovery_button()
        assert recovery_page.check_save_button() and recovery_page.get_current_url() == (BaseUrl.BASE_URL + Urls.URL_RESET_PASSWORD)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_checking_the_show_of_the_password_field(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        user_data = User().create_user()
        home_page.move_to_personal_account_button_and_click()
        login_page.click_recovery_button()
        recovery_page.send_email_to_email_field(user_data.get("email"))
        recovery_page.click_recovery_button()
        assert recovery_page.check_active_password_field(user_data.get("password"))
