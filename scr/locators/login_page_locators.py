from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTH_FORM = (By.XPATH, ".//h2[text() = 'Вход']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    REGISTRATION_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    RECOVERY_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")
